from Day10Exercises.game import Character, Barbarian

player = Character(40)
enemy = Character(3, 3, 1, 5)


# for x in range(20):
#     enemy.attack(player)
#     print(f"After attack player has armor {player.armor} and health {player.health}")
#     x=x+1
print(Barbarian)
for x in range(20):
    Barbarian().attack(enemy)
    print(f"After attack player has armor {enemy.armor} and health {enemy.health}")
    x=x+1