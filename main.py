from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from diffusers import StableDiffusionPipeline
from fastapi.responses import JSONResponse
from io import BytesIO
import torch
import base64
import os
from datetime import datetime

# Uygulama
app = FastAPI()

# Görselleri saklayacağımız klasör
SAVE_DIR = "generated_images"
os.makedirs(SAVE_DIR, exist_ok=True)

print("Model yükleniyor... (CPU, düşük RAM modu)")
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    torch_dtype=torch.float32
)
pipe.to("cpu")
print("Model yüklendi!")

# İstek modeli
class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "Yeni sistem çalışıyor!"}

@app.post("/generate")
def generate(req: PromptRequest):
    if not req.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt alanı boş olamaz.")

    # Görsel üret
    image = pipe(req.prompt).images[0]

    # Klasöre kaydetme
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(SAVE_DIR, f"{timestamp}.png")
    image.save(file_path)

    # Base64 encode
    img_bytes = BytesIO()
    image.save(img_bytes, format="PNG")
    img_bytes.seek(0)
    img_base64 = base64.b64encode(img_bytes.read()).decode("utf-8")

    # JSON olarak döndür
    return JSONResponse(content={
        "status": "success",
        "prompt": req.prompt,
        "file_path": file_path,
        "image_base64": img_base64
    })
