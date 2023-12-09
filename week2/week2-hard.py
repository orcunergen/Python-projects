alfabe = "zabcçdefgğhıijklmnoöprsştuüvyza"
while True:

    deneme = input("1- Şifreleme \n2- Şifre çözme \n3- Çıkış \nYapmak istediğiniz işlemi girin: \n")
    if(deneme == "1"):   #şifreleme yapılcak
        sonuc = ""
        word = input("Şifrelemek istediğiniz metni girin. \n").lower()
        for x in word:
            sonuc += alfabe[alfabe.index(x)+1]
        print(f"şifreli metin : {sonuc}")
            

    elif(deneme == "2"):  #şifre çözülcek
        sonuc = ""
        word = input("Şifresini çözmek istediğiniz metni girin. \n").lower()
        for x in word:
            sonuc += alfabe[alfabe.index(x)-1]
        print(f"Çözülen metin: {sonuc}")
    elif(deneme == "3"):
        print("Çıkış yapılıyor.")
        break

    else:
        print("\n Hatalı giriş yaptınız. \n")

