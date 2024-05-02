# MathCAT #

* Yazar: Neil Soiffer
* NVDA uyumluluğu: 2018.1 veya sonrası (önceki sürümlerde denenmemiştir)
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

### Sürüm 0.5.0
* Almanca LaTeX braille kodu eklendi. Diğer braille kodlarından farklı
  olarak bu, ASCII karakterleri oluşturur ve karakterleri braille'e çevirmek
  için mevcut braille çıktı tablosunu kullanır.
* ASCIIMath braille kodu eklendi.  (Deneysel) LaTeX braille kodu gibi, bu da
  ASCII karakterleri oluşturur ve karakterleri braille'e çevirmek için
  mevcut braille çıktı tablosunu kullanır.
* MathML'ye odaklanıldığında (daha önce olduğu gibi) CTRL+C kullanılarak
  MathML, LaTeX veya ASCIIMath olarak kopyalamayı destekleyen "Farklı
  Kopyala" tercihi eklendi. O anda odaklanılan düğüm kopyalanır. Not: Bu
  yalnızca prefs.yaml dosyasında listelenir ve MathCAT Tercihleri ​​iletişim
  kutusunda (henüz) gösterilmez.

### Sürüm 0.4.2
* Ses değiştiğinde ve MathCAT dili "Otomatik" olduğunda dil değişimi
  düzeltildi
* Görme engelliler için ayarlanmadığında okumayı iyileştirmek amacıyla
  $Impairments için daha fazla kontrol eklendi
* Nemeth: Bir mrowun parçası olmadığında "~" için düzeltme
* UEB: karakter eklemeleri, önek ise "~" boşluk düzeltmesi, xor düzeltmesi,
* Aksanlı ünlüler için MathML temizliği (özellikle Vietnamca için)
* Tercih okuma/güncelleme kodunun büyük bir hızla yeniden yazılması - hangi
  dosyaların güncellemeler için kontrol edildiğini denetlemek için
  "CheckRuleFiles" tercihi eklendi
* İki yeni arayüz çağrısı eklendi - gezinme konumunun braille imlecinden
  ayarlanmasını sağlar (henüz MathCAT eklentisinin bir parçası değil)

### Sürüm 0.3.11
* Python 3.11'e yükseltildi ve NVDA 2024.1 ile çalıştığı doğrulandı
* Vietnamca braille alfabesindeki ve ayrıca Konuşmadaki, çoğunlukla kimyaya
  yönelik hatalar düzeltildi.
* Braille kodu ve bağımlı dil eşleşmediğinde bozuk braille düzeltildi
  (özellikle Vietnam braille ve Vietnamca konuşma)
* Belirteçlerin içindeki HTML'de bulunan boşluk hatası düzeltildi
* Roma rakamı algılaması geliştirildi

### Sürüm 0.3.9
* Geleneksel Çince çevirisi eklendi (Hon-Jang Yang sayesinde)
* Parantez içeren kodlanmış bir ifadenin tabanına gitmeyle ilgili hata
  düzeltildi
* Boşlukların işlenme şekli önemli ölçüde değiştirildi. Bu esas olarak
  braille çıktısını etkiler (boşluklar ve "ihmal" tespiti).
* Kimyanın daha iyi tanınması
* Kimya örneklerinin eklenmesiyle ortaya çıkan UEB braille düzeltmeleri
* Bazı durumlarda yardımcı parantez eklemeye yönelik UEB düzeltmeleri

### Sürüm 0.3.8
Braille:

* Diyalog birçok dilde uluslararası hale getirildi (çevirmenlere çok
  teşekkürler!)
* CMU'nun ilk uygulaması - İspanyolca ve Portekizce konuşulan ülkelerde
  kullanılan braille kodu
* Bazı UEB hataları düzeltildi ve UEB için bazı karakterler eklendi
* Vietnamca braille alfabesinde önemli iyileştirmeler

Diğer düzeltmeler:

* Göreli hız iletişim kutusunun kaydırıcısı maksimum %100 değerine sahip
  olacak şekilde değiştirildi (artık yalnızca daha yavaş hızların
  ayarlanmasına izin veriyor). Ayrıca, hızı önemli ölçüde artırmak/düşürmek
  daha kolay olacak şekilde adım boyutları eklendi.
* Göreceli hız değiştirildiğinde bazen konuşmayı kesen eSpeak hatası
  düzeltildi
* Vietnamca konuşmada iyileştirmeler
* OneCore seslerinin "a" demesiyle ilgili hata düzeltildi
* 'Otomatik Yakınlaştırma' Yanlış olduğunda (varsayılan değil) bazı gezinme
  hataları düzeltildi
* Dil değişiklikleri ve diğer bazı iletişim kutusu değişiklikleriyle ilgili
  güncellemeler düzeltildi; böylece bunların "Uygula" veya "Tamam"
  tıklandığında hemen etkili olması sağlandı.
* MathCAT'in kutudan çıkar çıkmaz doğru dilde konuşması için "Sesin Dilini
  Kullan" seçeneği eklendi (bir çeviri varsa)
* Zayıf MathML kodunu temizlemeye yönelik çeşitli iyileştirmeler

### Sürüm 0.3.3
Bu sürümde bir dizi hata düzeltmesi var. Başlıca yeni özellikler ve hata
düzeltmeleri şunlardır:

* İspanyolca Çeviri eklendi (Noelia Ruiz ve Maria Allo Roldan'a teşekkürler)
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

### Sürüm 0.2.5
* Kimya alanında daha fazla iyileştirme
* Nemeth için Düzeltmeler:

	* * "İhmal" kuralları eklendi
	* * İngilizce Dil Göstergeleri için bazı kurallar eklendi
	* * Çok amaçlı göstergenin gerekli olduğu daha fazla durum eklendi
	* * Nemeth ve noktalama işaretleriyle ilgili düzeltmeler

### Sürüm 0.2
* Çok sayıda hata düzeltmesi
* Konuşma iyileştirmeleri
* Duraklatma süresini kontrol etmek için bir tercih ayarı (matematik için
  göreli konuşma hızındaki değişikliklerle çalışır)
* Kimya gösterimini tanıma ve uygun şekilde konuşma desteği
* Endonezce ve Vietnamca çeviriler

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=mathcat
