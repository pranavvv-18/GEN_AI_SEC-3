# main.py
import os
from dotenv import load_dotenv
from llm_client import (
    GeminiProvider,
    OllamaProvider,
    LLMClient
)
from mongo_logger import MongoLogger

# Load environment variables
load_dotenv(override=True)

print("================================")
print("       WEEK 3: LLM MONITORING")
print("================================")
print("1. Gemini")
print("2. Ollama")

choice = input("\nSelect provider (1/2): ").strip()

logger = None
try:
    # Connect to MongoDB
    logger = MongoLogger()

    # Select AI provider
    if choice == "1":
        api_key = os.getenv("GEMINI_API_KEY")
        model = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
        if not api_key:
            raise ValueError("Gemini API key not found in .env")
        provider = GeminiProvider(api_key, model)
    elif choice == "2":
        model = os.getenv("OLLAMA_MODEL", "llama3.2")
        provider = OllamaProvider(model)
    else:
        raise ValueError("Invalid selection. Choose 1 or 2.")

    # Create common client
    client = LLMClient(provider, logger)

    # Get user prompt
    prompt = input("\nEnter your question: ")

    # Generate response
    answer = client.generate(prompt)

    print("\n========== AI RESPONSE ==========")
    print(answer)
    print("\n========== COMPLETED ==========")

except Exception as error:
    print("\nApplication error:", error)

finally:
    if logger is not None:
        logger.close()

