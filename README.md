# Sürdürülebilirlik Chatbot API

Bu proje, döngüsel ekonomi ilkelerine göre yanıt veren bir chatbot API'sidir. FastAPI kullanılarak geliştirilmiştir ve Google'ın Gemini API'sini kullanmaktadır.

## Kurulum

1. Projeyi klonlayın:
```bash
git clone [repo-url]
cd [repo-name]
```

2. Sanal ortam oluşturun ve aktifleştirin:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# veya
.venv\Scripts\activate  # Windows
```

3. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

4. `.env` dosyasını oluşturun ve Gemini API anahtarınızı ekleyin:
```
GOOGLE_API_KEY=your_api_key_here
```

## Kullanım

1. API'yi başlatın:
```bash
uvicorn main:app --reload
```

2. API'ye erişin:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoint'leri

- `POST /chat`: Kullanıcı mesajını alır ve 9R ilkelerine göre yanıt verir
- `GET /`: API hakkında bilgi verir

## Örnek Kullanım

```python
import requests

response = requests.post(
    "http://localhost:8000/chat",
    json={"message": "Eski tişörtlerimi nasıl değerlendirebilirim?"}
)

print(response.json())
```

## 9R İlkeleri

- R0: Reddet
- R1: Yeniden düşün
- R2: Azalt
- R3: Yeniden kullanım
- R4: Onar
- R5: Yeniden üret
- R6: Geri dönüştür
- R7: Geri kazan
- R8: Yeniden tasarla
- R9: Bertaraf 