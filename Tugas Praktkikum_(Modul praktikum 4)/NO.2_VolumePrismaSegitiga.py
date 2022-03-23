# Muhammad Rizky Cavendio - 20051397011
# 2020A
class PrismaSegitiga:
    def __init__(self, alas, tinggi, tinggiPrisma):
        self.alas=alas
        self.tinggi=tinggi
        self.tinggiPrisma=tinggiPrisma

    def get_volume(self):
        return int ((0.5 * self.alas * self.tinggi) * self.tinggiPrisma)

prismaSegitiga=PrismaSegitiga(5, 10, 5)

print('Volume prisma segitiga adalah:', prismaSegitiga.get_volume(),'cm^3')