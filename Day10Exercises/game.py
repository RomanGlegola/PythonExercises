import random


class Dice(object):
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.choice(range(1, self.sides + 1))


class Character(object):
    def __init__(self, health=10, strength=5, damage=2, armor=5):
        self.health = health
        self.strength = strength
        self.damage = damage
        self.armor = armor

    def attack(self, target_character):
        target_character.defend(self.damage)

    def parry(self, damage):
        dice_to_parry = Dice()
        if dice_to_parry.roll() > damage:
            print("Attack has been parried!")
            return True

    def defend(self, damage):
        if Character.death(self, self.health) is True:
            damage = 0
        elif self.parry(damage) is True:
            damage = 0
        damage_to_health = damage - self.armor
        self.armor = self.armor - damage
        if self.armor < 0:
            self.armor = 0
        #self.armor = max(self.armor - damage,0)
        self.health = self.health - damage_to_health
        Character.death(self, self.health)

    def death(self, health):
        if health <= 0:
            self.health = 0
            print("Character has ben struck down!")
            return True
        else:
            return False

class Barbarian(Character):
    def __init__(self, health=10, strength=5, damage=6, armor=5, anger=1):
        super().__init__()
        self.anger = anger

    def __str__(self):
        return f"I'm mighty barbarian"

    def attack(self, target_character):
        print(f'This is method from {self.__class__().Barbarian()}')
        target_character.defend(self.damage + self.anger)