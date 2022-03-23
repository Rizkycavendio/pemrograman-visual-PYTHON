# Muhammad Rizky Cavendio - 20051397011

class Persegi:
    def __init__(self, sisi):
        self.sisi=sisi

    def get_luas(self):
        return self.sisi * self.sisi

persegi=Persegi(10)

print('Luas persegi:', persegi.get_luas(), 'cm')