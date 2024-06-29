# MathCAT #

* Yazar: Neil Soiffer
* NVDA uyumluluğu: 2018.1 veya sonrası (önceki sürümlerde denenmemiştir)
* [Kararlı sürümü indir][1]

MathCAT, MathPlayer artık desteklenmediğinden, sonunda MathPlayer'ın yerini
alacak şekilde tasarlanmıştır. MathCAT, MathML'den konuşma ve braille
üretir. MathCAT tarafından matematik için üretilen konuşma, daha doğal
görünmesi için prozodi ile zenginleştirilmiştir. Konuşmada MathPlayer ile
aynı komutlar kullanılarak üç modda gezinilebilir. Ayrıca gezinme düğümü bir
braille ekranında gösterilir. Hem Nemeth hem de UEB teknik
desteklenmektedir.

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
* UEB teknik braille, CMU (İspanyolca/Portekizce), Almanca LaTeX, ASCIIMath
  veya Vietnamca braille'e ihtiyaç duyanlar
* En son teknolojiyi denemek isteyenler ve hataları bildirerek yardım etmeye
  istekli olanlar
* Eloquence sesini kullananlar

MathCAT'ı kimler KULLANMAMALIDIR:

* MathPlayer'ı henüz MathCAT tarafından desteklenmeyen bir dille kullanan
  (Çince (Geleneksel), İspanyolca, Endonezce ve Vietnamca için çeviriler
  mevcuttur; çeviriler gelecekte gelecektir) ve desteklenen dillerden
  birinde konuşma konusunda rahat olmayan herkes.
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

### Sürüm 0.6.3

* Tüm dil ve Braille Kural dosyaları dizin bazında sıkıştırılır ve talep
  üzerine açılır.

	* Bu, şu anda Rules.zip dosyası açıldığında yaklaşık 5 MB tasarruf
	  sağlar. Daha fazla dil ve braille kodu eklendikçe daha da fazla tasarruf
	  sağlayacaktır.
	* Bu, MathCAT'in NVDA 2024.3'e dahili olarak eklenmesine hazırlık
	  niteliğindedir

* Yeni tercih 'Ondalık Ayırıcı' eklendi.

	* Varsayılan değer "Otomatik" olup diğer değerler ".", "," ve
	  "Özel"dir. İlk üç değer `Ondalık Ayırıcılar` ve `Blok Ayırıcılar`ı
	  ayarlar.
	* 'Otomatik', bu tercihleri ​​'Dil' tercihinin değerine göre
	  ayarlar. İspanyolca gibi bazı diller için bazı ülkelerde `,`, bazılarında
	  ise `.` kullanılır. Bu durumda, doğru değerin kullanıldığından emin olmak
	  için dili ülke kodunu da içerecek şekilde ayarlamak (ör. "es-es" veya
	  "es-mx") en iyisidir.

* Desteklenen dillere İsveççe eklendi.
* Unicode standardına hem "Sm" olarak işaretlenen tüm Unicode karakterlerini
  hem de matematik sınıfına sahip olanları (Alfabetik ve Glif sınıfları
  hariç) dahil etmek için daha fazla Unicode karakteri eklendi.
* Önceki bir sürümde tercihlerin çalışma şeklini değiştirdikten sonra,
  'MathRate' ve 'PauseFactor'ı dize olarak değil sayı olarak değiştirmeyi
  unuttum.
* Bir tanımın değerini ararken konuşma dosyalarına değil, _Braille_
  `definitions.yaml` dosyalarına bakmak için üçüncü bir argümanın
  verilmesinin gerektiği Braille Kurallarında (önceki değişikliklerde
  kaçırılan) hata düzeltildi.
* 'definitions.yaml' kullanımı temizlendi.
* ``, ondalık ayırıcılar için MathML temizliğindeki bazı hatalar düzeltildi.
* Hiçbir şey vurgulanmadığında braille vurgulamada bir hata buldum (belki de
  hiçbir zaman gerçekleşmez, bu yüzden bunu pratikte görmedim?)
* "Açıklama" modu çalışacak şekilde düzeltildi; hala çok az düzeyde ve
  muhtemelen henüz kullanışlı değil
* Desteklenen minimum sürüm düzeltildi

### Sürüm 0.5.6
* MathCAT iletişim kutusuna ("Gezinme" bölmesinde) Farklı
  Kopyala... eklendi.
* Konuşma stillerini değiştirirken dilin İngilizceye dönmesine neden olan
  bir hata düzeltildi.
* Gezinme ve braille ile ilgili bir hata düzeltildi
* Bazı Asciimath aralık sorunları düzeltildi.
* Geliştirilmiş kimya tanıma
* MathCAT yeni BANA Nemeth kimya spesifikasyonuna güncellendi (hala yalnızca
  tek satır ve özel durum stili/yazı tipi değişiklikleri işlenmedi)
* Sayılarda ASCII olmayan rakamlar (ör. kalın rakamlar) kullanıldığında
  oluşan çökme düzeltildi
* Matematik alfanümerik italik karakterler kullanıldığında, braille
  kodlarında italik göstergeler kullanmayın
* Kullanıcılar tarafından bildirilmeyen diğer bazı küçük hata düzeltmeleri

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

	* "İhmal" kuralları eklendi
	* İngilizce Dil Göstergeleri için bazı kurallar eklendi
	* Çok amaçlı göstergenin gerekli olduğu daha fazla durum eklendi
	* Nemeth ve noktalama işaretleriyle ilgili düzeltmeler

### Sürüm 0.2
* Çok sayıda hata düzeltmesi
* Konuşma iyileştirmeleri
* Duraklatma süresini kontrol etmek için bir tercih ayarı (matematik için
  göreli konuşma hızındaki değişikliklerle çalışır)
* Kimya gösterimini tanıma ve uygun şekilde konuşma desteği
* Endonezce ve Vietnamca çeviriler

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=mathcat
