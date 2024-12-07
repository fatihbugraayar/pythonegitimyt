# Değişkenler ve Girdi/Çıktı İşlemleri
# Bu bölümde değişken tanımlama, kullanıcıdan giriş alma ve çıktı biçimlendirme konuları gösterilmektedir.

# Kullanıcıdan giriş alma
ad = input("Adınız: ")  # Kullanıcıdan bir isim girmesini ister ve bu girişi 'ad' değişkenine atar
print("Merhaba", ad)  # Kullanıcının girdiği ismi ekrana yazdırır (klasik bir çıktı yöntemi)

# Çıktı biçimlendirme: f-string yöntemi
ad = input("Adınız: ")  # Kullanıcıdan bir isim girmesini ister ve bu girişi 'ad' değişkenine atar
print(f"Merhaba {ad}")  # 'ad' değişkenini doğrudan süslü parantez içinde çağırarak çıktı biçimlendirilir

# Çıktı biçimlendirme: .format() yöntemi
ad = input("Adınız: ")  # Kullanıcıdan bir isim girmesini ister ve bu girişi 'ad' değişkenine atar
print("Merhaba {}, adssasd {}".format(ad, ad))  
# .format() yöntemi kullanılarak 'ad' değişkeni belirtilen yerlere yerleştirilir
# İlk süslü parantez 'ad' değişkeninin değerini alır, ikinci süslü parantez de aynısını alır
