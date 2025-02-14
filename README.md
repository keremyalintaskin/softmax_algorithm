# Kırklareli Ulaşım Güzergahı Optimizasyonu Projesi

Bu proje, Kırklareli'deki belirli mahalleler için en uygun ulaşım güzergahını belirlemek amacıyla geliştirilmiştir. Proje, çeşitli kriterlere göre mahalleleri değerlendirir ve en uygun güzergahı belirlemek için softmax fonksiyonunu kullanır. Ayrıca, maliyet-fayda analizi yaparak en faydalı güzergahı da belirler.

##  Kullanılan Kütüphaneler

- **NumPy**: Sayısal hesaplamalar için kullanıldı.
- **Pandas**: Veri işleme ve analiz için kullanıldı.
- **Folium**: Harita üzerinde mahallelerin konumlarını göstermek için kullanıldı.

##  Veri Seti

Projede kullanılan veri seti aşağıdaki kriterlere göre oluşturulmuştur:

- **Nüfus Yoğunluğu**: Mahallelerin nüfus yoğunluğu.
- **Mevcut Ulaşım Altyapısı**: Mevcut ulaşım altyapısının kalitesi (1-5 arası puan).
- **Maliyet Analizi**: Ulaşım altyapısı geliştirme maliyeti.
- **Çevresel Etki**: Ulaşım altyapısı geliştirmenin çevresel etkisi (1-5 arası puan).
- **Sosyal Fayda**: Ulaşım altyapısı geliştirmenin sosyal faydası (1-10 arası puan).

##  Metodoloji

1. **Veri Normalizasyonu**: Maliyet Analizi ve Çevresel Etki kriterleri tersine çevrilerek normalizasyon yapıldı.
2. **Ağırlıklandırma**: Her kriter için belirli ağırlıklar atandı.
3. **Toplam Skor Hesaplama**: Her mahalle için toplam skor hesaplandı.
4. **Softmax Puanı Hesaplama**: Softmax fonksiyonu kullanılarak her mahallenin softmax puanı hesaplandı.
5. **Fayda-Maliyet Oranı Hesaplama**: Sosyal Fayda ve Maliyet Analizi kriterleri kullanılarak fayda-maliyet oranı hesaplandı.
6. **Harita Üzerinde Gösterim**: Folium kütüphanesi kullanılarak mahallelerin konumları harita üzerinde işaretlendi.

##  Sonuçlar

Proje sonucunda en uygun güzergah ve en faydalı güzergah (maliyet-fayda analizi ile) belirlenmiştir.

- **En Uygun Güzergah**: `en_uygun`
- **En Faydalı Güzergah (Maliyet-Fayda Analizi ile)**: `en_faydalı`

##  Harita

Projede oluşturulan harita **`kirklareli_harita.html`** dosyası olarak kaydedilmiştir. Bu dosyayı bir web tarayıcısında açarak mahallelerin konumlarını görüntüleyebilirsiniz.

##  Nasıl Çalıştırılır?

### 1️⃣ Gerekli Kütüphaneleri Yükleyin:

```bash
pip install numpy pandas folium
```
### 2️⃣ Proje Dosyasını Çalıştırın:
```bash
python proje_dosyasi.py
```
## Lisans
Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakabilirsiniz.



