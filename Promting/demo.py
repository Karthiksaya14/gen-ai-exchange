import os
from google import genai
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Get API key from .env
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

MODEL_ID = "gemini-2.0-flash"
prompt = "Suggest a name for a flower shop that sells bouquets of dried flowers"

response = client.models.generate_content(model=MODEL_ID, contents=prompt)

print(response.text)
