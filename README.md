# YZ50 - 1. Hafta: Yapay Sinir Ağları Temelleri ve Gradient Descent

Bu depo, **YZ50** programı 1. Hafta ödevi kapsamında hazırlanmıştır. Çalışmada, derin öğrenmenin ve yapay sinir ağlarının temel yapı taşları hiçbir dış kütüphane (PyTorch, TensorFlow vb.) kullanılmadan, **saf Python** ile sıfırdan inşa edilmiştir.

---

## 📌 Görev Özeti ve İçerik

1. **Tek Nöron Forward Pass (Fonksiyonel & OOP):**
   - $z = \sum_{i} (w_i \cdot x_i) + b$ formülü saf Python döngüleri ve `Neuron` sınıfı ile uygulanmıştır.
2. **Katman (Layer) Forward Pass:**
   - Birden fazla nöronun aynı girdileri işlediği katman yapısı `Layer` sınıfı ile modellenmiştir.
3. **Kayıp Fonksiyonu (MSE - Mean Squared Error):**
   - Hem tek nöron hem de çoklu nöron çıktıları için Ortalama Kare Hata ($L = \frac{1}{N}\sum (y_{pred} - y_{true})^2$) hesaplanmıştır.
4. **Manuel Parametre Değişimi & Loss Landscape:**
   - $w_1$ ağırlığı belirli bir aralıkta değiştirilerek kayıp değerleri hesaplanmış ve `matplotlib` ile Loss Eğrisi çizilmiştir.
5. **Sayısal Türev & Gradient Descent:**
   - Andrej Karpathy'nin 1. videosunda anlatılan Sayısal Türev (Numerical Derivative: $\frac{f(x+h) - f(x)}{h}$) yöntemiyle gradyanlar hesaplanmış ($h = 10^{-5}$).
   - Parametreler gradyanın tersi yönünde güncellenerek ($p \leftarrow p - \eta \cdot \frac{\partial L}{\partial p}$) otomatik öğrenme döngüsü tamamlanmıştır.

---

## 📁 Proje Yapısı

```text
YZ50-WEEK1/
├── yz50_hafta1_odev.ipynb   # Ana Ödev Jupyter Notebook Dosyası
├── create_notebook.py       # Notebook oluşturucu yardımcı betik
├── .gitignore               # Gereksiz dosyaları hariç tutma yapılandırması
└── README.md                # Proje dokümantasyonu
```

---

## 🚀 Çalıştırma Talimatları

1. **Depoyu Klonlayın:**
   ```bash
   git clone <repo-url>
   cd YZ50-WEEK1
   ```

2. **Sanal Ortamı Aktifleştirin ve Bağımlılıkları Yükleyin:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install matplotlib jupyter
   ```

3. **Jupyter Notebook'u Başlatın:**
   ```bash
   jupyter notebook yz50_hafta1_odev.ipynb
   ```

---

## 📹 Video Sunumu & Kavramlar

Videoda ele alınan temel başlıklar:
- Forward pass mantığı ve nöron/katman matematiği.
- Loss fonksiyonu ve parametre değişimiyle Loss Landscape ilişkisi.
- Sayısal türevdeki $h = 10^{-5}$ seçimi ve bilgisayarlardaki Floating Point hassasiyet sınırı.
- Gradient Descent ile modelin otomatik olarak "öğrenmesi".
