# Bir giriş uygulaması oluşturalım

# Kullanıcı bilgilerini içeren bir liste (örnek veriler)
veriler = [
    {"kullanıcı adı": "admin", "sifre": "2131"},
    {"kullanıcı adı": "admin2", "sifre": "123"},
    {"kullanıcı adı": "admin3", "sifre": "213"},
    {"kullanıcı adı": "admin4", "sifre": "124123"}
]

# Giris fonksiyonu: Kullanıcı adı ve şifreyi kontrol eder
def giris(kullanıcı_adı, sifre):
    # Veriler üzerinde dönerek, kullanıcı adı ve şifresini karşılaştırıyoruz
    for veri in veriler:
        if veri["kullanıcı adı"] == kullanıcı_adı and veri["sifre"] == sifre:
            return True  # Eşleşme bulduysak giriş başarılıdır
        
    return False  # Eşleşme bulunamazsa giriş başarısızdır

# Kullanıcı girişini sürekli alacağız
while True:
    kullanıcı_adı = input("Kullanıcı adı: ")  # Kullanıcıdan kullanıcı adı alıyoruz
    sifre = input("Şifre: ")  # Kullanıcıdan şifre alıyoruz
    
    # Giris fonksiyonunu kullanarak, girilen kullanıcı adı ve şifreyi kontrol ediyoruz
    if giris(kullanıcı_adı, sifre):
        print("Giriş başarılı.")  # Giriş başarılı ise mesajı gösteriyoruz
        break  # Giriş başarılıysa döngüden çıkıyoruz
    else:
        print("Giriş başarısız. Lütfen tekrar deneyin.")  # Giriş başarısızsa hata mesajı
