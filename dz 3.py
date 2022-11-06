import random

class Mama:
    def __init__(self, zarplata):
        self.zarplata = zarplata
        self.produkty = 2

class Rabota:
    def __init__(self):
        self.zadacha = 8
        self.mama = mama
    def smena(self):
        if self.zadacha >= 8:
            print("Opyat na rabotu, ne hochu rabotat, ya ustala:(")
            self.mama.zarplata += 45
            if self.mama.zarplata > 100:
                print("Vkustnenkoe!!!")
                self.mama.zarplata -= 42
                self.mama.produkty += 2
    def vihodnoi(self):
        print("Hochy otdohnut!!!")
        self.batya.pivo -= 3
    def live(self):
        cube = random.randint(1, 2)
        if cube == 1:
            self.smena()
        elif cube == 2:
            self.vihodnoi()

mama = Mama(40)
rabota = Rabota()
rabota.live()
