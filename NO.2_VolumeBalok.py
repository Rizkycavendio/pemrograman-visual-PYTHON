# Muhammad Rizky Cavendio - 20051397011

class Balok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang=panjang
        self.lebar=lebar
        self.tinggi=tinggi

    def get_volume(self):
        return int (self.panjang * self.lebar * self.tinggi)

balok=Balok(7, 4, 5)

print('Volume balok adalah:', balok.get_volume(),'cm^3')