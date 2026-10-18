import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from PIL import Image

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing from .env")

client = genai.Client(api_key=api_key)

image_path = Path("input/original.jpg")

if not image_path.exists():
    raise FileNotFoundError("Input image not found!")

print("Analyzing image with Gemini AI...")

image = Image.open(image_path)

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        "Describe this image in detailed English for recreating it "
        "using an AI image generation model. Include the scenery, "
        "objects, colors, lighting, composition, and atmosphere. "
        "Return only the image description.",
        image,
    ],
)

description = response.text

if not description:
    raise ValueError("Gemini did not return a description.")

Path("description.txt").write_text(
    description, encoding="utf-8"
)

print("\nGenerated Image Description:\n")
print(description)
print("\nDescription saved to description.txt")