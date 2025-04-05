visual-search-vlm :
This project implements a visual search system using OpenAI's CLIP model. It lets users input a natural language query (e.g., "a cat on a sofa") and retrieves the most relevant images from a dataset based on semantic similarity. A simple Streamlit app is included for easy interaction

🎨 Visual Search for Artwork using CLIP :
This project lets you search for artworks using simple text like:

> "a surreal painting with stars"  
> "an impressionist landscape with sunset"

It uses CLIP, a powerful AI model from OpenAI, to match your text with the most relevant images from your art dataset.
🔧 How to Run It:

1. Clone the project-
git clone https://github.com/Madhumitha-07/visual-search-vlm
cd visual-search-art

2. Install the required libraries-
pip install -r requirements.txt

3. Add your artwork images-
Put your .jpg or .png images inside the art_dataset/ folder.

4. Start the web app-
streamlit run app.py

🧠 How It Works :
The model converts both images and your text into numbers (embeddings).
It compares how similar your text is to each image.
It shows the top 5 most similar images

🖼️ Example Queries :
"a painting of a forest in autumn"
"a digital artwork of space"
"a colorful abstract composition"

🗂 Project Files :
File	Purpose
app.py      	    - The Streamlit web app
vlm_search.py	    - Code to search images using CLIP
art_dataset/	    - Folder with artwork images
requirements.txt	- List of libraries to install

✅ Requirements :
Python 3.7+
Libraries:
torch,
transformers,
streamlit,
Pillow,
tqdm

Install them with:
pip install -r requirements.txt

🙌 Credits :
CLIP by OpenAI
Hugging Face model: openai/clip-vit-base-patch32

📄 LICENSE :
MIT License
Copyright (c) 2025 [Madhumitha V]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.





