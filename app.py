import os
import streamlit as st
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering.chain import load_qa_chain

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def getPDFText(pdfDocs):
    text = ""
    for pdf in pdfDocs:
        pdf_Reader = PdfReader(pdf)
        for page in pdf_Reader.pages:
            text += page.extract_text()
    return text



def getTextChunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_text(text)
    return chunks



def getVectorStore(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model='models/text-embedding-004')
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")



def getConversationalChain():
    prompt_template = """
    In your response, please be as specific as you can given the context that has been supplied. 
    If the answer is not there, simply state that "answer is not available in the context"; 
    do not give an incorrect response.\n\n
    Context:\n {context}\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model='gemini-pro', temperature=0.2)
    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(llm=model, chain_type="stuff", prompt=prompt)

    return chain



def userInput(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    
    new_db = FAISS.load_local(folder_path="faiss_index", embeddings=embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    chain = getConversationalChain()
    response = chain({"input_documents":docs, "question": user_question}, return_only_outputs=True)

    st.write("Answer: ", response["output_text"])



def main():
    st.set_page_config("PDFAssist")
    st.header("Chat with PDFs via PDFAssist 📃✍⚡")

    user_question = st.text_input("Ask your Queries from the PDF Files")

    if user_question:
        userInput(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = getPDFText(pdf_docs)
                text_chunks = getTextChunks(raw_text)
                getVectorStore(text_chunks)
                st.success("Done")


if __name__ == "__main__":
    main()