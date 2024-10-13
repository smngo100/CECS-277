# Authors: Sophia Ngo, Melanie Lopez, Sara Tfaili
# Date: 4/15/2024
# Description: A game where the user must defeat three monsters to pass the trials. 

import hero
import beg_goblin
import beg_troll
import exp_goblin
import exp_troll
import random
import check_input

def main(): 
  print("Monster Trials")
  hero_name = input("What is your name? ")
  print()
  print(f"You will face a series of 4 monsters, {hero_name}.\nDefeat them all to win.\n")

  main_hero = hero.Hero(hero_name)
  monsters = [beg_goblin.BegGoblin(), beg_troll.BegTroll(), exp_goblin.ExpGoblin(), exp_troll.ExpTroll()]

  # Loop that repeats until the hero dies, or until the monsters are defeated
  while monsters and main_hero.hp > 0: 
    print(f"\nChoose an enemy to attack: ")
    for i, enemy in enumerate(monsters, start = 1):
      print(f"{i}. {enemy.name} HP: {enemy.hp}")

    monster_choice = check_input.get_int_range("Enter choice: ", 1, 4)  # Check input for invalid monster choice
    print()

    print(f"{main_hero.name} HP: {main_hero.hp}")
    print("1. Sword Attack\n2. Arrow Attack")
    weapon_choice = check_input.get_int_range("Enter choice: ", 1, 2)
    print()

    if 0 < monster_choice <= len(monsters):
      if weapon_choice == 1: # Sword attack
        print(main_hero.melee_attack(monsters[monster_choice - 1])) 
      elif weapon_choice == 2: # Arrow attack
        print(main_hero.ranged_attack(monsters[monster_choice - 1]))

      if monsters[monster_choice - 1].hp == 0: 
        defeated_monster = monsters.pop(monster_choice - 1)
        print(f"You have slain the {defeated_monster.name}.")

      if monsters: 
        attacking_monster = random.choice(monsters)
        attack_type = "melee"

        if attack_type == "melee":
          print(attacking_monster.melee_attack(main_hero))

  # Monsters defeated = Win. Hero dead = Lose.
  if not monsters: 
    print("\nCongratulations! You defeated all four monsters!\nGame Over")
  else: 
    if main_hero.hp == 0: 
      print("\nYou died.\nGame Over")
      
main()