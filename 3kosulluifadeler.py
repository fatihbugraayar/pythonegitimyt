# Kullanıcıdan iki sayı alıp toplamlarını kontrol eden bir program

# Kullanıcıdan birinci sayıyı al ve tam sayıya çevir
sayi1 = int(input("Birinci sayıyı girin: "))

# Kullanıcıdan ikinci sayıyı al ve tam sayıya çevir
sayi2 = int(input("Ikinci sayıyı girin: "))

# İki sayının toplamını hesapla
toplam = sayi1 + sayi2

# Toplamın 10'a eşit olup olmadığını kontrol et
if toplam == 10:
    # Eğer toplam 10'a eşitse bu mesajı yazdır
    print(f"Sayınız 10'a eşit. İlk sayınız: {sayi1}, ikinci sayınız: {sayi2}, toplam: {toplam}")

# Toplam 10'dan büyükse bu durumu kontrol et
elif toplam > 10:
    # Eğer toplam 10'dan büyükse bu mesajı yazdır
    print(f"Sayınız 10'dan büyük. İlk sayınız: {sayi1}, ikinci sayınız: {sayi2}, toplam: {toplam}")

# Yukarıdaki durumlar dışında toplamın 10'dan küçük olduğu durum
else:
    # Eğer toplam 10'dan küçükse bu mesajı yazdır
    print(f"Sayınız 10'dan küçük. İlk sayınız: {sayi1}, ikinci sayınız: {sayi2}, toplam: {toplam}")
