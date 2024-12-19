# chat-with-website
Overview
This project implements a Retrieval-Augmented Generation (RAG) pipeline that allows users to chat with website content. The system crawls, scrapes, and processes website data, converts the content into embeddings, and stores them in a vector database for efficient retrieval. When a user asks a question, the system retrieves relevant information and generates context-rich responses using a language model from Hugging Face.

Features

Data Ingestion:
Crawls and scrapes content from websites.
Converts content into embeddings using a pre-trained model.
Stores embeddings in a vector database (e.g., FAISS).

Query Handling:
Accepts natural language queries.
Retrieves relevant chunks from the vector database.
Generates accurate responses based on retrieved content.

Response Generation:
Uses Hugging Face's transformers library to generate responses.
Ensures context-rich and factual replies.

How to Use
Add Target URLs:
In main.py, specify the list of URLs you want to scrape:
urls = ["https://example.com", "https://another-example.com"]
Query the System:
After running main.py, enter your questions when prompted:
Enter your query: What is the main service provided by the website?
Sample Output:


Handling Errors:
If you encounter a 403 Forbidden error, try changing the user-agent string in scraper.py:
headers = {"User-Agent": "Mozilla/5.0"}
<img width="953" alt="s2" src="https://github.com/user-attachments/assets/05e63668-12e3-4eac-bb68-de1e4ca12ffb" />


License
This project is licensed under the MIT License.

