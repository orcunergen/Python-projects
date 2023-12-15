class sekil:
    def __init__(self,kenar_sayisi):
        self.kenar_sayisi = kenar_sayisi
        
    
    def ic_acilar_toplami(self):
        return (int(self.kenar_sayisi)-2)*180
    def bir_ic_aci(self):
        return self.ic_acilar_toplami()/self.kenar_sayisi
    
ucgen = sekil(3)
print(ucgen.ic_acilar_toplami())
print(ucgen.bir_ic_aci())