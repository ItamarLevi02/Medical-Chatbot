import chromadb
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.embeddings import OpenAIEmbeddings
import os
from dotenv import load_dotenv
from langchain.vectorstores import Chroma


load_dotenv()
api_key = os.getenv('PINECONE_API_KEY')


chroma_client = chromadb.Client()

#Extract PDF Data
def load_pdf(data):
    loader = DirectoryLoader(data,
                    glob='*.pdf',
                    loader_cls=PyPDFLoader)
    documents = loader.load()

    return documents

# Crreate Text Split
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 20)
    text_chunks = text_splitter.split_documents(extracted_data)

    return text_chunks

