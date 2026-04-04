import os
from dotenv import load_dotenv

# LangChain & FAISS Imports
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS

# Python 3.14 Compatibility Imports
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def ask_ai_about_pdf(pdf_path, user_question):
    """
    Advanced RAG Engine:
    - Uses FAISS for high-speed vector search
    - Extracts Page Number Metadata for precise citations
    """
    
    # 1. Load the PDF (PyPDFLoader automatically captures page numbers)
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    # 2. Split into chunks while preserving metadata (page numbers)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    # 3. Create the Librarian (Vector Database)
    vectorstore = FAISS.from_documents(
        documents=splits, 
        embedding=OpenAIEmbeddings(api_key=os.getenv('OPEN_AI_API_KEY'))
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5}) # Look at top 5 chunks

    # 4. Fetch relevant chunks and MANUALLY build a cited context
    relevant_docs = retriever.invoke(user_question)
    context_with_metadata = ""
    
    for doc in relevant_docs:
        page_num = doc.metadata.get('page', 0) + 1  # Humans start counting at 1
        context_with_metadata += f"\n--- SOURCE: PAGE {page_num} ---\n{doc.page_content}\n"

    # 5. The Professional System Prompt
    system_prompt = (
        "You are an expert document analyzer. Use the provided context to answer the question. "
        "IMPORTANT: You must explicitly state which Page Number(s) the answer was found on. "
        "If the answer is not in the context, say 'I cannot find the answer in this document.'\n\n"
        "CONTEXT WITH PAGE NUMBERS:\n{context}"
    )
    
    # 6. Execute with ChatOpenAI
    llm = ChatOpenAI(
        api_key=os.getenv('OPEN_AI_API_KEY'), 
        model="gpt-3.5-turbo", 
        temperature=0
    )

    final_prompt = system_prompt.format(context=context_with_metadata)
    
    response = llm.invoke([
        ("system", final_prompt),
        ("human", user_question)
    ])

    return response.content
