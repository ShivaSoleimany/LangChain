# **An LLM-Powered RAG for News Retrieval 📈**  

![LangChain](https://img.shields.io/badge/LangChain-RAG-green)  
![FAISS](https://img.shields.io/badge/Vector%20Database-FAISS-yellow)  
![OpenAI](https://img.shields.io/badge/LLM-GPT-orange)  

**Retrieval-Augmented Generation (RAG) system** that fetches real-time news articles, processes them using a **vector database**, and generates AI-driven answers using **LLMs (GPT/OpenAI/Hugging Face)**.  

🔹 **Fetches real-time news** from the web via SerpAPI.  
🔹 **Processes & stores articles** in a vector database for efficient retrieval.  
🔹 **Uses an LLM** to generate context-aware answers.  

---

## **🚀 Features**
✅ **Retrieves real-time news** via web search (SerpAPI).  
✅ **Extracts & chunks text** from web articles.  
✅ **Embeds & stores documents** in a **vector database** (FAISS).  
✅ **Performs semantic search** to find relevant news snippets.  
✅ **Augments LLM responses** with retrieved documents.  
✅ **User-friendly Streamlit UI** for easy interaction.  

---

## **🛠️ Installation**
### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/ShivaSoleimany/LangChain.git
```

### **2️⃣ Install Dependencies**
Ensure you have Python 3.8+ installed, then run:

```bash
pip install -r requirements.txt
```

### **3️⃣ Set Up API Keys**
You need OpenAI, HUGGINGFACE_API_KEY, and SerpAPI keys to use this project.
Create a .env file in the root directory:

```bash
touch .env
```

Add your API keys:
```bash
OPENAI_API_KEY=your_openai_api_key
SERPAPI_KEY=your_serpapi_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key
```

## **🖥️ Usage**

### **1️⃣ Start the Streamlit App**
```bash
streamlit run src/app/main.py
```

This will launch the UI, where you can input questions and receive AI-generated answers.


### **🔍 Project Structure**
```bash
rockybot-rag/
│── src/
│   ├── app/
│   │   ├── main.py              # Streamlit UI
│   │   ├── get_answer.py        # LLM inference pipeline
│   │   ├── llm.py               # LLM initialization
│   ├── scripts/
│   │   ├── search.py            # Fetches real-time news via SerpAPI
│   │   ├── url_loader.py        # Scrapes & extracts text from articles
│   │   ├── chunker.py           # Splits documents into text chunks
│   │   ├── vectorstore.py       # FAISS vector store (stores & retrieves docs)
│── data/                        # FAISS index storage
│── .env                         # API keys
│── requirements.txt             # Dependencies
│── README.md                    # Documentation
```

### **🛠️ How It Works**

#### 🔹 Step 1: Retrieve Relevant News
The system uses SerpAPI or DuckDuckGo to find the url of real-time articles matching the query.

#### 🔹 Step 2: Extract & Process the Content
The system scrapes articles and extracts readable text.
Text is split into smaller chunks for embedding.

#### 🔹 Step 3: Store & Retrieve from Vector Database
Chunks are embedded using OpenAI or Hugging Face embeddings.
FAISS indexes the embedded vectors for fast retrieval.
A semantic search finds the most relevant passages.

#### 🔹 Step 4: Generate Context-Aware Answers
The LLM uses retrieved passages to generate a concise, AI-driven answer.
Sources are displayed alongside the answer for verification.

<!-- 📌 Sources:
1️⃣ TechCrunch - AI Breakthroughs
2️⃣ OpenAI Blog - GPT-4 Updates

📌 Future Improvements
🔹 Support for more LLMs (Claude, Gemini, Mistral).
🔹 Multilingual support for broader news retrieval.
🔹 Caching to reduce API costs and speed up retrieval.
🔹 Better ranking of retrieved documents for improved accuracy. -->

## **🛠️ Technologies Used**
🚀 LLMs: OpenAI GPT-4, Hugging Face
📊 Vector Database: FAISS
🌐 Web Search: SerpAPI, DuckDuckGO
🔍 Semantic Search: Embeddings-based retrieval
💻 Frameworks: LangChain, Streamlit
📜 Text Processing: BeautifulSoup, Recursive Text Splitter

## **📩 Contact & Contribution**
🚀 Want to contribute? Open a PR!
💡 Found an issue? Report it under GitHub Issues.

📧 Contact: shiva.soleimany.dzch@gmail.com