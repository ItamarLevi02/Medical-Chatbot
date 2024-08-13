from src.helper import load_pdf, text_split
from dotenv import load_dotenv
import os
import chromadb
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI


load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

extracted_data=load_pdf("data/")
text_chunks = text_split(extracted_data)

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_collection")


text_chunks = text_split(extracted_data)

persist_directory = 'db'
embedding = OpenAIEmbeddings()
vetordb = Chroma.from_documents(documents = text_chunks,
                                embedding=embedding,
                                persist_directory=persist_directory)

vetordb.persist()
vectordb=None
