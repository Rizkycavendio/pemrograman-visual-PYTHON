# Muhammad Rizky Cavendio - 20051397011

class jajarGenjang:
    def __init__(self, alas, tinggi):
        self.alas=alas
        self.tinggi=tinggi

    def get_luas(self):
        return self.alas * self.tinggi

jajarGenjang=jajarGenjang(19, 13)

print('Luas jajar genjang:', jajarGenjang.get_luas(),'cm')