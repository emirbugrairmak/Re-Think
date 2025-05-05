# Re-Think Frontend

Re-Think, döngüsel ekonomi prensiplerine dayalı bir chatbot uygulamasının frontend kısmıdır. Bu uygulama, kullanıcıların sürdürülebilirlik ve çevre dostu yaşam konularında bilgi almasını sağlar.

## Özellikler

- Modern ve kullanıcı dostu arayüz
- Döngüsel ekonominin 9R ilkelerine göre yanıtlar
- Responsive tasarım
- Gerçek zamanlı chatbot etkileşimi

## Teknolojiler

- HTML5
- CSS3
- JavaScript (Vanilla)
- FastAPI (Backend ile iletişim)

## Kurulum

1. Projeyi klonlayın:
```bash
git clone [repo-url]
```

2. Frontend klasörüne gidin:
```bash
cd frontend
```

3. Basit bir HTTP sunucusu başlatın:
```bash
python3 -m http.server 3000
```

4. Tarayıcınızda `http://localhost:3000` adresine gidin.

## Backend Bağlantısı

Frontend, `http://localhost:8000` adresinde çalışan backend API'si ile iletişim kurar. Backend'in çalışır durumda olduğundan emin olun.

## Kullanım

1. Ana sayfada bulunan metin kutusuna sorunuzu yazın
2. "Gönder" butonuna tıklayın
3. Chatbot, sorunuzu döngüsel ekonomi prensiplerine göre değerlendirip yanıt verecektir

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