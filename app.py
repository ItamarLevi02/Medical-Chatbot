from flask import Flask, render_template, jsonify, request
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import *
import chromadb
import os
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI





app = Flask(__name__)

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

print(api_key)

#Loading the index


PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain_type_kwargs = {"prompt": PROMPT}

persist_directory = 'db'
embedding = OpenAIEmbeddings()
vetordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)

retreiver = vetordb.as_retriever(search_kwargs={"k":2})


qa_chain = RetrievalQA.from_chain_type(llm = OpenAI(),
                                       chain_type="stuff",
                                       retriever=retreiver,
                                       chain_type_kwargs=chain_type_kwargs,
                                       return_source_documents=True)


@app.route("/")
def index():
    return render_template('chat.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa_chain({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)