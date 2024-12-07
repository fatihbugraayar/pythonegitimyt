def demonstrate_data_types_and_arithmetic():
    """
    Bu fonksiyon, Python'da farklı veri türlerinin kullanımını
    ve temel aritmetik işlemleri göstermektedir.
    """
    
    # Veri türlerinin tanıtımı
    a = 10  # Tam sayı (Integer): Örneğin 10 gibi tam sayılar
    print(type(12))  # 12'nin veri türünü yazdırır (Çıktı: <class 'int'>)

    b = 10.5  # Ondalık sayı (Float): Örneğin 10.5 gibi ondalıklı sayılar
    print(type(b))  # b'nin veri türünü yazdırır (Çıktı: <class 'float'>)

    c = 10 + 5j  # Karmaşık sayı (Complex): Gerçek ve sanal kısmı olan sayılar, örn. 10 + 5j
    print(type(c))  # c'nin veri türünü yazdırır (Çıktı: <class 'complex'>)

    d = "Merhaba"  # Metin (String): Karakter dizileri, örn. "Merhaba"
    print(type(d))  # d'nin veri türünü yazdırır (Çıktı: <class 'str'>)

    e = True  # Mantıksal değer (Boolean): Doğru (True) veya Yanlış (False)
    print(type(e))  # e'nin veri türünü yazdırır (Çıktı: <class 'bool'>)

    f = None  # NoneType: Değerin olmadığını temsil eder, örn. None
    print(type(f))  # f'nin veri türünü yazdırır (Çıktı: <class 'NoneType'>)
    
    # Aritmetik işlemler
    a = 10  # Aritmetik işlemler için örnek tam sayı değeri
    b = 5   # Diğer bir tam sayı değeri

    # Aşağıdaki işlemleri gerçekleştirip sonuçlarını yazdırıyoruz
    print(a + b)  # Toplama: a ve b'nin toplamı (Çıktı: 15)
    print(a - b)  # Çıkarma: a'dan b'nin çıkarılması (Çıktı: 5)
    print(a * b)  # Çarpma: a ile b'nin çarpımı (Çıktı: 50)
    print(a / b)  # Bölme: a'nın b'ye bölünmesi (Çıktı: 2.0)
    print(a % b)  # Modülüs: a'nın b'ye bölümünden kalan (Çıktı: 0)
    print(a // b) # Taban bölmesi: a'nın b'ye bölümünden en büyük tam sayı (Çıktı: 2)
    print(a ** b) # Üs alma: a'nın b kuvveti (Çıktı: 100000)

# Fonksiyonu çağırarak işlevini gösteriyoruz
demonstrate_data_types_and_arithmetic()
