# try-except yapısı
# Yaygın hata türleri (örneğin: ValueError, ZeroDivisionError)

try:
    # Kullanıcıdan iki sayı alınır
    a = int(input("Birinci sayıyı girin: "))  # Kullanıcıdan birinci sayıyı alır ve integer'a dönüştürür
    b = int(input("Ikinci sayıyı girin: "))  # Kullanıcıdan ikinci sayıyı alır ve integer'a dönüştürür
    
    # Bölme işlemi yapılır
    result = a / b  # İlk sayıyı ikinci sayıya böler
    print("Sonuc:", result)  # Sonuç ekrana yazdırılır

except ValueError:
    # Eğer kullanıcı sayıyı doğru girmezse (örneğin, harf veya karakter girerse)
    print("Girdiniz bir sayı değil.")  # Hata mesajı ekrana yazdırılır

except ZeroDivisionError:
    # Eğer ikinci sayıya sıfır girilirse
    print("Bir sayıyı 0'a bölemezsiniz.")  # Hata mesajı ekrana yazdırılır

# Programın sonlandırıldığını belirten mesaj
print("Program sonlandı.")
