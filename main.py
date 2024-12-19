from scraper import scrape_website
from embedding import EmbeddingStore
from query_handler import handle_query

def main():
    urls = ["https://www.uchicago.edu/",
            "https://www.washington.edu/",
            "https://www.stanford.edu/",
            "https://und.edu/"]  # Add target URLs here
    embedding_store = EmbeddingStore()
    
    for url in urls:
        print(f"Scraping {url}...")
        text = scrape_website(url)
        chunks = [text[i:i+500] for i in range(0, len(text), 500)]
        embedding_store.add_texts(chunks)
    
    print("Ready to handle queries!")
    while True:
        query = input("\nEnter your query (or 'exit' to quit): ")
        if query.lower() == "exit":
            break
        response = handle_query(query, embedding_store)
        print(f"\nResponse: {response}")

if __name__ == "__main__":
    main()
