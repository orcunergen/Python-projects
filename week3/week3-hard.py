def otopark_olustur(n):
    i = 0
    park = []
    while i < n:
        j = 0
        row = []
        while j < n:
            row.append(0)
            j +=1
        park.append(row)
        i +=1
    return park
def otopark_ciz(otopark):    #çizim fonksiyonunu void olarak tanımlayıp print'i içinde yapmıştım
    gorsel = ""              #main'i değiştirmemek için biraz uzadı ama bu şekilde güncelledim.
    for a in otopark:
        gorsel += f"{a}\n"
    return gorsel
def yer_bul(otopark):
    x=0
    y=0
    toplam = -1
    for i in range((len(otopark))) :
        for j in range(len(otopark[i])):
            if (otopark[i][j] == 0):
                if toplam < i+j :
                    toplam = i+j
                    x = i
                    y = j
                else:
                    pass
            else:
                break
    if toplam == -1 :
        print("otoparkın kapasitesi aşıldığı için araç dışarda kaldı!")     
    return (x,y)
def arac_ekle(otopark, n):    
    if n == 0:
        return
    else:
        arac_ekle(otopark, n-1)
    kordinat = yer_bul(otopark)
    otopark[kordinat[0]][kordinat[1]] = 1
def main():
    n = int(input("otoparkın bir kenar uzunluğu: "))
    otopark = otopark_olustur(n)
    print(f"otopark:\n{otopark_ciz(otopark)}")
    while True:
        try:
            cevap = int(input("eklenecek araç sayısı girin: "))
            arac_ekle(otopark,cevap)
            print(f"otopark:\n{otopark_ciz(otopark)}")
        except ValueError:
            print("geçerli bir değer girilmedi! İşlem iptal ediliyor...")
            break
        except:
            print("Hata! İşlem iptal ediliyor...")
            break
main()