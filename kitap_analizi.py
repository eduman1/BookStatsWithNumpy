import numpy as np

kitap_fiyatları = np.array([25,45,20,35,50,40,30])

satis_adetleri = np.array([100,150,200,120,130,80,110])
kategoriler = np.array(["Roman","Bilim","Çocuk","Tarih","Roman","Bilim","Çocuk"])

toplam_gelir = kitap_fiyatları*satis_adetleri
print("Toplam Gelir : ",kategoriler,"\n",toplam_gelir)

ortalama_fiyat = np.mean(kitap_fiyatları)

max_fiyat=np.max(kitap_fiyatları)
min_fiyat=np.min(kitap_fiyatları)

print("Ortalama Fiyat : ",ortalama_fiyat,"TL")
print("Max Fiyat : ",max_fiyat,"TL")
print("Min Fiyat : ",min_fiyat,"TL")

romanlar = kitap_fiyatları[kategoriler=="Roman"]

print("Roman Fiyatları : ",romanlar)
roman_satışları = satis_adetleri[kategoriler=="Roman"]
print("Roman Satış : ", roman_satışları)
roman_toplam_satış = np.sum(romanlar*roman_satışları)
print("Romanların Toplam Satışı : ",roman_toplam_satış,"TL")

veri= np.array([kitap_fiyatları,satis_adetleri])
veri_reshaped = np.reshape(veri,(2,7))

print(veri_reshaped)

