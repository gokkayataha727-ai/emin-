kelime = input("Bir kelime veya cumle giriniz:")
sesli_harfler = "aeıioöuüAEIİOÖUÜ"
sayac = 0 
for harf in kelime : 
    if harf in sesli_harfler:
        sayac = sayac + 1 
print("Girilen kelimedeki sesli harf sayisi:",sayac)
