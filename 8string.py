# Karakter dizisi oluşturma ve indeksleme
# String metodları: lower(), upper(), strip(), replace(), split()
# String birleştirme ve dilimleme

# Karakter dizisi oluşturma
karakter_dizisi = "merhaba"  # Bir karakter dizisi (string) oluşturuluyor
print(karakter_dizisi)  # Karakter dizisi ekrana yazdırılır

# İndeksleme
# Karakter dizilerinde her karakter bir indeks ile erişilebilir
print(karakter_dizisi[0])  # İlk karakter (indis 0) ekrana yazdırılır

# String metodları
karakter_dizisi = "meR.hAba"  # Yeni bir karakter dizisi oluşturuluyor

print(karakter_dizisi.lower())  # Tüm harfler küçük harfe dönüştürülür
print(karakter_dizisi.upper())  # Tüm harfler büyük harfe dönüştürülür
print(karakter_dizisi.strip())  # Başındaki ve sonundaki boşluklar kaldırılır
print(karakter_dizisi.replace("a", "i"))  # "a" harfleri "i" ile değiştirilir
print(karakter_dizisi.split("."))  # "." karakterine göre dizi parçalanır ve bir liste oluşturulur

# String birleştirme ve dilimleme
karakter_dizisi1 = "merhaba"  # Birinci karakter dizisi
karakter_dizisi2 = "dünya"  # İkinci karakter dizisi

# İki karakter dizisini birleştirme
print(karakter_dizisi1 + " " + karakter_dizisi2)  # Birleştirilen diziler ekrana yazdırılır

# Dilimleme
# Dilimleme belirli bir aralıktaki karakterleri seçmek için kullanılır
print(karakter_dizisi1[0:3])  # İlk 3 karakter seçilir (indis 0, 1 ve 2)
