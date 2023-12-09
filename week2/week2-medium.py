ilanlar={}
while True:
    islem = input("yapmak istediğiniz işlemi seçiniz: \n -ilan eklemek: 1 \n -ilan çıkarmak: 2 \n -çıkış: 3 \n ~ \n ")
    if (islem == "1"):
        ad= input("ilan adı girin: ")
        if(ad in ilanlar):
            print("\n Bu isimde bir ilan zaten bulunmaktadır.\n ")
            continue
        else:
            marka = input("marka: ")
            model = input("model: ")
            yıl = input("yıl: ")
            fiyat = input("fiyat: ")
            ozellikler={
            "marka": marka,
            "model": model,
            "yıl": yıl,
            "fiyat": fiyat}
            ilanlar[ad] = ozellikler
            print(f"\n {ad} isimli ilan başarıyla eklendi! \n ")
    elif (islem =="2"):
        deneme = input("silmek istediğiniz ilanın adını giriniz: ")
        if (deneme in ilanlar):
            del ilanlar[deneme]
            print(f"\n {deneme} ilanı başarıyla silindi! \n")
        else:
            print(" \n bu isimde bir ilan bulunmamaktadır. \n ")
            continue
    elif (islem =="3"):
        print("çıkılıyor. \n ~ \n ~ \n ~")
        break
    else:
        print("\n hatalı giriş yaptınız, tekrar deneyiniz. \n ~ \n ~")