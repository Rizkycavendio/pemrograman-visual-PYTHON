# Muhammad Rizky Cavendio - 20051397011
# 2020A
class Tabung:
    def __init__(self, jarijari, tinggi, pi=22/7):
        self.jarijari=jarijari
        self.tinggi=tinggi
        self.pi=pi

    def get_volume(self):
        return int ((self.pi * (self.jarijari * self.jarijari)) * self.tinggi)

tabung=Tabung(3, 7)

print('Volume tabung adalah:', tabung.get_volume(),'cm^3')