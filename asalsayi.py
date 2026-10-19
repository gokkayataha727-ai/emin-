toplam = 0

# En küçük asal sayı 2 olduğu için döngüyü 2'den başlatıyoruz (100 dahil ise 101 yazılır)
for sayi in range(2, 101):
    asal_mi = True  # Başlangıçta sayıyı asal kabul ediyoruz
    
    # Sayının 2'den kendisine kadar olan sayılara bölünüp bölünmediğini kontrol ediyoruz
    for i in range(2, sayi):
        if sayi % i == 0:
            asal_mi = False  # Tam bölündüğü bir sayı çıkarsa asal değildir
            break            # Asal olmadığını anladığımız an iç döngüyü durdurabiliriz
            
    # Eğer iç döngü bittiğinde asal_mi hala True ise sayı asaldır, toplama ekle
    if asal_mi == True:
        toplam = toplam + sayi

print("1'den 100'e kadar olan asal sayıların toplamı:", toplam)