def add(sayi1,sayi2):                 #toplama
    sonuc = sayi1 + sayi2
    return sonuc
def multiply(sayi1,sayi2):            #çarpma
    sonuc = sayi1 * sayi2
    return sonuc
def divide(sayi1,sayi2):              #bölme
    try:
        sonuc = sayi1 / sayi2
        return sonuc
    except (ZeroDivisionError):
        print("0' bölme yapılamaz.")
def get_user_input():                     # SAYI inputu alır.
    try:
        sayi1 = int(input("sayi1: "))
        sayi2 = int(input("sayi2: "))
        return sayi1,sayi2
    except:
        pass
def calculator():                         # İŞLEM SEÇTİRİR.
    islem = input("1:toplama(+)\n2:çıkarma(-)\n3:çarpma(*)\n4:bölme(/)\n5:çıkış\n.\nişlem seçimi:\n")
    if (islem == "1"):
        try:
            a= get_user_input()
            return add(a[0],a[1])
        except:
            return("hatalı giriş!")
    elif (islem == "2"):
        try:
            a= get_user_input()
            return add(a[0],-1*(a[1]))
        except:
            return("hatalı giriş!")
    elif (islem == "3"):
        try:
            a= get_user_input()
            return multiply(a[0],a[1])
        except:
            return("hatalı giriş!")
    elif (islem == "4"):
        try:
            a= get_user_input()
            return divide(a[0],a[1])
        except:
            return("hatalı giriş!")
    elif (islem == "5"):
        return "s"
    else:
        return ("hatalı işlem seçimi!")        
while True:
    asd= calculator()
    if (asd == "s"):
        break
    elif (asd == None):
        pass
    else:
        print(asd)