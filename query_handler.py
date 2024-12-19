from transformers import pipeline

# Initialize the generator pipeline once
generator = pipeline("text-generation", model="gpt2")

def handle_query(query, embedding_store, max_context_length=500, max_new_tokens=50):
    # Retrieve relevant chunks
    relevant_chunks = embedding_store.search(query)
    
    # Truncate context to avoid exceeding token limits
    context = ' '.join(relevant_chunks)[:max_context_length]
    
    # Construct the prompt
    prompt = f"Context: {context}\n\nUser Question: {query}"
    
    try:
        # Generate a response with explicit truncation and max_new_tokens
        response = generator(
            prompt,
            max_new_tokens=max_new_tokens,
            truncation=True,
            pad_token_id=50256  # Explicitly set pad_token_id to eos_token_id for GPT-2
        )
        return response[0]["generated_text"]
    except Exception as e:
        return f"Error generating response: {e}"
