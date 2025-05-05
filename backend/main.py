from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import google.generativeai as genai
import os
from dotenv import load_dotenv
import json

# .env dosyasını yükle
load_dotenv()

# Gemini API anahtarını al
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

# Gemini API'yi yapılandır
genai.configure(api_key=GOOGLE_API_KEY)

app = FastAPI()

# CORS ayarları
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend'in çalıştığı adres
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

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # Modeli oluştur
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        # 9R ilkelerine göre yanıt vermesi için prompt oluştur
        prompt = f"""
        Kullanıcının sorusu: {request.message}
        
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
        
        # Kullanıcı mesajını al ve Gemini'ye gönder
        response = model.generate_content(prompt)
        return {"response": response.text}
    except Exception as e:
        print(f"Error: {str(e)}")  # Hata detayını konsola yazdır
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Döngüsel Ekonomi Chatbot API'sine Hoş Geldiniz!"} 