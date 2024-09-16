from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from pinecone import Pinecone, ServerlessSpec
import os

# Choose embeddings
embeddings = HuggingFaceEmbeddings()

# Vector Search DB in Pinecone
api_key = os.getenv("PINECONE_API_KEY")
os.environ['PINECONE_API_KEY'] = api_key
index_name = "langchainvector"
vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)

def add_docs(path, text=True):
    if text:
        loader = TextLoader(path)
    else:
        loader = DirectoryLoader(path, glob="./*.pdf", loader_cls=PyPDFLoader)
    
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1024, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)

    vectorstore.add_documents(docs)

def similsearch(query, k=1):
    return vectorstore.similarity_search(query, k)

if __name__ == '__main__':
    # Loading the pdf docs
    loader = DirectoryLoader('raw_data', glob="./*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()

    # Splitting the text
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)
    
    # Embedding and Uploading to pinecone
    vectorstore_from_docs = PineconeVectorStore.from_documents(
        texts,
        index_name=index_name,
        embedding=embeddings
    )
