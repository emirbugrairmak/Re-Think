# Sürdürülebilirlik Chatbot - Backend

Bu proje, sürdürülebilirlik temalı bir chatbot'un backend kısmını içerir. FastAPI kullanılarak geliştirilmiştir ve Google'ın Gemini API'sini kullanarak kullanıcı sorularına döngüsel ekonomi çerçevesinde yanıtlar üretir.

## Özellikler

- FastAPI tabanlı REST API
- Gemini API entegrasyonu
- 9R ilkelerine göre özelleştirilmiş yanıtlar
- CORS desteği

## Kurulum

1. Sanal ortam oluşturun:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# veya
.venv\Scripts\activate  # Windows
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

3. `.env` dosyasını oluşturun ve Gemini API anahtarınızı ekleyin:
```
GOOGLE_API_KEY=your_api_key_here
```

## Çalıştırma

```bash
uvicorn main:app --reload
```

API `http://localhost:8000` adresinde çalışacaktır.

## API Endpoint'leri

- `POST /chat`: Kullanıcı mesajını alır ve 9R ilkelerine göre yanıt döndürür
- `GET /`: API'nin çalıştığını doğrulamak için basit bir yanıt döndürür

## Frontend Entegrasyonu

Frontend uygulaması `http://localhost:8000/chat` endpoint'ine POST istekleri gönderebilir. CORS ayarları tüm originlere izin verecek şekilde yapılandırılmıştır. 