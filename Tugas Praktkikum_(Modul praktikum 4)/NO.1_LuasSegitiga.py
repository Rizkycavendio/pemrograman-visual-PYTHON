# Muhammad Rizky Cavendio - 20051397011
# 2020A
class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas=alas
        self.tinggi=tinggi

    def get_luas(self):
        return 0.5 * self.alas * self.tinggi

segitiga=Segitiga(10, 15)

print('Luas segitiga:', segitiga.get_luas(), 'cm')