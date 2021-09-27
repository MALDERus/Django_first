class Unit:

    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def attack(self, target):
        target.hp -= self.dmg

class FlyUnitMixin:

    def fly(self):
        print(f'{self.name} летит на {self.fly_item}')

class Dragon(FlyUnitMixin, Unit):
    fly_item = 'Крылья'


class Witch(FlyUnitMixin, Unit):
    fly_item = 'Метла'


orche = Unit('Орче', 100, 25)
gnome = Unit('Гном', 100, 25)

orche.attack(gnome)
print(gnome.hp)

gorynych = Dragon('Горыныч', 100, 25)
yaha = Witch('Баба Яга', 100, 25)

gorynych.fly()
yaha.fly()