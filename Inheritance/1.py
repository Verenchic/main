class Hero():
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self):
        print('Поприветствуйте героя ->', self.name)
        print('Уровень здоровья:', self.health)
        print('Класс брони:', self.armor)
        print('Сила удара:', self.power)
        print('Оружие:', self.weapon)


class Magician(Hero):
    def hello(self):
        super().print_info()
        print('Welcome to the Magician')

    def attack(self, knight):
        print(self.name, 'hits', knight.name)
        knight.health -= 50
        self.armor += 100


John = Magician('John', 10, 10, 10, 'Knife')
knight = Hero('Jamie', 50, 25, 20, 'Bow')
John.hello()

Magician.attack(John, knight)
print(knight.health)
print(John.armor)