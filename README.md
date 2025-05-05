# Re-Think: Döngüsel Ekonomi Chatbotu

Re-Think, döngüsel ekonomi prensiplerine dayalı bir chatbot uygulamasıdır. Kullanıcıların sürdürülebilirlik ve çevre dostu yaşam konularında bilgi almasını sağlayan bu uygulama, Google'ın Gemini API'sini kullanarak akıllı yanıtlar üretir.

## Proje Yapısı

```
Re-Think/
├── frontend/           # Frontend uygulaması
│   ├── index.html     # Ana HTML dosyası
│   └── README.md      # Frontend dokümantasyonu
├── backend/           # Backend uygulaması
│   ├── main.py       # FastAPI uygulaması
│   └── README.md     # Backend dokümantasyonu
└── README.md         # Ana proje dokümantasyonu
```

## Özellikler

- Döngüsel ekonominin 9R ilkelerine göre yanıtlar
- Modern ve kullanıcı dostu arayüz
- Gerçek zamanlı chatbot etkileşimi
- Google Gemini API entegrasyonu

## Kurulum

### Gereksinimler

- Python 3.8+
- Google Gemini API anahtarı
- Modern bir web tarayıcısı

### Adımlar

1. Projeyi klonlayın:
```bash
git clone [repo-url]
```

2. Sanal ortam oluşturun ve aktifleştirin:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
.\venv\Scripts\activate  # Windows
```

3. Gerekli paketleri yükleyin:
```bash
pip install -r backend/requirements.txt
```

4. `.env` dosyası oluşturun ve Gemini API anahtarınızı ekleyin:
```
GOOGLE_API_KEY=your_api_key_here
```

5. Backend'i başlatın:
```bash
cd backend
uvicorn main:app --reload
```

6. Frontend'i başlatın:
```bash
cd frontend
python3 -m http.server 3000
```

7. Tarayıcınızda `http://localhost:3000` adresine gidin.

## 9R İlkeleri

Uygulama, döngüsel ekonominin 9R ilkelerine göre yanıtlar üretir:

1. Reddet (Refuse)
2. Yeniden Düşün (Rethink)
3. Azalt (Reduce)
4. Yeniden Kullanım (Reuse)
5. Onar (Repair)
6. Yeniden Üret (Remanufacture)
7. Geri Dönüştür (Recycle)
8. Geri Kazan (Recover)
9. Yeniden Tasarla (Redesign)

## Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Bir Pull Request oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## İletişim

Proje Sahibi - [@your_twitter](https://twitter.com/your_twitter)

Proje Linki: [https://github.com/yourusername/re-think](https://github.com/yourusername/re-think) 