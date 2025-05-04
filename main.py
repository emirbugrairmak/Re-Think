from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
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
    R0: str
    R1: str
    R2: str
    R3: str
    R4: str
    R5: str
    R6: str
    R7: str
    R8: str
    R9: str

def generate_circular_economy_response(user_message: str) -> CircularEconomyResponse:
    # Basit anahtar kelime kontrolü
    if "tişört" in user_message.lower():
        return CircularEconomyResponse(
            R0="Eski tişörtleri satın almayı reddedin, ikinci el mağazaları tercih edin.",
            R1="Tişörtlerinizi nasıl daha uzun süre kullanabileceğinizi düşünün.",
            R2="Yeni tişört alımını azaltın, kaliteli ve dayanıklı ürünler seçin.",
            R3="Eski tişörtlerinizi ev temizliği için bez olarak kullanın.",
            R4="Yırtık tişörtlerinizi onarın veya dikiş kurslarına katılın.",
            R5="Eski tişörtlerinizi yeni aksesuarlara dönüştürün.",
            R6="Kullanılamayacak durumdaki tişörtleri geri dönüşüme gönderin.",
            R7="Eski tişörtlerin kumaşını yeni projelerde kullanın.",
            R8="Modüler ve tamir edilebilir tişörtler tasarlayın.",
            R9="Son çare olarak, doğru şekilde bertaraf edin."
        )
    elif "plastik" in user_message.lower():
        return CircularEconomyResponse(
            R0="Tek kullanımlık plastik ürünleri reddedin.",
            R1="Plastik kullanımınızı gözden geçirin ve alternatifleri düşünün.",
            R2="Plastik tüketiminizi azaltın, yeniden kullanılabilir ürünler tercih edin.",
            R3="Plastik kapları tekrar tekrar kullanın.",
            R4="Kırık plastik eşyaları onarın.",
            R5="Eski plastikleri yeni ürünlere dönüştürün.",
            R6="Plastikleri geri dönüşüm kutularına atın.",
            R7="Plastik atıkları enerji üretiminde kullanın.",
            R8="Biyobozunur alternatifler tasarlayın.",
            R9="Plastikleri doğru şekilde bertaraf edin."
        )
    elif "kavanoz" in user_message.lower():
        return CircularEconomyResponse(
            R0="Yeni kavanoz satın almayı reddedin.",
            R1="Kavanozların farklı kullanım alanlarını düşünün.",
            R2="Kavanoz tüketiminizi azaltın.",
            R3="Kavanozları saklama kapları olarak kullanın.",
            R4="Kırık kavanozları onarın veya yeniden kullanın.",
            R5="Kavanozları dekoratif eşyalara dönüştürün.",
            R6="Kavanozları cam geri dönüşümüne gönderin.",
            R7="Kavanozları yeni ürünlerde kullanın.",
            R8="Modüler ve çok amaçlı kavanozlar tasarlayın.",
            R9="Kavanozları doğru şekilde bertaraf edin."
        )
    else:
        # Gemini API'yi kullanarak yanıt oluştur
        try:
            model = genai.GenerativeModel('gemini-2.0-flash')
            prompt = f"""
            Kullanıcının sorusu: {user_message}
            
            Lütfen bu soruyu döngüsel ekonomi çerçevesinde değerlendir ve 9R ilkelerine göre yanıt ver.
            Her R için kısa ve yaratıcı bir öneri yaz. Yanıtı JSON formatında ver.
            
            Format:
            {{
                "R0": "Reddet önerisi",
                "R1": "Yeniden düşün önerisi",
                "R2": "Azalt önerisi",
                "R3": "Yeniden kullanım önerisi",
                "R4": "Onar önerisi",
                "R5": "Yeniden üret önerisi",
                "R6": "Geri dönüştür önerisi",
                "R7": "Geri kazan önerisi",
                "R8": "Yeniden tasarla önerisi",
                "R9": "Bertaraf önerisi"
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
                    R0="Ürünü satın almayı reddedin.",
                    R1="Kullanım amacını yeniden düşünün.",
                    R2="Tüketimi azaltın.",
                    R3="Ürünü farklı amaçlarla kullanın.",
                    R4="Ürünü onarın.",
                    R5="Ürünü yeni bir şeye dönüştürün.",
                    R6="Geri dönüşüme gönderin.",
                    R7="Enerji geri kazanımı için kullanın.",
                    R8="Daha sürdürülebilir bir tasarım yapın.",
                    R9="Doğru şekilde bertaraf edin."
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