# 11. Python ile Modüller ve Kütüphaneler
# Python modüllerini kullanma: import
# Matematik modülü: math
# Rastgele sayı üretimi: random
# Zaman işlemleri: time, datetime

# math modülünden pi sabitini import ederiz
from math import pi  
# random modülünü import ederiz
import random  
# time modülünü import ederiz
import time  
# datetime modülünü import ederiz
import datetime  

# pi sabitini ekrana yazdırır
print(pi)  # 3.141592653589793

# random modülünü kullanarak 0 ile 1 arasında rastgele bir sayı üretir
print(random.random())  # 0.0 ile 1.0 arasında rastgele bir sayı döndürür

# time modülünü kullanarak geçerli zamanın Unix zaman damgasını ekrana yazdırır
print(time.time())  # Geçerli zamanın başlangıçtan (1970) itibaren saniye cinsinden değeri

# datetime modülünü kullanarak geçerli tarih ve saat bilgisini ekrana yazdırır
print(datetime.datetime.now())  # Geçerli tarihi ve saati "YYYY-MM-DD HH:MM:SS" formatında döndürür
