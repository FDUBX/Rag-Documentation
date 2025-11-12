#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Interface Web RAG avec Flask et LangChain"""

import os
import sys
import yaml
import pickle
from flask import Flask, render_template, request, jsonify
from langchain_community.vectorstores import SKLearnVectorStore
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_core.prompts import PromptTemplate

# Forcer l'encodage UTF-8 pour la console Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

app = Flask(__name__)

def load_config():
    """Charge la configuration depuis config.yaml"""
    with open('config.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

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
    
    # Recréer le vector store
    embeddings = OllamaEmbeddings(model=save_data.get('embedding_model', config['models']['embedding_model']))
    vectorstore = SKLearnVectorStore.from_documents(
        documents=documents,
        embedding=embeddings
    )
    
    return vectorstore

# Charger la configuration et le vector store au démarrage
config = load_config()
vectorstore = load_vectorstore()

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
        
        # Initialiser le LLM avec Ollama
        llm = OllamaLLM(
            model=config['models']['generation_model'],
            temperature=config['models']['temperature']
        )
        
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
        answer = llm.invoke(prompt)
        
        # Extraire les sources
        sources = list(set([doc.metadata.get('source', 'Inconnu') for doc in docs]))
        
        return jsonify({
            'answer': answer,
            'sources': sources,
            'chunks_found': len(docs)
        })
        
    except Exception as e:
        return jsonify({'error': f'Erreur: {str(e)}'}), 500

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
    print("🚀 Démarrage de l'interface web RAG...")
    print(f"📱 Ouvrez votre navigateur sur: http://{config['web']['host']}:{config['web']['port']}")
    
    if vectorstore is None:
        print("⚠️  Vector store non trouvé. Lancez d'abord: python ingest.py")
    
    app.run(
        debug=config['web']['debug'],
        host=config['web']['host'],
        port=config['web']['port']
    )
