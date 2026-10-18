import os
from pathlib import Path
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

hf_token = os.getenv("HF_TOKEN")

if not hf_token:
    raise ValueError("HF_TOKEN is missing from .env")

description_file = Path("description.txt")

if not description_file.exists():
    raise FileNotFoundError("description.txt not found")

prompt = description_file.read_text(encoding="utf-8")

output_folder = Path("output")
output_folder.mkdir(exist_ok=True)

print("Generating new image using FLUX AI...")
print("Please wait...")

client = InferenceClient(
    provider="auto",
    api_key=hf_token
)

image = client.text_to_image(
    prompt=prompt,
    model="black-forest-labs/FLUX.1-schnell",
    width=1024,
    height=1024
)

output_path = output_folder / "generated.jpg"
image.convert("RGB").save(output_path)

print("Image generated successfully!")
print(f"Saved to: {output_path}")