#Multi inheritance lesson

#Exercise n1

# class Vehicle:
#     def move(self):
#         print("the vehicle moves forward.")
#
# class Watercraft:
#     def float(self):
#         print("The watercraft floats on water.")
#
# class AmphibiousVehicle(Vehicle, Watercraft):
#     def move_on_water(self):
#         self.float()
#         self.move()
#
# amphibious = AmphibiousVehicle()
# amphibious.move()
# amphibious.float()
# amphibious.move_on_water()
######################################################################################################################

# RPG Character System with Cooperative Multiple Inheritance

# class Fighter:
#     def __init__(self, stamina:int):
#         self.stamina = stamina
#     def attack(self):
#         self.stamina -= 5
#         print("The Fighter strikes with a weapon!")
#         print(f"Stamina: {self.stamina}")
#
#     def defend(self):
#         self.stamina -= 5
#         print("The Fighter blocks the attack!")
#         print(f"Stamina: {self.stamina}")
#
#
# class Mage:
#     def __init__(self, mana:int):
#         self.mana = mana
#
#     def cast_spell(self):
#         self.mana -= 5
#         print("The Mage casts a powerful spell!")
#         print(f"Mana: {self.mana}")
#
#
# class Rogue:
#     def __init__(self, agility:int):
#         self.agility = agility
#
#     def stealth(self):
#         self.agility -= 5
#         print("The Rogue sneaks past undetected!")
#         print(f"Agility: {self.agility}")
#
#     def attack(self):
#         self.agility -= 5
#         print("The Rogue strikes from the shadows!")
#         print(f"Agility: {self.agility}")
#
#
# class SpellBlade(Fighter, Mage):
#     def __init__(self,stamina, mana):
#         super().__init__(stamina)
#         Mage.__init__(self,mana)
#
#
# class ShadowBlade(Rogue, Fighter):
#     def __init__(self,agility,stamina):
#         super().__init__(agility)
#         Fighter.__init__(self,stamina)
#
#
# class ArcaneAssassin(Mage, Rogue):
#     def __init__(self,mana ,agility):
#         super().__init__(mana)
#         Rogue.__init__(self,agility)
#     def ambush(self):
#         self.stealth()
#         self.cast_spell()
#
# arcane = ArcaneAssassin(90, 80)
# shadow_blade = ShadowBlade(70, 60)
# spell_blade = SpellBlade(50, 40)
#
# arcane.ambush()
# shadow_blade.attack()  # Output: The Rogue strikes from the shadows! The Fighter strikes with a weapon!
# shadow_blade.stealth() # Output: The Rogue sneaks past undetected!
# shadow_blade.defend()  # Output: The Fighter blocks the attack!   spellblade = Spellblade()
# spell_blade.attack()   # Output: The Fighter strikes with a weapon! The Mage casts a powerful spell!
# spell_blade.cast_spell() # Output: The Mage casts a powerful spell
######################################################################################################################

#Exercise Animal, Mammal, Primate

# class Animal:
#     def __init__(self, name:str):
#         self.name = name
#
#     def make_noise(self):
#         print("Animal noise.")
#
# class Mammal:
#     def __init__(self, warm_blooded:bool):
#         self.warm_blooded = warm_blooded
#
#     def give_birth(self):
#         print("This animal does give birth.")
#
# class Primate(Animal, Mammal):
#     def __init__(self, name:str, warm_blooded:bool, opposable_thumbs: bool):
#         super().__init__(name)
#         Mammal.__init__(self, warm_blooded)
#         self.opposable_thumbs = opposable_thumbs
#
#     def swing(self):
#         print("Monkey swing happy.")
#
#     def make_noise(self):
#         print("banana's on the storm.")
#
# chimpanzee = Primate("Bobo", True, True)
# print(chimpanzee.name)
# print(chimpanzee.warm_blooded)
# print(chimpanzee.opposable_thumbs)
# chimpanzee.swing()
# chimpanzee.give_birth()
# chimpanzee.make_noise()
######################################################################################################################

#Exercise Zoo Management System

class Animal:
    def __init__(self, species:str, diet:str):
        self.species = species
        self.diet = diet

    def __str__(self):
        print(f"Species: {self.species}, Diet: {self.diet} diet.")

class Aquatic:
    def __init__(self, can_swim:bool):
        self.can_swim = can_swim

    def swim(self):
        if self.can_swim:
            print("Swimming in the water...")
        else:
            print("Cannot swim.")

class Terrestrial:
    def __init__(self, can_walk:bool):
        self.can_walk = can_walk

    def walk(self):
        if self.can_walk:
            print("Walking on land..")
        else:
            print("Cannot walk.")

class ZooAnimal(Animal, Aquatic, Terrestrial):
    def __init__(self, name:str, species, diet, can_swim, can_walk):
        super().__init__(species, diet)
        Aquatic.__init__(self,can_swim)
        Terrestrial.__init__(self, can_walk)
        self.name = name

    def zoo_info(self):
        print(f"{self.name} is a {self.species}, it has a {self.diet} diet and can it swim? {self.can_swim} or walk? {self.can_walk}")

penguin = ZooAnimal("Penguin", "Mammal", "Carnivore", True, True)
snake = ZooAnimal("Snake", "Reptile", "Carnivore", False, False)

penguin.zoo_info()
snake.zoo_info()

penguin.walk()
penguin.swim()
penguin.__str__()

snake.walk()
snake.swim()
snake.__str__()