\# Assignment 7: Image-to-Text-to-Image



\## Group Name

\*\*Cronus\*\*



\## Group Members

1\. K M Arafat Islam

2\. Rubina Akther

3\. Mahamud Galib Bin

4\. Zarin Anjum Prova



\## Project Description

This project demonstrates an Image-to-Text-to-Image workflow using artificial intelligence.



First, Google Gemini analyzes an original landscape image and generates a detailed English description. The description is then used as a prompt in Pollinations AI to generate a new image.



\## AI Models Used

\- \*\*Image-to-Text:\*\* Google Gemini 3.8 Flash

\- \*\*Text-to-Image:\*\* Z-Image Turbo (Pollinations AI)



\## Tools and Technologies

\- Python

\- Google Gemini API

\- Pollinations AI

\- Hugging Face (initially tested)

\- GitHub



\## Workflow

1\. Select an original landscape image.

2\. Analyze the image using Google Gemini.

3\. Save the generated description in `description.txt`.

4\. Use the description as a prompt in Pollinations AI.

5\. Generate and download the new image.

6\. Compare the original and generated images.



\## Project Files

\- `main.py` — Image analysis using Gemini AI

\- `requirements.txt` — Python dependencies

\- `input/original.jpg` — Original image

\- `description.txt` — Gemini-generated description

\- `output/generated.jpg` — Newly generated image



\## Results



\### Original Image

!\[Original Image](input/original.jpg)



\### AI-Generated Image

!\[Generated Image](output/generated.jpg)



\## Conclusion

We successfully completed an Image-to-Text-to-Image workflow using Google Gemini and Pollinations AI. The project demonstrates how an AI-generated image description can be used to create a new image.



\*\*Note:\*\* The image-generation step was completed through the Pollinations AI web interface. Hugging Face FLUX was tested but could not generate an image because the account had no remaining inference credits.

