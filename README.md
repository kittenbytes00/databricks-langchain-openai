# 🚕 RAG with Databricks, LangChain, OpenAI & Streamlit

### A Proof of Concept (POC) for a **Retrieval-Augmented Generation (RAG)** application using **Databricks Vector Search**, **LangChain**, **OpenAI (GPT-4)**, and **Streamlit**.

#### This project indexes **free and open-source New York Taxi data** in Databricks, retrieves relevant embeddings via Vector Search and uses an LLM to generate contextual answers based on user queries.

---

## 🧠 Architecture Overview

1. **Databricks**
   - Stores embeddings created from NYC Taxi open data
   - Provides similarity search over indexed data

2. **LangChain**
   - Connects to Databricks Vector Search
   - Handles retrieval and prompt orchestration

3. **OpenAI (GPT-4)**
   - Receives retrieved context + user query
   - Generates final response

4. **Streamlit**
   - User-facing web interface
   - Displays answers returned by the LLM

---

## 🧪 Project Type

**POC – Retrieval Augmented Generation (RAG)**  
Built using:
- Databricks
- LangChain
- OpenAI LLM (GPT-4)
- Streamlit

---

## 📂 Project Structure

```text
.
├── my_app.py                         # Streamlit application
|── vector_search_helper.py           # helper functions
├── databricks_nyc_indexing_script.py # Databricks indexing script
├── .env                              # Environment variables
├── requirements.txt
└── README.md
````

---

## ⚙️ Prerequisites

* Databricks workspace (Free Edition)
* Databricks Vector Search enabled
* OpenAI API key
* Python 3.9+
* Streamlit
* LangChain

---

## 🚀 Setup Instructions

### STEP 1: Create Vector Search Endpoint in Databricks

1. Go to **Databricks Workspace**

2. Navigate to:

   ```
   Compute --> Vector Search --> Create Endpoint
   ```

3. Create an endpoint with the following details:

   * **Name:** `vs_index`

4. Wait until the endpoint status becomes **ONLINE**

---

### STEP 2: Create the Vector Index

1. Open Databricks workspace
2. Create a new notebook
3. Choose:

   * **Language:** Python
4. Run the script:

   ```
   databricks_nyc_indexing_script.py
   ```

✅ This script:

* Loads free open-source NYC Taxi data
* Generates embeddings
* Creates and populates a Vector Search index
* Is compatible with **Databricks Free Edition**

---

### STEP 3: Update Environment Variables

Create or update the `.env` file with the required secrets and configuration.

Example:

```env
OPENAI_API_KEY=your_openai_api_key
DATABRICKS_HOST=https://<your-databricks-workspace>
DATABRICKS_TOKEN=your_databricks_token
```

> ⚠️ Make sure `.env` is **not committed** to version control.

---

### STEP 4: Run the Application

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run ./my_app.py
```

---

## 🧩 How It Works

1. User submits a query via Streamlit UI
2. LangChain sends the query to **Databricks Vector Search**
3. Relevant embeddings are retrieved from the NYC Taxi index
4. Retrieved context + user query is sent to **OpenAI GPT-4**
5. LLM generates a response grounded in retrieved data
6. Answer is displayed back to the user

---

## 📌 Use Case Examples

* Analyze NYC Taxi trip patterns
* Ask questions about fares, locations, and trends
* Natural language querying over structured datasets

---

## 🔒 Notes

* This is a **POC** and not production-hardened
* Error handling and security can be extended
* Designed for experimentation and learning

---

## 📄 License

This project uses **open-source NYC Taxi data**
Use responsibly and comply with data usage policies.

---

## ✨ Acknowledgements

* Databricks Vector Search
* LangChain
* OpenAI
* Streamlit