# databricks-langchain-openai
#### A POC for a RAG project with Databricks, Langchain, OpenAI(LLM) and Streamlit

### STEP 1 : Create endpoint in Databricks

- Compute --> Vector Search --> Create Endpoint
- Name: vs_index
- Wait till it is Online


### STEP 2 :  - Create index

- run script databricks_nyc_indexing_script in Databricks
- script is compatible with free edition
- ensure you chose language as Python


### STEP 3 : Update .env file

- update .env file with correct secrets and links


### STEP 4 : Run project
 - cmd : streamlit run ./my_app.py