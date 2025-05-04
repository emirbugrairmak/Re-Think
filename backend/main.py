from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
from fastapi.middleware.cors import CORSMiddleware

# .env dosyasını yükle
load_dotenv()

# Gemini API anahtarını ayarla
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY bulunamadı. Lütfen .env dosyasında tanımlayın.")
genai.configure(api_key=GOOGLE_API_KEY)

# Mevcut modelleri listele
print("Mevcut modeller:")
for m in genai.list_models():
    print(f"- {m.name}")

app = FastAPI(title="Sürdürülebilirlik Chatbot")

# CORS ayarları
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Geliştirme için tüm originlere izin ver
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserMessage(BaseModel):
    message: str

class CircularEconomyResponse(BaseModel):
    reddet: str = Field(alias="Reddet")
    yeniden_dusun: str = Field(alias="Yeniden Düşün")
    azalt: str = Field(alias="Azalt")
    yeniden_kullan: str = Field(alias="Yeniden Kullanım")
    onar: str = Field(alias="Onar")
    yeniden_uret: str = Field(alias="Yeniden Üret")
    geri_donustur: str = Field(alias="Geri Dönüştür")
    geri_kazan: str = Field(alias="Geri Kazan")
    yeniden_tasarla: str = Field(alias="Yeniden Tasarla")
    bertaraf: str = Field(alias="Bertaraf")

    class Config:
        populate_by_name = True

def generate_circular_economy_response(user_message: str) -> CircularEconomyResponse:
    # Gemini API'yi kullanarak yanıt oluştur
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        prompt = f"""
        Kullanıcının sorusu: {user_message}
        
        Lütfen bu soruyu döngüsel ekonomi çerçevesinde değerlendir ve 9R ilkelerine göre yanıt ver.
        Her R için kısa ve yaratıcı bir öneri yaz. Yanıtı JSON formatında ver.
        
        Format:
        {{
            "Reddet": "Reddet önerisi",
            "Yeniden Düşün": "Yeniden düşün önerisi",
            "Azalt": "Azalt önerisi",
            "Yeniden Kullanım": "Yeniden kullanım önerisi",
            "Onar": "Onar önerisi",
            "Yeniden Üret": "Yeniden üret önerisi",
            "Geri Dönüştür": "Geri dönüştür önerisi",
            "Geri Kazan": "Geri kazan önerisi",
            "Yeniden Tasarla": "Yeniden tasarla önerisi",
            "Bertaraf": "Bertaraf önerisi"
        }}
        """
        
        print("Gemini API'ye istek gönderiliyor...")
        response = model.generate_content(prompt)
        print(f"Gemini API yanıtı: {response.text}")
        
        # Yanıtı JSON formatına dönüştür
        try:
            # Yanıttaki ```json işaretlerini temizle
            cleaned_response = response.text.replace('```json', '').replace('```', '').strip()
            response_json = json.loads(cleaned_response)
            return CircularEconomyResponse(**response_json)
        except json.JSONDecodeError as e:
            print(f"JSON dönüştürme hatası: {str(e)}")
            print(f"Temizlenmiş yanıt: {cleaned_response}")
            # Eğer JSON formatında değilse, önceden tanımlanmış bir yanıt döndür
            return CircularEconomyResponse(
                reddet="Ürünü satın almayı reddedin.",
                yeniden_dusun="Kullanım amacını yeniden düşünün.",
                azalt="Tüketimi azaltın.",
                yeniden_kullan="Ürünü farklı amaçlarla kullanın.",
                onar="Ürünü onarın.",
                yeniden_uret="Ürünü yeni bir şeye dönüştürün.",
                geri_donustur="Geri dönüşüme gönderin.",
                geri_kazan="Enerji geri kazanımı için kullanın.",
                yeniden_tasarla="Daha sürdürülebilir bir tasarım yapın.",
                bertaraf="Doğru şekilde bertaraf edin."
            )
    except Exception as e:
        print(f"Gemini API Hatası: {str(e)}")  # Hata detayını konsola yazdır
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat", response_model=CircularEconomyResponse)
async def chat(user_message: UserMessage):
    return generate_circular_economy_response(user_message.message)

@app.get("/")
async def root():
    return {"message": "Sürdürülebilirlik Chatbot API'sine Hoş Geldiniz!"} 