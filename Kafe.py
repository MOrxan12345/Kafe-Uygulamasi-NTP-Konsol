from sys import *
import sqlite3

baglanti = sqlite3.connect("KafaVeritabani.db")
cursor = baglanti.cursor()



class KafeSinifi():

    def __init__(self):
        self.tabloOlustur()

    def tabloOlustur(self):
        cursor.execute("CREATE TABLE If not exists KafeVeri (Masa INT, Tutar INT)")

        # Başarılı bu metod duğru çalışıyor

    def hesaplariGoruntule(self):
        cursor.execute("SELECT * FROM KafeVeri")
        veri = cursor.fetchall()

        print("Bilgiler")
        print(veri)

        for i in veri:
            print("--------------------------------")
            print(f"Masa {i[0]} için hesap tutarı {i[1]} TL'dir")

        # Başarılı bu metod duğru çalışıyor

    def hesabaEklemeYap(self):
        masa_No = int(input("Masa No Giriniz: "))
        tutar = int(input("Tutar Giriniz: "))

        cursor.execute("Select * From KafeVeri where  Masa = ?",(masa_No,))
        veri = cursor.fetchall()[0][1]

        cursor.execute("Update KafeVeri set Tutar = ? where Masa = ?",(veri+tutar,masa_No))
        baglanti.commit()

        # Başarılı bu metod duğru çalışıyor


    def hesaptanCikar(self):
        masa_No = int(input("Masa No Giriniz: "))
        tutar = int(input("Tutar Giriniz: "))

        cursor.execute("Select * From KafeVEri where Masa = ?",(masa_No,))
        veri = cursor.fetchall()[0][1]

        cursor.execute("Update KafeVeri set Tutar = ? where Masa = ?",(veri-tutar,masa_No))
        baglanti.commit()

        # Başarılı bu metod duğru çalışıyor

