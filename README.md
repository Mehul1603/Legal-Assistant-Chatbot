# Legal Assistant Chatbot Using Retrieval-Augmented Generation (RAG)

# App link
https://legal-assistant-chatbot-gpqc2m5merpbkjqh2vbadp.streamlit.app/

## Overview  
This project is a **Legal Assistant Chatbot** that leverages **Retrieval-Augmented Generation (RAG)** to provide accurate and contextually relevant legal information. The chatbot integrates **natural language processing (NLP)** and **information retrieval systems** to make legal knowledge accessible to individuals, businesses, and researchers.  

---

## Key Features  
- **Legal Document Retrieval**: Retrieves relevant legal documents, case laws, and articles from public databases like [CaseMine](https://www.casemine.com/) and [Indian Kanoon](https://indiankanoon.org/).  
- **Context-Aware Responses**: Combines retrieved data with a large language model (LLM) to generate precise, easy-to-understand answers.  
- **User-Friendly Interface**: Offers an intuitive interface built using **Streamlit**, making it accessible to users with no technical background.  
- **Vector Database**: Uses **Pinecone** to store embedded representations of legal documents for efficient similarity-based retrieval.  
- **Document Embedding**: Employs **HuggingFace Embedding** models to convert legal texts into numerical vectors for search and matching.  

---

## Problems It Solves  
- **Legal Complexity**: Simplifies the understanding of dense legal jargon and documents.  
- **Accessibility Issues**: Bridges the gap for individuals and small businesses that lack access to professional legal services.  
- **Time-Consuming Research**: Reduces the effort and time required to find relevant legal information.  

---

## Target Audience  
1. **Individuals**: Seeking legal advice or assistance with drafting basic documents.  
2. **Small Businesses**: Requiring quick, affordable access to legal resources.  
3. **Students & Researchers**: Working on legal studies or case research.  

---

## System Architecture  
The chatbot uses the following architecture:  
1. **Vector Database**: Stores preprocessed legal documents as vectors.  
2. **Embedding Model**: Converts text data and queries into vector form using HuggingFace Embedding models.  
3. **Query Processing**: Processes user queries and retrieves similar vectors from the database.  
4. **RAG Framework**: Combines retrieved data with an LLM to generate responses.  
5. **Streamlit Interface**: Delivers the results to users in a simple, accessible format.

---

## How It Works  
1. **Data Gathering**: Collects legal texts from reliable public databases.  
2. **Data Embedding**: Preprocesses the data and embeds it into vectors using NLP techniques.  
3. **Query Handling**: User queries are converted into vectors and compared with the database to retrieve relevant information.  
4. **Response Generation**: The retrieved documents are synthesized by an LLM to generate an accurate, context-aware response.  

---

## Tools and Technologies  
- **Natural Language Processing**: HuggingFace Embedding models  
- **Vector Database**: Pinecone  
- **Interface**: Streamlit  
- **Data Sources**: Public legal databases like CaseMine and Indian Kanoon  

---

## Installation and Usage  

### Prerequisites  
- Python 3.8 or higher  
- Internet connection for accessing external resources and APIs  

### Steps to Run  
1. Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/legal-assistant-chatbot.git
   cd legal-assistant-chatbot



## Important Links

- https://indiankanoon.org/
- https://www.casemine.com/caseiq

- https://youtu.be/HkG06wBbTPM      Use combination of langchain, fast-embedding, reranking, **llama-parse** etc.
- https://youtu.be/L7Tm1h1AUcE      Web scraper to get data out of the above sites
- https://youtu.be/erUfLIi9OFM?list=PLZoTAELRMXVORE4VF7WQ_fAl0L1Gljtar      Code using the proper way by creating an environment, adding requirements.txt file, etc.

- https://docs.pinecone.io/integrations/langchain#1-set-up-your-environment     Pinecone with langchain docs
- https://youtu.be/p42BzKKAO74      Use groq with langchain + webscraping
