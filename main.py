from abc import ABC, abstractmethod

# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Конкретные классы оружия
class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"

class Bow(Weapon):
    def attack(self):
        return "наносит удар из лука"

# Класс бойца
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if not self.weapon:
            print(f"{self.name} не вооружен!")
        else:
            print(f"{self.name} {self.weapon.attack()}")

# Класс монстра
class Monster:
    def __init__(self, name):
        self.name = name

    def is_defeated(self):
        print(f"{self.name} побежден!")

# Пример использования
def main():
    fighter = Fighter("Боец")
    monster = Monster("Монстр")

    # Выбираем меч
    sword = Sword()
    fighter.change_weapon(sword)
    print(f"{fighter.name} выбирает меч.")
    fighter.attack()
    monster.is_defeated()

    # Выбираем лук
    bow = Bow()
    fighter.change_weapon(bow)
    print(f"{fighter.name} выбирает лук.")
    fighter.attack()
    monster.is_defeated()

if __name__ == "__main__":
    main()