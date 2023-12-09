sayi1 = int(input("sayı girin: "))
sayi2 = int(input("2. sayıyı girin: "))
print(f"{sayi1} + {sayi2} = {sayi1+sayi2} \n{sayi1} - {sayi2} = {sayi1-sayi2} \n{sayi1} * {sayi2} = {sayi1*sayi2}")
if(sayi2==0):
    if(sayi1==0):
        print(f"{sayi1} / {sayi2} = belirsiz")
    else:
        print(f"{sayi1} / {sayi2} = tanımsız")
        
else:
    deneme = bool(not(sayi1%sayi2))
    print(f"{sayi1} / {sayi2} = {round(sayi1/sayi2 , 2)} ")
    if(deneme):
        print("bu iki sayı birbirine tam bölünüyor")
    else:
        print("bu iki sayı birbirine tam bölünmüyor")