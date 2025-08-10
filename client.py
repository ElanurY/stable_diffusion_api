import requests

prompt = "a cute cat wearing sunglasses"
response = requests.post(
    "http://127.0.0.1:8000/generate",
    json={"prompt": prompt}
)

if response.status_code == 200:
    with open("output.png", "wb") as f:
        f.write(response.content)
    print("✅ Görsel kaydedildi: output.png")
else:
    print("❌ Hata:", response.text)
