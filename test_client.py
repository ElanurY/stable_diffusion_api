import requests
import base64
import os
import webbrowser
from datetime import datetime

# API endpoint URL
url = "http://127.0.0.1:8001/generate"

while True:
    prompt = input("\n🎨 Prompt gir (çıkmak için 'q' yaz): ")
    if prompt.lower() == "q":
        print("🚪 Çıkılıyor...")
        break

    # Görsel adı iste
    custom_name = input("💾 Görsel adı (boş bırakılırsa otomatik verilir): ").strip()

    # Boş ise otomatik isim oluştur
    if custom_name == "":
        custom_name = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Dosya uzantısını ekle
    filename = f"{custom_name}.png"
    save_dir = "generated_images"
    file_path = os.path.join(save_dir, filename)

    payload = {"prompt": prompt}
    print("⏳ Görsel üretiliyor...")

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()

        data = response.json()

        # Görseli base64'ten çöz
        img_data = base64.b64decode(data["image_base64"])

        # Kaydet
        os.makedirs(save_dir, exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(img_data)

        print(f"✅ Görsel kaydedildi: {file_path}")

        # Otomatik aç
        webbrowser.open(file_path)

    except Exception as e:
        print("❌ Hata:", e)
