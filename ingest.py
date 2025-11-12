#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Indexation de documents avec LangChain et scikit-learn"""

import os
import sys
import yaml
import argparse
import json
from datetime import datetime
from pathlib import Path

# Forcer l'encodage UTF-8 pour la console Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Configurer USER_AGENT par défaut si non défini
if 'USER_AGENT' not in os.environ:
    os.environ['USER_AGENT'] = 'RAG-Documentation/1.0'

from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader, WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import SKLearnVectorStore
from langchain_ollama import OllamaEmbeddings
import pickle

def load_config():
    """Charge la configuration depuis config.yaml"""
    with open('config.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def get_document_loader(file_path):
    """Retourne le loader approprié selon le type de fichier"""
    ext = Path(file_path).suffix.lower()
    
    if ext == '.pdf':
        return PyPDFLoader(file_path)
    elif ext == '.txt':
        return TextLoader(file_path, encoding='utf-8')
    elif ext in ['.docx', '.doc']:
        return Docx2txtLoader(file_path)
    elif ext in ['.md', '.markdown']:
        return TextLoader(file_path, encoding='utf-8')
    else:
        raise ValueError(f"Format non supporté: {ext}")

def load_and_index_documents(documents_to_index, config=None, reset=False):
    """
    Charge et indexe une liste de documents.
    
    Args:
        documents_to_index: Liste de documents LangChain à indexer
        config: Configuration (si None, charge depuis config.yaml)
        reset: Si True, supprime le vector store existant avant d'indexer
    
    Returns:
        Tuple (documents_list, metadatas_list) pour sauvegarde
    """
    if config is None:
        config = load_config()
    
    vectorstore_dir = config['paths']['vectorstore_dir']
    
    # Créer le dossier vectorstore s'il n'existe pas
    os.makedirs(vectorstore_dir, exist_ok=True)
    
    # Paramètres de chunking
    chunk_size = config['chunking']['chunk_size']
    chunk_overlap = config['chunking']['chunk_overlap']
    
    # Initialiser le text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    
    if not documents_to_index:
        return [], []
    
    # Découper en chunks
    splits = text_splitter.split_documents(documents_to_index)
    
    # Créer les embeddings avec Ollama
    ollama_config = config.get('ollama', {})
    # Note: OllamaEmbeddings n'accepte pas timeout directement
    embeddings = OllamaEmbeddings(
        model=config['models']['embedding_model'],
        base_url=ollama_config.get('base_url', 'http://localhost:11434')
    )
    
    # Charger le vector store existant s'il existe (sauf si reset)
    vectorstore_path = os.path.join(vectorstore_dir, "vectorstore.pkl")
    existing_documents = []
    existing_metadatas = []
    
    if reset:
        # Supprimer le vector store existant
        if os.path.exists(vectorstore_path):
            os.remove(vectorstore_path)
            print("🗑️  Vector store existant supprimé (reset)")
    elif os.path.exists(vectorstore_path):
        with open(vectorstore_path, 'rb') as f:
            save_data = pickle.load(f)
            existing_documents = save_data.get('documents', [])
            existing_metadatas = save_data.get('metadatas', [])
    
    # Ajouter les nouveaux documents
    new_documents = [doc.page_content for doc in splits]
    new_metadatas = [doc.metadata for doc in splits]
    
    # Combiner avec les documents existants
    all_documents = existing_documents + new_documents
    all_metadatas = existing_metadatas + new_metadatas
    
    # Recréer tous les documents pour le vector store
    from langchain_core.documents import Document
    all_doc_objects = [
        Document(page_content=doc, metadata=meta)
        for doc, meta in zip(all_documents, all_metadatas)
    ]
    
    # Créer le vector store avec tous les documents
    vectorstore = SKLearnVectorStore.from_documents(
        documents=all_doc_objects,
        embedding=embeddings
    )
    
    # Sauvegarder
    save_data = {
        'documents': all_documents,
        'metadatas': all_metadatas,
        'embedding_model': config['models']['embedding_model']
    }
    with open(vectorstore_path, 'wb') as f:
        pickle.dump(save_data, f)
    
    return new_documents, new_metadatas

def save_indexed_urls(urls, config=None):
    """
    Sauvegarde les URLs indexées dans un fichier JSON.
    
    Args:
        urls: Liste d'URLs à sauvegarder
        config: Configuration (si None, charge depuis config.yaml)
    """
    if config is None:
        config = load_config()
    
    urls_file = config['paths']['urls_file']
    urls_dir = os.path.dirname(urls_file)
    
    # Créer le dossier s'il n'existe pas
    if urls_dir:
        os.makedirs(urls_dir, exist_ok=True)
    
    # Charger les URLs existantes
    indexed_urls = []
    if os.path.exists(urls_file):
        try:
            with open(urls_file, 'r', encoding='utf-8') as f:
                indexed_urls = json.load(f)
        except (json.JSONDecodeError, IOError):
            indexed_urls = []
    
    # Ajouter les nouvelles URLs avec timestamp
    current_time = datetime.now().isoformat()
    for url in urls:
        # Vérifier si l'URL existe déjà
        url_exists = any(item['url'] == url for item in indexed_urls)
        if not url_exists:
            indexed_urls.append({
                'url': url,
                'indexed_at': current_time,
                'last_indexed': current_time
            })
        else:
            # Mettre à jour la date de dernière indexation
            for item in indexed_urls:
                if item['url'] == url:
                    item['last_indexed'] = current_time
                    break
    
    # Sauvegarder
    with open(urls_file, 'w', encoding='utf-8') as f:
        json.dump(indexed_urls, f, indent=2, ensure_ascii=False)

def load_indexed_urls(config=None):
    """
    Charge les URLs indexées depuis le fichier JSON.
    
    Args:
        config: Configuration (si None, charge depuis config.yaml)
    
    Returns:
        Liste des URLs indexées
    """
    if config is None:
        config = load_config()
    
    urls_file = config['paths']['urls_file']
    
    if not os.path.exists(urls_file):
        return []
    
    try:
        with open(urls_file, 'r', encoding='utf-8') as f:
            indexed_urls = json.load(f)
        return [item['url'] for item in indexed_urls]
    except (json.JSONDecodeError, IOError):
        return []

def reindex_saved_urls(config=None, reset=False):
    """
    Réindexe toutes les URLs sauvegardées.
    
    Args:
        config: Configuration (si None, charge depuis config.yaml)
        reset: Si True, réinitialise l'index avant de réindexer
    
    Returns:
        Tuple (success, message, total_chunks)
    """
    if config is None:
        config = load_config()
    
    urls = load_indexed_urls(config)
    
    if not urls:
        return True, "Aucune URL sauvegardée à réindexer", 0
    
    print(f"📋 {len(urls)} URLs sauvegardées trouvées")
    
    if reset:
        # Réinitialiser l'index d'abord
        vectorstore_path = os.path.join(config['paths']['vectorstore_dir'], "vectorstore.pkl")
        if os.path.exists(vectorstore_path):
            os.remove(vectorstore_path)
            print("🗑️  Vector store existant supprimé (reset)")
    
    # Réindexer toutes les URLs
    total_chunks = 0
    failed_urls = []
    
    for url in urls:
        print(f"  🔄 Réindexation de {url}...")
        success, message, chunks = ingest_urls([url], config)
        if success:
            total_chunks += chunks
            print(f"    ✅ {chunks} chunks ajoutés")
        else:
            failed_urls.append(url)
            print(f"    ❌ Erreur: {message}")
    
    if failed_urls:
        return False, f"Erreurs lors de la réindexation de {len(failed_urls)} URL(s)", total_chunks
    
    return True, f"Réindexation réussie: {total_chunks} chunks au total", total_chunks

def ingest_urls(urls, config=None):
    """
    Indexe une ou plusieurs URLs web.
    
    Args:
        urls: Liste d'URLs ou URL unique (string)
        config: Configuration (si None, charge depuis config.yaml)
    
    Returns:
        Tuple (success, message, chunks_count)
    """
    if config is None:
        config = load_config()
    
    # Normaliser en liste
    if isinstance(urls, str):
        urls = [urls]
    
    all_documents = []
    
    # Récupérer le user_agent depuis la config ou utiliser celui de l'environnement
    user_agent = config.get('web_loader', {}).get('user_agent', os.environ.get('USER_AGENT', 'RAG-Documentation/1.0'))
    
    # Définir USER_AGENT dans l'environnement pour WebBaseLoader
    os.environ['USER_AGENT'] = user_agent
    
    for url in urls:
        try:
            loader = WebBaseLoader(url)
            documents = loader.load()
            
            # Ajouter l'URL comme metadata
            for doc in documents:
                doc.metadata['source'] = url
                doc.metadata['type'] = 'web'
            
            all_documents.extend(documents)
        except Exception as e:
            return False, f"Erreur lors du chargement de {url}: {str(e)}", 0
    
    if not all_documents:
        return False, "Aucun contenu récupéré des URLs", 0
    
    try:
        new_docs, new_metas = load_and_index_documents(all_documents, config)
        chunks_count = len(new_docs)
        
        # Sauvegarder les URLs après indexation réussie
        save_indexed_urls(urls, config)
        
        return True, f"Indexation réussie: {chunks_count} chunks ajoutés", chunks_count
    except Exception as e:
        return False, f"Erreur lors de l'indexation: {str(e)}", 0

def ingest_documents(reset=False):
    """
    Indexe tous les documents du dossier data/
    
    Args:
        reset: Si True, supprime le vector store existant avant d'indexer
    """
    config = load_config()
    
    data_dir = config['paths']['data_dir']
    
    # Charger tous les documents
    all_documents = []
    data_path = Path(data_dir)
    
    print(f"📂 Recherche de documents dans {data_dir}...")
    
    # Formats supportés
    supported_extensions = ['.pdf', '.txt', '.docx', '.doc', '.md', '.markdown']
    
    for file_path in data_path.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in supported_extensions:
            print(f"  📄 Traitement de {file_path.name}...")
            try:
                loader = get_document_loader(str(file_path))
                documents = loader.load()
                
                # Ajouter le nom du fichier comme metadata
                for doc in documents:
                    doc.metadata['source'] = file_path.name
                    doc.metadata['type'] = 'file'
                
                all_documents.extend(documents)
                print(f"    ✅ {len(documents)} pages chargées")
            except Exception as e:
                print(f"    ❌ Erreur: {e}")
    
    if not all_documents:
        print("⚠️  Aucun document trouvé!")
        return
    
    print(f"\n📝 Découpage de {len(all_documents)} documents en chunks...")
    
    try:
        new_docs, new_metas = load_and_index_documents(all_documents, config, reset=reset)
        chunks_count = len(new_docs)
        print(f"✅ {chunks_count} chunks créés et indexés")
        print(f"\n🎉 Indexation terminée! {chunks_count} chunks indexés.")
    except Exception as e:
        print(f"❌ Erreur lors de l'indexation: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Indexe les documents du dossier data/ dans le vector store',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  python ingest.py                    # Indexe les documents (ajoute aux existants)
  python ingest.py --reset            # Réinitialise l'index avant d'indexer
  python ingest.py --reset --reindex-urls  # Reset puis réindexe les URLs sauvegardées
  python ingest.py --list-urls        # Liste les URLs sauvegardées
  python ingest.py --reindex-urls     # Réindexe les URLs sauvegardées
        """
    )
    parser.add_argument(
        '--reset',
        action='store_true',
        help='Supprime le vector store existant avant d\'indexer (réinitialise l\'index)'
    )
    parser.add_argument(
        '--reindex-urls',
        action='store_true',
        help='Réindexe toutes les URLs sauvegardées'
    )
    parser.add_argument(
        '--list-urls',
        action='store_true',
        help='Liste les URLs sauvegardées'
    )
    
    args = parser.parse_args()
    
    config = load_config()
    
    # Lister les URLs sauvegardées
    if args.list_urls:
        urls = load_indexed_urls(config)
        if urls:
            print(f"📋 {len(urls)} URL(s) sauvegardée(s):\n")
            for i, url in enumerate(urls, 1):
                print(f"  {i}. {url}")
        else:
            print("📋 Aucune URL sauvegardée")
        sys.exit(0)
    
    # Réindexer les URLs sauvegardées
    if args.reindex_urls:
        success, message, total_chunks = reindex_saved_urls(config, reset=args.reset)
        if success:
            print(f"\n✅ {message}")
        else:
            print(f"\n❌ {message}")
        sys.exit(0)
    
    # Indexation normale des documents
    ingest_documents(reset=args.reset)
