# 7. Listeler
# Liste oluşturma ve elemanlara erişim
# Liste metodları: append(), remove(), sort(), reverse()
# Döngülerle listeler üzerinde gezinme

# Liste oluşturma
liste = [1, 2, 3, 4, 5]  # 5 elemanlı bir liste oluşturuluyor
print(liste)  # Listenin tamamı ekrana yazdırılır

# Elemanlara erişim
print(liste[0])  # Listenin ilk elemanı (indis 0)
print(liste[1])  # Listenin ikinci elemanı (indis 1)
print(liste[2])  # Listenin üçüncü elemanı (indis 2)
print(liste[3])  # Listenin dördüncü elemanı (indis 3)
print(liste[4])  # Listenin beşinci elemanı (indis 4)

# Liste metodları
liste.append(6)  # Listenin sonuna 6 eklenir
print(liste)  # Güncellenmiş liste ekrana yazdırılır

liste.remove(3)  # Listeden 3 değeri çıkarılır
print(liste)  # Güncellenmiş liste ekrana yazdırılır

liste.sort()  # Liste elemanları küçükten büyüğe sıralanır
print(liste)  # Sıralanmış liste ekrana yazdırılır

liste.reverse()  # Listenin elemanları tersine çevrilir
print(liste)  # Ters çevrilmiş liste ekrana yazdırılır

# Döngülerle listeler üzerinde gezinme
liste = [1, 2, 3, 4, 5]  # Yeni bir liste oluşturuluyor

for i in range(len(liste)):  # Listenin uzunluğu kadar döngü çalıştırılır
    print(liste[i])  # Her iterasyonda listenin ilgili elemanı yazdırılır


# Örnek uygulama: Dinamik bir playlist oluşturma
playlist = []  # Boş bir liste oluşturuluyor

while True:  # Sonsuz döngü oluşturulur, kullanıcı çıkana kadar devam eder
    durum = int(input("Durum (1: Ekle, 2: Sil, 3: Çıkış): "))  # Kullanıcıdan bir seçim yapması istenir

    if durum == 1:  # Kullanıcı 1 seçerse
        playlist.append(input("Eklenecek şarkı: "))  # Şarkı adı alınır ve listeye eklenir
    elif durum == 2:  # Kullanıcı 2 seçerse
        playlist.remove(input("Silinecek şarkı: "))  # Şarkı adı alınır ve listeden silinir
    elif durum == 3:  # Kullanıcı 3 seçerse
        print("Playlist: ", playlist)  # O ana kadarki playlist yazdırılır
        break  # Döngü sonlandırılır
