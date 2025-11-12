#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Indexation de documents avec LangChain et scikit-learn"""

import os
import sys
import yaml
from pathlib import Path

# Forcer l'encodage UTF-8 pour la console Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader
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

def ingest_documents():
    """Indexe tous les documents du dossier data/"""
    config = load_config()
    
    data_dir = config['paths']['data_dir']
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
                
                all_documents.extend(documents)
                print(f"    ✅ {len(documents)} pages chargées")
            except Exception as e:
                print(f"    ❌ Erreur: {e}")
    
    if not all_documents:
        print("⚠️  Aucun document trouvé!")
        return
    
    print(f"\n📝 Découpage de {len(all_documents)} documents en chunks...")
    splits = text_splitter.split_documents(all_documents)
    print(f"✅ {len(splits)} chunks créés")
    
    # Créer les embeddings avec Ollama
    print(f"\n🔢 Génération des embeddings avec {config['models']['embedding_model']}...")
    embeddings = OllamaEmbeddings(model=config['models']['embedding_model'])
    
    # Créer le vector store avec scikit-learn
    print("💾 Création du vector store...")
    vectorstore = SKLearnVectorStore.from_documents(
        documents=splits,
        embedding=embeddings
    )
    
    # Sauvegarder les données nécessaires pour recréer le vector store
    # (SKLearnVectorStore ne peut pas être sérialisé directement avec pickle)
    vectorstore_path = os.path.join(vectorstore_dir, "vectorstore.pkl")
    import numpy as np
    
    # Extraire les documents et métadonnées
    documents_list = [doc.page_content for doc in splits]
    metadatas_list = [doc.metadata for doc in splits]
    
    # Sauvegarder les données
    save_data = {
        'documents': documents_list,
        'metadatas': metadatas_list,
        'embedding_model': config['models']['embedding_model']
    }
    with open(vectorstore_path, 'wb') as f:
        pickle.dump(save_data, f)
    
    print(f"✅ Vector store sauvegardé dans {vectorstore_path}")
    print(f"\n🎉 Indexation terminée! {len(splits)} chunks indexés.")

if __name__ == '__main__':
    ingest_documents()
