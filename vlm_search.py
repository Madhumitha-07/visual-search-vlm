import os
from PIL import Image
import torch
from transformers import CLIPProcessor, CLIPModel
from tqdm import tqdm

class VLMSearch:
    def __init__(self, dataset_path="image_dataset"):
        self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
        self.dataset_path = dataset_path
        self.image_files = [os.path.join(dataset_path, f) for f in os.listdir(dataset_path) if f.endswith((".jpg", ".png"))]
        self.image_embeddings = []
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)

    def preprocess_images(self):
        images = [Image.open(img_path).convert("RGB") for img_path in self.image_files]
        return images

    def encode_images(self):
        images = self.preprocess_images()
        for img in tqdm(images, desc="Encoding images"):
            inputs = self.processor(images=img, return_tensors="pt").to(self.device)
            with torch.no_grad():
                embedding = self.model.get_image_features(**inputs)
            self.image_embeddings.append(embedding.squeeze(0))
        self.image_embeddings = torch.stack(self.image_embeddings)

    def search(self, query, top_k=5):
        inputs = self.processor(text=query, return_tensors="pt", padding=True).to(self.device)
        with torch.no_grad():
            text_embedding = self.model.get_text_features(**inputs)
        similarities = torch.nn.functional.cosine_similarity(text_embedding, self.image_embeddings)
        top_indices = similarities.topk(top_k).indices
        results = [self.image_files[i] for i in top_indices]
        return results
