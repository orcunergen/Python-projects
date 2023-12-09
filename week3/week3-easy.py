def string_combiner(args):
    final = ""
    for a in args:
        sonuc = ""
        for b in a:
            if (b in noktalama):
                pass
            else:
                sonuc += b
        final += sonuc + " "   
    return final.strip() + "."
noktalama = [".",",","!","?"]
liste=[]
while True:
    a = input("birleştirmek istediğiniz ifadeleri giriniz! \n ~ \nifadeleri girdikten sonra çalıştırmak için '1' yazınız.\n")
    if(a == "1"):
        break
    else:
        liste.append(a)
print(string_combiner(liste))
