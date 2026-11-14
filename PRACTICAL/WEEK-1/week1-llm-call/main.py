import os
from dotenv import load_dotenv
from openai import OpenAI

# Step 1: Load environment variables from .env
load_dotenv()

# Step 2: Read Ollama settings from .env
model = os.getenv("OLLAMA_MODEL", "llama3.2")
base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# Step 3: Initialize OpenAI client pointing to local Ollama endpoint
client = OpenAI(
    base_url=f"{base_url}/v1",
    api_key="ollama",  # Required by the OpenAI SDK, but ignored by Ollama
)

# Step 4: Send prompt to the model
print(f"Connecting to Ollama model '{model}' at {base_url}...")
try:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": "What is Artificial Intelligence? Explain in simple words.",
            }
        ],
    )

    # Step 5: Display the generated answer
    print("\nLLM Response:")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"\nError: {e}")
    print("\nPlease verify:")
    print("1. Run 'ollama list' in your terminal to see your installed model name.")
    print("2. Ensure OLLAMA_MODEL in your .env matches your installed model name.")
