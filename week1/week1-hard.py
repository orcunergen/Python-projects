anapara = int(input("ana para miktarı: "))
yillikfaiz = int(input("yıllık faiz oranı: "))
vade = int(input("para kaç ay kalacak? "))
sonuc = round(anapara*(vade*(yillikfaiz/12))/100 , 2)
print(f"{vade} ay sonunda, yıllık %{yillikfaiz} faiz oranıyla {anapara}TL ana paradan {sonuc}TL faiz geliri elde edilecektir.")