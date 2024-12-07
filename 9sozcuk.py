# Sözlük (dict) tanımı ve kullanımı
# Anahtar-değer çiftleri

# Sözlük tanımlama
sozluk = {"sifre": "123", "iki": 2, "uc": 3}  # Anahtar ve değer çiftlerinden oluşan bir sözlük
print(sozluk["sifre"])  # "sifre" anahtarının değerini ekrana yazdırır

# Sözlüğe yeni bir anahtar-değer çifti ekleme
sozluk["dort"] = 4  # "dort" anahtarı için değer 4 atanır
print(sozluk)  # Güncellenmiş sözlük ekrana yazdırılır

# keys() ve values() metodları

sozluk = {"bir": 1, "iki": 2, "uc": 3}  # Yeni bir sözlük tanımlanır

print(sozluk.keys())  # Sözlüğün anahtarlarını (keys) listeler
print(sozluk.values())  # Sözlüğün değerlerini (values) listeler


# Demet (tuple) tanımı ve özellikleri

# Demet tanımlama
demet = ("a", "b", "c")  # Parantez içinde tanımlanan sabit bir veri yapısı
print(demet)  # Tüm demet ekrana yazdırılır

# İndeksleme ile elemanlara erişim
print(demet[0])  # İlk eleman (indis 0) ekrana yazdırılır
print(demet[-1])  # Son eleman (negatif indeks -1) ekrana yazdırılır

# Dilimleme
print(demet[0:2])  # İlk iki eleman (indis 0 ve 1) seçilir
print(len(demet))  # Demetin uzunluğu ekrana yazdırılır

# Eleman kontrolü
print("a" in demet)  # "a" elemanı demette var mı? True veya False döndürür
print("a" not in demet)  # "a" elemanı demette yok mu? True veya False döndürür

# Yeni bir demet oluşturma
demet = ("a", "b", "c", "d", "e")
print(demet)  # Güncellenmiş demet ekrana yazdırılır

# Daha fazla dilimleme örneği
print(demet[0:3])  # İlk üç eleman (indis 0, 1, 2) seçilir
print(demet[:3])  # İlk üç eleman (indis 0, 1, 2) seçilir (başlangıç belirtilmez)
print(demet[2:])  # İkinci indeksten (indis 2) sona kadar olan elemanlar seçilir
