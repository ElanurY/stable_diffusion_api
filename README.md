# Stable Diffusion API

Bu proje, Python kullanarak **Stable Diffusion** modeli ile resim üretmek için bir API sunar.

## Özellikler
- Metinden görüntü oluşturma
- Üretilen görselleri kaydetme
- API istemcisi ile kolay kullanım

## Kurulum
```bash
git clone https://github.com/ElanurY/stable_diffusion_api.git
cd stable_diffusion_api
pip install -r requirements.txt-
## Kullanım
uvicorn main:app --reload
