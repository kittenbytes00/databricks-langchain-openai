import os
import time
import streamlit as st
from dotenv import load_dotenv
from databricks_langchain import DatabricksEmbeddings, DatabricksVectorSearch
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def nyc_taxi_search(query):
    load_dotenv()

    embeddings = DatabricksEmbeddings(
        endpoint="databricks-bge-large-en",
        databricks_host=os.environ["DATABRICKS_HOST"],
        databricks_token=os.environ["DATABRICKS_TOKEN"]
    )

    vector_store = DatabricksVectorSearch(
        index_name="demo.vector_demo.nyc_taxi_index",
        embedding=embeddings,
        text_column="content"
    )

    llm = ChatOpenAI(
        model="gpt-4",
        temperature=0.7
    )

    k = 5
    docs_and_scores = vector_store.similarity_search_with_score(query, k=k)

    docs = [doc for doc, score in docs_and_scores]

    print("\n=== Top Docs Retrieved ===")
    for i, (doc, score) in enumerate(docs_and_scores, 1):
        print(f"\nDoc {i}: {doc.page_content}")
        print(f"Cosine similarity: {score:.4f}")
        custom_message(message="⏳", wait=1)
        custom_message(
            message=f"\nEmbedding {i}: {doc.page_content}\n\nCosine similarity: {score:.4f}",
            wait=3)

    prompt_template = PromptTemplate(
        input_variables=["embedding_text", "question"],
        template="""You are an expert analyst with a sense of humour. Summarize the following documents:{embedding_text}
        Question: {question}
        Answer:
        Also add a funny quote about taxis and in New York City and try to tie it up with the question and use funny emojis
        Also do not use $ sign in your response and instead use USD or similar"""
    )

    parser = StrOutputParser()

    chain = prompt_template | llm | parser

    docs_text = "\n\n".join([doc.page_content for doc in docs])
    inputs = {
        "embedding_text": docs_text,
        "question": query
    }

    custom_message(message="Sending embeddings and query to GPT-4.", wait=3)
    custom_message(message="⏳", wait=1)
    custom_message(message="⏱️", wait=1)
    custom_message(message="👀", wait=2)

    answer = chain.invoke(inputs)

    custom_message(message="🙄", wait=2)
    custom_message(message="🤷", wait=2)
    custom_message(message="✅", wait=1)

    print("\n=== GPT-4 Answer ===")
    print(answer)
    return answer


def custom_message(message, wait):
    placeholder = st.empty()
    placeholder.info(message)
    time.sleep(wait)
    placeholder.empty()