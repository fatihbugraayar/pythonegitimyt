# Döngüleri açıklayan kod

# FOR DÖNGÜSÜ
# for döngüsü belirli bir aralıkta tekrar eden işlemler için kullanılır.
for i in range(5):  # 0'dan başlayarak 5'e kadar (5 dahil değil) bir aralık oluşturur
    print("Merhaba")  # Döngü her tekrar ettiğinde "Merhaba" yazdırır
# Bu döngü toplamda 5 kez çalışır ve her çalışmada "Merhaba" ekrana yazdırılır.


# WHILE DÖNGÜSÜ
# while döngüsü, belirli bir koşul sağlandığı sürece tekrar eden işlemler için kullanılır.
i = 0  # Döngüde kullanılacak sayaç değişkeni başlangıç değeri olarak 0 atanır

while True:  # Sonsuz bir döngü oluşturulur (koşul True olduğu sürece devam eder)
    print("Merhaba")  # Döngü her tekrar ettiğinde "Merhaba" yazdırır
    i += 1  # Sayaç değişkeni her döngüde 1 artırılır

    if i == 5:  # Sayaç 5 olduğunda döngüyü sonlandır
        break  # break komutu ile döngüden çıkılır
# Bu döngü de toplamda 5 kez çalışır ve her çalışmada "Merhaba" ekrana yazdırılır.
