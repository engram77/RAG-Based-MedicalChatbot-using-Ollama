from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_ollama import ChatOllama
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os


app = Flask(__name__)


load_dotenv()

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')


os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY



embeddings = download_hugging_face_embeddings()

index_name = "medical-chatbot" 
# Embed each chunk and upsert the embeddings into your Pinecone index.
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)




retriever = docsearch.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 8, "fetch_k": 20}
)

chatModel = ChatOllama(model="llama3.2")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(chatModel, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)



@app.route("/")
def index():
    return render_template('chat.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"].strip()
    lower_msg = msg.lower()

    # formatting / test / casual instructions
    simple_commands = [
        "type something in bold",
        "write something in bold",
        "say something in bold"
    ]

    if lower_msg in simple_commands:
        return "**This should appear in bold**"

    # fallback to RAG for actual medical questions
    response = rag_chain.invoke({"input": msg})
    answer = str(response["answer"])

    # remove markdown bold markers
    answer = answer.replace("**", "")

    # append doctor consultation note when fallback text appears
    if "I could not find specific information" in answer and "Kindly consult a Doctor for it." not in answer:
        answer += "\nKindly consult a Doctor for it."

    return answer

if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)
