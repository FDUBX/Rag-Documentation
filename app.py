#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Interface Web RAG avec Flask et LangChain"""

import os
import sys
import yaml
import pickle
import logging
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
        
        if vectorstore is None:
            return jsonify({'error': 'Vector store non trouvé. Lancez d\'abord l\'indexation avec: python ingest.py'}), 400
        
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
        
        # Créer le retriever
        retriever = vectorstore.as_retriever(
            search_kwargs={"k": config['search']['top_k']}
        )
        
        # Récupérer les documents pertinents
        docs = retriever.invoke(query_text)
        
        # Construire le contexte
        context = "\n\n".join([doc.page_content for doc in docs])
        
        # Créer le prompt
        prompt_template = """Utilise les extraits de documents suivants pour répondre à la question. 
Si tu ne trouves pas la réponse dans les documents, dis-le clairement.

Contexte:
{context}

Question: {question}

Réponse:"""
        
        prompt = prompt_template.format(context=context, question=query_text)
        
        # Générer la réponse
        logger.debug(f"Génération de la réponse avec {len(docs)} chunks...")
        answer = llm.invoke(prompt)
        
        # Extraire les sources
        sources = list(set([doc.metadata.get('source', 'Inconnu') for doc in docs]))
        
        logger.info(f"Reponse generee - {len(sources)} source(s), {len(docs)} chunk(s)")
        
        return jsonify({
            'answer': answer,
            'sources': sources,
            'chunks_found': len(docs)
        })
        
    except Exception as e:
        logger.error(f"Erreur lors de la requete: {str(e)}", exc_info=True)
        error_msg = str(e) if config['web']['debug'] else "Une erreur est survenue lors du traitement de votre requête"
        return jsonify({'error': error_msg}), 500

@app.route('/api/documents')
def list_documents():
    """Liste les documents disponibles dans le dossier data/"""
    try:
        data_dir = config['paths']['data_dir']
        if not os.path.exists(data_dir):
            return jsonify({
                'success': False,
                'error': f'Dossier {data_dir} non trouvé',
                'documents': []
            }), 404
        
        documents = []
        for filename in os.listdir(data_dir):
            filepath = os.path.join(data_dir, filename)
            if os.path.isfile(filepath):
                file_size = os.path.getsize(filepath)
                documents.append({
                    'name': filename,
                    'size': file_size,
                    'size_formatted': f"{file_size / 1024:.1f} KB" if file_size < 1024*1024 else f"{file_size / (1024*1024):.1f} MB"
                })
        
        documents.sort(key=lambda x: x['name'])
        
        return jsonify({
            'success': True,
            'documents': documents,
            'count': len(documents)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'documents': []
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
        
        return jsonify({
            'ollama': ollama_status,
            'vectorstore': vectorstore_status,
            'status': status
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'Erreur'
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
