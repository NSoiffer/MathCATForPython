# MathCAT #

* Yazar: Neil Soiffer
* [Kararlı sürümü indir][1]

MathCAT, sonunda MathPlayer'ın yerini alacak şekilde tasarlanmıştır çünkü
MathPlayer artık desteklenmemektedir. MathCAT, MathML'den konuşma ve braille
oluşturur. MathCAT tarafından üretilen matematik konuşması, kulağa daha
doğal gelmesi için prozodi ile geliştirilmiştir. Konuşma, MathPlayer ile
aynı komutlar kullanılarak üç modda gezinilebilir. Ek olarak, navigasyon
düğümü bir braille ekranda gösterilir. Hem Nemeth hem de UEB teknik
desteklenir.

MathCAT konuşma, Gezinme ve braille'i kontrol eden bir dizi yapılandırma
seçeneğine sahiptir.  Bunların çoğu MathCAT ayarlar iletişim kutusunda
ayarlanabilir (NVDA Tercihler menüsünde bulunur).  Bu ayarlar hakkında daha
fazla bilgi için [MathCAT belgelerine]
(https://nsoiffer.github.io/MathCAT/users.html) bakın.  Belgeler
[MathCAT'teki tüm gezinme komutlarını listeleyen bir
tablo](https://nsoiffer.github.io/MathCAT/nav-commands.html) için bir
bağlantı içerir.

Not: MathCAT, MathML'den konuşma ve braille oluşturmaya yönelik genel bir
kitaplıktır. NVDA dışında diğer AT projeleri tarafından kullanılır. Genel
olarak MathCAT projesi hakkında bilgi için ana [MathCAT Dokümantasyon
sayfasına](https://nsoiffer.github.io/MathCAT) bakın.


MathCAT'ı kimler kullanmalı:

* Yüksek kaliteli Nemeth braille'e ihtiyaç duyanlar (MathPlayer'ın Nemeth'i,
  teknik olarak düzeltilmesi zor olan bir dizi önemli hataya sahip olan
  liblouis'in Nemeth nesline dayanmaktadır).
* UEB teknik braille'e ihtiyaç duyanlar
* En son teknolojiyi denemek isteyenler ve hataları bildirerek yardım etmeye
  istekli olanlar
* Eloquence sesini kullananlar

MathCAT'ı kimler KULLANMAMALIDIR:

* MathPlayer'ı İngilizce dışında bir dille kullanan herkes (Endonezce ve
  Vietnamca için çeviriler mevcuttur; çeviriler gelecekte eklenecektir)
* MathPlayer'ı Nemeth olmayan/UEB olmayan braille çıktısıyla kullanan herkes
  (bir braille çevirisine yardımcı olmak istiyorsanız benimle iletişime
  geçin)
* Access8Math'i MathPlayer'a tercih eden herkes (konuşma veya diğer
  özellikler için)

MathCAT'in konuşma kuralları henüz MathPlayer'ın kuralları kadar kapsamlı
değil -- bu, MathPlayer'a bağlı kalmanın başka bir nedeni olabilir. MathCAT,
yazarların niyetlerini ifade etmelerine izin veren MathML 4 fikirleri için
bir test ortamı olarak kullanılıyor, böylece belirsiz gösterimler doğru bir
şekilde konuşulabilir ve tahmin edilemez. MathCAT'in mimarisi, yazar
niyetini kullanma ve çıkarım yapma etrafında toplandığından ve bunlar henüz
tam olarak çözülmediğinden, çok fazla kural eklemeyi erteledim.

## MathCAT Güncelleme Günlüğü

### Sürüm 0.2
* Çok sayıda hata düzeltmesi
* Konuşma iyileştirmeleri
* Duraklatma süresini kontrol etmek için bir tercih ayarı (matematik için
  göreli konuşma hızındaki değişikliklerle çalışır)
* Kimya gösterimini tanıma ve uygun şekilde konuşma desteği
* Endonezce ve Vietnamca çeviriler


### Sürüm 0.2.5
* Kimya alanında daha fazla iyileştirme
* Nemeth için Düzeltmeler:
* "İhmal" kuralları eklendi
* İngilizce Dil Göstergeleri için bazı kurallar eklendi
* Çok amaçlı göstergenin gerekli olduğu daha fazla durum eklendi
* Nemeth ve noktalama işaretleri ile ilgili düzeltmeler


### Sürüm 0.3.3
Bu sürümde bir dizi hata düzeltmesi var. Başlıca yeni özellikler ve hata
düzeltmeleri şunlardır:

* İspanyolca Çeviri eklendi (Noelia Ruiz ve María Allo Roldán'a teşekkürler)
* Gezinme bir seviye yakınlaştırılmış olarak başlayacak şekilde değiştirildi
* Tablo yapılarında gezinmenin bir yolu olarak ctrl+alt+ok eklendi. Bu
  tuşlar, NVDA'da tablolarda gezinmek için kullanıldıkları için daha akılda
  kalıcı olmalıdır.
* Göreli Matematik Hızı metin konuşma hızından daha yavaş olarak
  ayarlandığında, eSpeak seslerinin yavaşlamasına neden olan NVDA hatası
  giderildi.
* Uzun 'a' sesini konuşabilmeleri için OneCore ses problemi üzerinde
  çalıştık.

Hem Nemeth hem de UEB için konuşmada pek çok küçük ayar ve bazı hata
düzeltmeleri var.

Not: Artık Vietnam'ın braille standardını braille çıktısı olarak alma
seçeneği var. Bu hala devam eden bir çalışma ve test dışında
kullanılamayacak kadar hatalı. Bir sonraki MathCAT sürümünün güvenilir bir
uygulama içermesini bekliyorum.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=mathcat
