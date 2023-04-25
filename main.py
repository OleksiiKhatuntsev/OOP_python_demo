from abc import ABC


class Animal(ABC):
    def __init__(self, name, breed, weight, height):
        self.name = name
        self.breed = breed
        self.weight = weight
        self.height = height
        self.battle_roar_type = None

    def get_battle_roar(self):
        print(f"{self.name}, says {self.battle_roar_type}")


class Cat(Animal):
    def __init__(self, name, breed, weight, height):
        super().__init__(name, breed, weight, height)
        self.battle_roar_type = "mey"

    def drink_milk(self):
        print(f"{self.name} is drinking milk")

    def get_battle_roar(self):
        print(f"{self.name}, says {self.battle_roar_type} and want to kill you")

class Dog(Animal):
    def __init__(self, name, breed, weight, height):
        super().__init__(name, breed, weight, height)
        self.battle_roar_type = "gav"

    def eat_bones(self):
        print(f"{self.name}, eat bones")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    first_cat = Cat("murka", "main-coon", 5, 40)
    first_cat.get_battle_roar()

    first_dog = Dog("Patron", "very-cool-dog", 5, 40)
    first_dog.get_battle_roar()

    print(Cat.mro())
    # animal = Animal("murka-an", "main-coon", 5, 40)
    # animal.battle_roar_type()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
