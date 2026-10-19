sayi = int(input("Faktöriyeli hesaplanacak sayıyı girin: "))

faktoriyel = 1

if sayi < 0:
    print("Negatif sayıların faktöriyeli hesaplanamaz.")
elif sayi == 0:
    print("0 sayısının faktöriyeli 1'dir.")
else:
    i = 1  # Çarpmaya 1'den başlayacağımız için sayacımızı 1 yapıyoruz
    
    # i sayısı, kullanıcının girdiği sayıdan küçük veya eşit olduğu sürece dönmeye devam et
    while i <= sayi:
        faktoriyel = faktoriyel * i  # O anki i değerini faktöriyel ile çarp
        i = i + 1                    # Bir sonraki sayıya geçmek için i'yi 1 artır
        
    print(sayi, "sayısının faktöriyeli:", faktoriyel)