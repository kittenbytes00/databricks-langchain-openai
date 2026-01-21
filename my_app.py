import streamlit as st
from vector_search_helper import nyc_taxi_search, custom_message

st.title("New York Taxi Services")
question_input = st.text_input(label="question", placeholder="start typing ...")

do_search = st.button("Search")

if question_input:
    if do_search:
        custom_message(message="checking NYC taxi data...", wait=10)
        response = nyc_taxi_search(question_input)
        if response:
            st.markdown(response)


