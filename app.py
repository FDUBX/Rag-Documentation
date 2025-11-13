#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Interface Web RAG avec Flask et LangChain"""

import os
import sys
import yaml
import pickle
import json
import logging
import uuid
from datetime import datetime
from logging.handlers import RotatingFileHandler
from pathlib import Path
from flask import Flask, render_template, request, jsonify
from langchain_community.vectorstores import SKLearnVectorStore
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_core.prompts import PromptTemplate
from ingest import ingest_urls
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env si le fichier existe
load_dotenv()

# Forcer l'encodage UTF-8 pour la console Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Configurer USER_AGENT par défaut si non défini
if 'USER_AGENT' not in os.environ:
    os.environ['USER_AGENT'] = 'RAG-Documentation/1.0'

app = Flask(__name__)

def setup_logging(config):
    """Configure le système de logging"""
    log_config = config.get('logging', {})
    log_level = getattr(logging, log_config.get('level', 'INFO').upper(), logging.INFO)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Handler console (avec gestion UTF-8 pour Windows)
    class UTF8StreamHandler(logging.StreamHandler):
        """Handler qui gère l'encodage UTF-8 sur Windows"""
        def emit(self, record):
            try:
                msg = self.format(record)
                if sys.platform == 'win32':
                    # Encoder en UTF-8 et remplacer les caractères non encodables
                    msg = msg.encode('utf-8', errors='replace').decode('utf-8', errors='replace')
                stream = self.stream
                stream.write(msg + self.terminator)
                self.flush()
            except Exception:
                self.handleError(record)
    
    console_handler = UTF8StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(log_level)
    
    # Handler fichier (si configuré)
    log_file = log_config.get('file')
    handlers = [console_handler]
    
    if log_file:
        # Créer le dossier de logs si nécessaire
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Handler rotatif pour les fichiers
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=log_config.get('max_bytes', 10485760),  # 10MB par défaut
            backupCount=log_config.get('backup_count', 5)
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(log_level)
        handlers.append(file_handler)
    
    # Configurer le logger racine
    logging.basicConfig(
        level=log_level,
        handlers=handlers,
        force=True  # Forcer la reconfiguration
    )
    
    # Réduire le niveau de log de certaines bibliothèques
    logging.getLogger('werkzeug').setLevel(logging.WARNING)
    logging.getLogger('urllib3').setLevel(logging.WARNING)
    
    return logging.getLogger(__name__)

