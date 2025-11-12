# RAG Project - Documentation Technique

Projet RAG (Retrieval-Augmented Generation) pour accéder à de la documentation technique via un chat, basé sur LangChain et Ollama.

## 📋 Prérequis

1. **Python 3.8+**
2. **Ollama** installé et en cours d'exécution
3. Les modèles Ollama suivants :
   - `mxbai-embed-large` (pour les embeddings)
   - `llama3.2` (pour la génération)

## 🚀 Installation

1. **Créer un environnement virtuel** (recommandé) :
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac
```

2. **Installer les dépendances** :
```bash
pip install -r requirements.txt
```

3. **Installer les modèles Ollama** :
```bash
ollama pull mxbai-embed-large
ollama pull llama3.2
```

## 📝 Utilisation

### 1. Indexer les documents

Placez vos documents techniques dans le dossier `data/` (PDF, TXT, DOCX, MD).

Puis lancez l'indexation :
```bash
python ingest.py
```

Cette commande va :
- Charger tous les documents du dossier `data/`
- Les découper en chunks
- Générer les embeddings avec Ollama
- Créer le vector store avec scikit-learn

**Options disponibles** :

- `--reset` : Réinitialise complètement l'index (supprime le vector store existant avant d'indexer)
  ```bash
  python ingest.py --reset
  ```

- `--list-urls` : Liste toutes les URLs sauvegardées
  ```bash
  python ingest.py --list-urls
  ```

- `--reindex-urls` : Réindexe toutes les URLs sauvegardées (utile après un reset)
  ```bash
  python ingest.py --reindex-urls
  ```

- `--reset --reindex-urls` : Reset puis réindexe automatiquement les URLs sauvegardées
  ```bash
  python ingest.py --reset --reindex-urls
  ```

> ⚠️ **Attention** : L'option `--reset` supprime tous les documents déjà indexés. Les URLs indexées via l'interface web sont sauvegardées dans `vectorstore/indexed_urls.json` et peuvent être réindexées avec `--reindex-urls`.

### 2. Lancer l'interface web

```bash
python app.py
```

Ouvrez votre navigateur sur : http://localhost:5000

### 3. Utiliser le chat

Posez vos questions sur la documentation technique dans l'interface de chat. Le système va :
- Rechercher les passages pertinents dans vos documents
- Générer une réponse basée sur ces passages
- Afficher les sources utilisées

## 📁 Structure du projet

```
NewRag/
├── data/              # Documents à indexer
├── vectorstore/       # Vector store sauvegardé
├── templates/         # Templates HTML
│   └── chat.html      # Interface de chat
├── ingest.py          # Script d'indexation
├── app.py             # Application Flask
├── config.yaml        # Configuration
├── requirements.txt   # Dépendances Python
└── README.md          # Ce fichier
```

## ⚙️ Configuration

Modifiez `config.yaml` pour ajuster :
- Les chemins des dossiers
- La taille des chunks
- Le nombre de résultats à récupérer
- Les modèles Ollama utilisés
- Les paramètres de génération (température, etc.)

## 🔧 Technologies utilisées

- **LangChain** : Framework pour les applications LLM
- **LangChain Community** : Intégrations communautaires
- **LangChain Ollama** : Intégration avec Ollama
- **scikit-learn** : Vector store pour la recherche
- **Flask** : Framework web
- **Ollama** : Exécution locale de modèles LLM

## 📚 Formats de documents supportés

- PDF (`.pdf`)
- Texte (`.txt`)
- Markdown (`.md`)
- Word (`.docx`, `.doc`)

## 🐛 Dépannage

### Erreur "Vector store non trouvé"
Lancez d'abord `python ingest.py` pour indexer vos documents.

### Erreur "Ollama non accessible"
Assurez-vous qu'Ollama est en cours d'exécution :
```bash
ollama serve
```

### Erreur de modèle
Vérifiez que les modèles sont bien installés :
```bash
ollama list
```

## 📝 Notes

- Le vector store est sauvegardé dans `vectorstore/vectorstore.pkl`
- Pour réindexer après avoir ajouté des documents, relancez `python ingest.py`
- Les embeddings sont générés via Ollama, ce qui peut prendre du temps pour de gros volumes

