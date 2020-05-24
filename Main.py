from Kafe import *

print("""
|--------------------------------------|
|    Kafe Uygulamasına Hoş Geldiniz    |
|--------------------------------------|

""")

k = KafeSinifi()

while True:
    print("""
    
    [1] Masaları Görüntüle
    [2] Hesaba Ekleme Yap
    [3] Hesaptan Çıkar
    [Q] Çıkış
    
    """)
    secim = input("> ")

    if secim == "1":
        k.hesaplariGoruntule()
    elif secim == "2":
        k.hesabaEklemeYap()
    elif secim == "3":
        k.hesaptanCikar()
    elif secim == "Q" or secim == "q":
        baglanti.close()
        break
    else:
        print("Lütfen doğru seçim ediniz.")
