Kırklareli Ulaşım Güzergahı Optimizasyonu Projesi
Bu proje, Kırklareli'deki belirli mahalleler için en uygun ulaşım güzergahını belirlemek amacıyla geliştirilmiştir. Proje, çeşitli kriterlere göre mahalleleri değerlendirir ve en uygun güzergahı belirlemek için softmax fonksiyonunu kullanır. Ayrıca, maliyet-fayda analizi yaparak en faydalı güzergahı da belirler.

Kullanılan Kütüphaneler
NumPy: Sayısal hesaplamalar için kullanıldı.

Pandas: Veri işleme ve analiz için kullanıldı.

Folium: Harita üzerinde mahallelerin konumlarını göstermek için kullanıldı.

Veri Seti
Projede kullanılan veri seti aşağıdaki kriterlere göre oluşturulmuştur:

Nüfus Yoğunluğu: Mahallelerin nüfus yoğunluğu.

Mevcut Ulaşım Altyapısı: Mevcut ulaşım altyapısının kalitesi (1-5 arası puan).

Maliyet Analizi: Ulaşım altyapısı geliştirme maliyeti.

Çevresel Etki: Ulaşım altyapısı geliştirmenin çevresel etkisi (1-5 arası puan).

Sosyal Fayda: Ulaşım altyapısı geliştirmenin sosyal faydası (1-10 arası puan).

Metodoloji
Veri Normalizasyonu: Maliyet Analizi ve Çevresel Etki kriterleri tersine çevrilerek normalizasyon yapıldı.

Ağırlıklandırma: Her kriter için belirli ağırlıklar atandı.

Toplam Skor Hesaplama: Her mahalle için toplam skor hesaplandı.

Softmax Puanı Hesaplama: Softmax fonksiyonu kullanılarak her mahallenin softmax puanı hesaplandı.

Fayda-Maliyet Oranı Hesaplama: Sosyal Fayda ve Maliyet Analizi kriterleri kullanılarak fayda-maliyet oranı hesaplandı.

Harita Üzerinde Gösterim: Folium kütüphanesi kullanılarak mahallelerin konumları harita üzerinde işaretlendi.

Sonuçlar
Proje sonucunda en uygun güzergah ve en faydalı güzergah (maliyet-fayda analizi ile) belirlenmiştir. Sonuçlar aşağıdaki gibidir:

En Uygun Güzergah: en_uygun

En Faydalı Güzergah (Maliyet-Fayda Analizi ile): en_faydalı

Harita
Proje sonucunda oluşturulan harita kirklareli_harita.html dosyası olarak kaydedilmiştir. Bu dosyayı bir web tarayıcısında açarak mahallelerin konumlarını görüntüleyebilirsiniz.

Nasıl Çalıştırılır?
Gerekli kütüphaneleri yükleyin:

bash
Copy
pip install numpy pandas folium
Proje dosyasını çalıştırın:

bash
Copy
python proje_dosyasi.py
Sonuçları konsolda görüntüleyin ve kirklareli_harita.html dosyasını bir web tarayıcısında açın.

Katkıda Bulunma
Bu proje açık kaynaklıdır. Katkıda bulunmak için lütfen fork edin ve pull request gönderin.

Lisans
Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakın.