def load_config():
    """Charge la configuration depuis config.yaml"""
    with open('config.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def is_production():
    """Détecte si on est en mode production"""
    flask_env = os.environ.get('FLASK_ENV', '').lower()
    return flask_env == 'production' or os.environ.get('PRODUCTION', '').lower() == 'true'

def load_vectorstore():
    """Charge le vector store depuis le fichier"""
    config = load_config()
    vectorstore_path = os.path.join(config['paths']['vectorstore_dir'], 'vectorstore.pkl')
    
    if not os.path.exists(vectorstore_path):
        return None
    
    # Charger les données sauvegardées
    with open(vectorstore_path, 'rb') as f:
        save_data = pickle.load(f)
    
    # Recréer les documents LangChain
    from langchain_core.documents import Document
    documents = [
        Document(page_content=doc, metadata=meta)
        for doc, meta in zip(save_data['documents'], save_data['metadatas'])
    ]
    
    # Recréer le vector store (avec timeout pour les embeddings)
    ollama_config = config.get('ollama', {})
    # Note: OllamaEmbeddings n'accepte pas timeout directement, on utilise base_url avec timeout dans l'URL si nécessaire
    embeddings = OllamaEmbeddings(
        model=save_data.get('embedding_model', config['models']['embedding_model']),
        base_url=ollama_config.get('base_url', 'http://localhost:11434')
    )
    vectorstore = SKLearnVectorStore.from_documents(
        documents=documents,
        embedding=embeddings
    )
    
    return vectorstore

# Charger la configuration et le vector store au démarrage
config = load_config()

# Configurer le logging
logger = setup_logging(config)
logger.info("Demarrage de l'application RAG")

# Détecter le mode production
production_mode = is_production()
if production_mode:
    logger.info("Mode PRODUCTION detecte - debug desactive")
    config['web']['debug'] = False
else:
    logger.info("Mode DEVELOPPEMENT - debug active")

vectorstore = load_vectorstore()
if vectorstore is None:
    logger.warning("Vector store non trouve. Lancez d'abord: python ingest.py")
else:
    logger.info("Vector store charge avec succes")

def reload_vectorstore():
    """Recharge le vector store depuis le fichier"""
    global vectorstore
    vectorstore = load_vectorstore()
    return vectorstore

# ==================== GESTION DES CONVERSATIONS ====================

def get_conversations_file_path():
    """Retourne le chemin du fichier de stockage des conversations"""
    conversations_file = config.get('paths', {}).get('conversations_file', './vectorstore/conversations.json')
    return conversations_file

def load_conversations():
    """Charge toutes les conversations depuis le fichier"""
    conversations_file = get_conversations_file_path()
    
    if not os.path.exists(conversations_file):
        return {}
    
    try:
        with open(conversations_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        logger.warning(f"Erreur lors du chargement des conversations: {e}")
        return {}

def save_conversations(conversations):
    """Sauvegarde toutes les conversations dans le fichier"""
    conversations_file = get_conversations_file_path()
    conversations_dir = os.path.dirname(conversations_file)
    
    # Créer le dossier s'il n'existe pas
    if conversations_dir:
        os.makedirs(conversations_dir, exist_ok=True)
    
    try:
        with open(conversations_file, 'w', encoding='utf-8') as f:
            json.dump(conversations, f, indent=2, ensure_ascii=False)
    except IOError as e:
        logger.error(f"Erreur lors de la sauvegarde des conversations: {e}")

def create_conversation(title=None, filtered_sources=None):
    """Crée une nouvelle conversation
    
    Args:
        title: Titre de la conversation
        filtered_sources: Liste des sources à filtrer (None = toutes les sources)
    """
    conversations = load_conversations()
    
    conversation_id = str(uuid.uuid4())
    now = datetime.now().isoformat()
    
    if not title:
        title = f"Conversation {len(conversations) + 1}"
    
    conversation = {
        'id': conversation_id,
        'title': title,
        'created_at': now,
        'updated_at': now,
        'messages': [],
        'filtered_sources': filtered_sources if filtered_sources else None  # None = toutes les sources
    }
    
    conversations[conversation_id] = conversation
    save_conversations(conversations)
    
    logger.info(f"Nouvelle conversation creee: {conversation_id} - {title} (sources: {len(filtered_sources) if filtered_sources else 'toutes'})")
    return conversation

def get_conversation(conversation_id):
    """Récupère une conversation par son ID"""
    conversations = load_conversations()
    return conversations.get(conversation_id)

def add_message_to_conversation(conversation_id, role, content, sources=None):
    """Ajoute un message à une conversation"""
    conversations = load_conversations()
    
    if conversation_id not in conversations:
        logger.warning(f"Conversation {conversation_id} non trouvee")
        return None
    
    conversation = conversations[conversation_id]
    now = datetime.now().isoformat()
    
    message = {
        'role': role,  # 'user' ou 'assistant'
        'content': content,
        'timestamp': now,
        'sources': sources or []
    }
    
    conversation['messages'].append(message)
    conversation['updated_at'] = now
    
    # Mettre à jour le titre si c'est le premier message utilisateur
    if len(conversation['messages']) == 1 and role == 'user':
        # Utiliser les 50 premiers caractères comme titre
        title = content[:50] + ('...' if len(content) > 50 else '')
        conversation['title'] = title
    
    save_conversations(conversations)
    return message

def delete_conversation(conversation_id):
    """Supprime une conversation"""
    conversations = load_conversations()
    
    if conversation_id in conversations:
        del conversations[conversation_id]
        save_conversations(conversations)
        logger.info(f"Conversation supprimee: {conversation_id}")
        return True
    
    return False

def list_conversations():
    """Liste toutes les conversations, triées par date de mise à jour"""
    conversations = load_conversations()
    
    # Convertir en liste et trier par updated_at (plus récent en premier)
    conversations_list = list(conversations.values())
    conversations_list.sort(key=lambda x: x.get('updated_at', ''), reverse=True)
    
    return conversations_list

@app.route('/')
def index():
    """Page d'accueil - Interface de chat"""
    return render_template('chat.html')

@app.route('/api/query', methods=['POST'])
def query():
    """API pour les requêtes RAG"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Données JSON requises'}), 400
        
        query_text = data.get('query', '')
        if not query_text:
            return jsonify({'error': 'Aucune question fournie'}), 400
        
        conversation_id = data.get('conversation_id')
        
        # Créer une nouvelle conversation si aucune n'est fournie
        if not conversation_id:
            conversation = create_conversation()
            conversation_id = conversation['id']
        else:
            # Vérifier que la conversation existe
            conversation = get_conversation(conversation_id)
            if not conversation:
                return jsonify({'error': 'Conversation non trouvée'}), 404
        
        if vectorstore is None:
            return jsonify({'error': 'Vector store non trouvé. Lancez d\'abord l\'indexation avec: python ingest.py'}), 400
        
        # Ajouter le message utilisateur à la conversation
        add_message_to_conversation(conversation_id, 'user', query_text)
        
        # Initialiser le LLM avec Ollama (avec timeout et max_tokens)
        ollama_config = config.get('ollama', {})
        llm = OllamaLLM(
            model=config['models']['generation_model'],
            temperature=config['models']['temperature'],
            num_predict=config['models'].get('max_tokens', 1024),  # max_tokens pour Ollama
            base_url=ollama_config.get('base_url', 'http://localhost:11434'),
            timeout=ollama_config.get('timeout', 120)
        )
        
        logger.info(f"Requete: {query_text[:100]}...")
        
        # Récupérer les sources filtrées de la conversation
        conversation = get_conversation(conversation_id)
        filtered_sources = conversation.get('filtered_sources') if conversation else None
        
        # Créer le retriever
        retriever = vectorstore.as_retriever(
            search_kwargs={"k": config['search']['top_k']}
        )
        
        # Récupérer les documents pertinents
        docs = retriever.invoke(query_text)
        
        # Filtrer par sources si des sources sont spécifiées
        if filtered_sources and len(filtered_sources) > 0:
            docs = [doc for doc in docs if doc.metadata.get('source') in filtered_sources]
            if not docs:
                logger.warning(f"Aucun document trouvé dans les sources filtrées: {filtered_sources}")
                return jsonify({
                    'error': f'Aucun document trouvé dans les sources sélectionnées: {", ".join(filtered_sources)}',
                    'conversation_id': conversation_id
                }), 404
        
        # Construire le contexte de manière structurée avec les sources
        context_parts = []
        for i, doc in enumerate(docs, 1):
            source = doc.metadata.get('source', 'Document inconnu')
            content = doc.page_content.strip()
            context_parts.append(f"[Document {i} - Source: {source}]\n{content}")
        
        context = "\n\n---\n\n".join(context_parts)
        
        # Charger le template de prompt depuis la configuration
        prompt_template = config.get('prompt', {}).get('template', 
            """Utilise les extraits de documents suivants pour répondre à la question. 
Si tu ne trouves pas la réponse dans les documents, dis-le clairement.

Contexte:
{context}

Question: {question}

Réponse:""")
        
        prompt = prompt_template.format(context=context, question=query_text)
        
        # Générer la réponse
        logger.debug(f"Génération de la réponse avec {len(docs)} chunks...")
        answer = llm.invoke(prompt)
        
        # Extraire les sources
        sources = list(set([doc.metadata.get('source', 'Inconnu') for doc in docs]))
        
        # Ajouter la réponse de l'assistant à la conversation
        add_message_to_conversation(conversation_id, 'assistant', answer, sources)
        
        logger.info(f"Reponse generee - {len(sources)} source(s), {len(docs)} chunk(s)")
        
        return jsonify({
            'answer': answer,
            'sources': sources,
            'chunks_found': len(docs),
            'conversation_id': conversation_id
        })
        
    except Exception as e:
        logger.error(f"Erreur lors de la requete: {str(e)}", exc_info=True)
        error_msg = str(e) if config['web']['debug'] else "Une erreur est survenue lors du traitement de votre requête"
        return jsonify({'error': error_msg}), 500

@app.route('/api/documents')
def list_documents():
    """Liste les documents disponibles dans le dossier data/ et les URLs indexées"""
    try:
        documents = []
        urls = []
        total_size = 0
        
        # Récupérer les documents du dossier data/
        data_dir = config['paths']['data_dir']
        if os.path.exists(data_dir):
            for filename in os.listdir(data_dir):
                filepath = os.path.join(data_dir, filename)
                if os.path.isfile(filepath):
                    file_size = os.path.getsize(filepath)
                    total_size += file_size
                    documents.append({
                        'name': filename,
                        'size': file_size,
                        'size_formatted': f"{file_size / 1024:.1f} KB" if file_size < 1024*1024 else f"{file_size / (1024*1024):.1f} MB",
                        'type': 'file'
                    })
        
        documents.sort(key=lambda x: x['name'])
        
        # Récupérer les URLs indexées
        from ingest import load_indexed_urls
        indexed_urls = load_indexed_urls(config)
        for url in indexed_urls:
            urls.append({
                'name': url,
                'url': url,
                'type': 'url'
            })
        
        urls.sort(key=lambda x: x['name'])
        
        # Formater la taille totale
        if total_size < 1024:
            total_size_formatted = f"{total_size} B"
        elif total_size < 1024*1024:
            total_size_formatted = f"{total_size / 1024:.1f} KB"
        else:
            total_size_formatted = f"{total_size / (1024*1024):.1f} MB"
        
        total_count = len(documents) + len(urls)
        
        # Retourner JSON si demandé, sinon HTML
        if request.headers.get('Accept', '').startswith('application/json'):
            return jsonify({
                'success': True,
                'documents': documents,
                'urls': urls,
                'count': total_count
            })
        
        return render_template('documents.html', 
                             documents=documents,
                             urls=urls,
                             count=total_count,
                             documents_count=len(documents),
                             urls_count=len(urls),
                             total_size_formatted=total_size_formatted)
    except Exception as e:
        if request.headers.get('Accept', '').startswith('application/json'):
            return jsonify({
                'success': False,
                'error': str(e),
                'documents': [],
                'urls': []
            }), 500
        return render_template('documents.html', error=str(e), count=0, documents_count=0, urls_count=0, total_size_formatted='0 B')

@app.route('/api/sources')
def list_sources():
    """Liste toutes les sources disponibles (documents + URLs indexées)"""
    try:
        sources = []
        
        # Récupérer les documents du dossier data/
        data_dir = config['paths']['data_dir']
        if os.path.exists(data_dir):
            for filename in os.listdir(data_dir):
                filepath = os.path.join(data_dir, filename)
                if os.path.isfile(filepath):
                    sources.append({
                        'name': filename,
                        'type': 'file',
                        'source': filename
                    })
        
        # Récupérer les URLs indexées
        from ingest import load_indexed_urls
        indexed_urls = load_indexed_urls(config)
        for url in indexed_urls:
            sources.append({
                'name': url,
                'type': 'url',
                'source': url
            })
        
        # Trier par type puis par nom
        sources.sort(key=lambda x: (x['type'], x['name']))
        
        return jsonify({
            'success': True,
            'sources': sources,
            'count': len(sources)
        })
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des sources: {str(e)}", exc_info=True)
        return jsonify({
            'success': False,
            'error': str(e),
            'sources': []
        }), 500

@app.route('/api/index-url', methods=['POST'])
def index_url():
    """API pour indexer une ou plusieurs URLs web"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'error': 'Données JSON requises'}), 400
        
        urls = data.get('urls', [])
        if not urls:
            return jsonify({'success': False, 'error': 'Aucune URL fournie'}), 400
        
        # Normaliser en liste si une seule URL est fournie
        if isinstance(urls, str):
            urls = [urls]
        
        logger.info(f"Indexation de {len(urls)} URL(s): {urls}")
        
        # Indexer les URLs
        success, message, chunks_count = ingest_urls(urls, config)
        
        if success:
            # Recharger le vector store
            reload_vectorstore()
            logger.info(f"Indexation reussie: {chunks_count} chunks ajoutes")
            return jsonify({
                'success': True,
                'message': message,
                'chunks_count': chunks_count,
                'urls_indexed': urls
            })
        else:
            logger.error(f"Erreur d'indexation: {message}")
            return jsonify({
                'success': False,
                'error': message
            }), 400
        
    except Exception as e:
        logger.error(f"Erreur lors de l'indexation d'URLs: {str(e)}", exc_info=True)
        error_msg = str(e) if config['web']['debug'] else "Une erreur est survenue lors de l'indexation"
        return jsonify({
            'success': False,
            'error': error_msg
        }), 500

@app.route('/api/status')
def status():
    """Vérification du statut du système"""
    try:
        # Vérifier Ollama (basique)
        try:
            from langchain_ollama import OllamaLLM
            llm = OllamaLLM(model=config['models']['generation_model'])
            llm.invoke("test")
            ollama_status = "OK"
        except:
            ollama_status = "Erreur"
        
        # Vérifier le vector store
        vectorstore_path = os.path.join(config['paths']['vectorstore_dir'], 'vectorstore.pkl')
        vectorstore_status = "OK" if os.path.exists(vectorstore_path) else "Index manquant"
        
        status = 'OK' if ollama_status == 'OK' and vectorstore_status == 'OK' else 'Erreur'
        
        # Retourner JSON si demandé, sinon HTML
        if request.headers.get('Accept', '').startswith('application/json'):
            return jsonify({
                'ollama': ollama_status,
                'vectorstore': vectorstore_status,
                'status': status
            })
        
        # Préparer les données pour le template HTML
        from datetime import datetime
        timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        embedding_model = config['models']['embedding_model']
        generation_model = config['models']['generation_model']
        ollama_base_url = config.get('ollama', {}).get('base_url', 'http://localhost:11434')
        
        return render_template('status.html',
                             status=status,
                             ollama=ollama_status,
                             vectorstore=vectorstore_status,
                             timestamp=timestamp,
                             embedding_model=embedding_model,
                             generation_model=generation_model,
                             ollama_base_url=ollama_base_url)
    except Exception as e:
        if request.headers.get('Accept', '').startswith('application/json'):
            return jsonify({
                'error': str(e),
                'status': 'Erreur'
            }), 500
        
        from datetime import datetime
        return render_template('status.html',
                             status='Erreur',
                             ollama='Erreur',
                             vectorstore='Erreur',
                             timestamp=datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                             embedding_model='N/A',
                             generation_model='N/A',
                             ollama_base_url='N/A',
                             error=str(e))

# ==================== ENDPOINTS CONVERSATIONS ====================

@app.route('/api/conversations', methods=['GET'])
def get_conversations():
    """Liste toutes les conversations"""
    try:
        conversations = list_conversations()
        return jsonify({
            'success': True,
            'conversations': conversations,
            'count': len(conversations)
        })
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des conversations: {str(e)}", exc_info=True)
        return jsonify({
            'success': False,
            'error': str(e),
            'conversations': []
        }), 500

@app.route('/api/conversations', methods=['POST'])
def create_new_conversation():
    """Crée une nouvelle conversation"""
    try:
        data = request.get_json() or {}
        title = data.get('title')
        filtered_sources = data.get('filtered_sources')  # Liste des sources à filtrer (None = toutes)
        
        # Normaliser filtered_sources : si liste vide, considérer comme None (toutes les sources)
        if filtered_sources is not None and len(filtered_sources) == 0:
            filtered_sources = None
        
        conversation = create_conversation(title=title, filtered_sources=filtered_sources)
        
        return jsonify({
            'success': True,
            'conversation': conversation
        })
    except Exception as e:
        logger.error(f"Erreur lors de la création de la conversation: {str(e)}", exc_info=True)
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/conversations/<conversation_id>', methods=['GET'])
def get_conversation_by_id(conversation_id):
    """Récupère une conversation par son ID"""
    try:
        conversation = get_conversation(conversation_id)
        
        if not conversation:
            return jsonify({
                'success': False,
                'error': 'Conversation non trouvée'
            }), 404
        
        return jsonify({
            'success': True,
            'conversation': conversation
        })
    except Exception as e:
        logger.error(f"Erreur lors de la récupération de la conversation: {str(e)}", exc_info=True)
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/conversations/<conversation_id>', methods=['DELETE'])
def delete_conversation_by_id(conversation_id):
    """Supprime une conversation"""
    try:
        success = delete_conversation(conversation_id)
        
        if not success:
            return jsonify({
                'success': False,
                'error': 'Conversation non trouvée'
            }), 404
        
        return jsonify({
            'success': True,
            'message': 'Conversation supprimée'
        })
    except Exception as e:
        logger.error(f"Erreur lors de la suppression de la conversation: {str(e)}", exc_info=True)
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/conversations/<conversation_id>/title', methods=['PUT'])
def update_conversation_title(conversation_id):
    """Met à jour le titre d'une conversation"""
    try:
        data = request.get_json()
        if not data or 'title' not in data:
            return jsonify({
                'success': False,
                'error': 'Titre requis'
            }), 400
        
        conversations = load_conversations()
        
        if conversation_id not in conversations:
            return jsonify({
                'success': False,
                'error': 'Conversation non trouvée'
            }), 404
        
        conversations[conversation_id]['title'] = data['title']
        conversations[conversation_id]['updated_at'] = datetime.now().isoformat()
        save_conversations(conversations)
        
        return jsonify({
            'success': True,
            'conversation': conversations[conversation_id]
        })
    except Exception as e:
        logger.error(f"Erreur lors de la mise à jour du titre: {str(e)}", exc_info=True)
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    logger.info(f"Ouvrez votre navigateur sur: http://{config['web']['host']}:{config['web']['port']}")
    
    if vectorstore is None:
        logger.warning("Vector store non trouve. Lancez d'abord: python ingest.py")
    
    app.run(
        debug=config['web']['debug'],
        host=config['web']['host'],
        port=config['web']['port'],
        use_reloader=config['web'].get('use_reloader', False)
    )
