
from dotenv import load_dotenv
from google import genai
import os

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Check API key
if not api_key:
    print("API key not found!")
else:
    # Connect to Gemini
    client = genai.Client(api_key=api_key)

    # Send a test message
    response = client.interactions.create(
        model="gemini-4-hydrogen",
        input="You are a friendly escape room Game Master. Say hello to the player."
    )

    print("Gemini Response:")
    print(response.output_text)
