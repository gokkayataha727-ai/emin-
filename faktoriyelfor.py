sayi = int(input("Faktöriyeli hesaplanacak sayıyı girin: "))

# Çarpma işleminde etkisiz eleman 1 olduğu için 1'den başlatıyoruz
faktoriyel = 1

if sayi < 0:
    print("Negatif sayıların faktöriyeli hesaplanamaz.")
elif sayi == 0:
    print("0 sayısının faktöriyeli 1'dir.")
else:
    # 1'den başlayıp girilen sayıya kadar (sayı dahil) döngü kuruyoruz
    # range() son sayıyı dahil etmediği için sayi + 1 yazıyoruz
    for i in range(1, sayi + 1):
        faktoriyel = faktoriyel * i
        
    print(sayi, "sayısının faktöriyeli:", faktoriyel)