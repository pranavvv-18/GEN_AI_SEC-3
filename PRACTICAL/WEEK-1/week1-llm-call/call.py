import os
from dotenv import load_dotenv
import ollama

# Step 1: Load environment variables from .env
load_dotenv()

# Step 2: Read Ollama model from .env
model = os.getenv("OLLAMA_MODEL", "llama3.2")

print(f"Connecting to Ollama model '{model}'...")
try:
    # Step 3: Make LLM call using Ollama SDK
    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": "What is Artificial Intelligence? Explain in simple words.",
            }
        ],
    )

    # Step 4: Display response
    print("\nLLM Response:")
    print(response["message"]["content"])

except Exception as e:
    print(f"\nError: {e}")
    print("\nPlease verify:")
    print("1. Run 'ollama list' in your terminal to see your installed model name.")
    print("2. Ensure OLLAMA_MODEL in your .env matches your installed model name.")
