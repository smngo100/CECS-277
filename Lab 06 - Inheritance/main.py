# Authors: Sophia Ngo, Melanie Lopez, Sara Tfaili
# Date: 3/4/2024
# Description: This is a game where the user must defeat three dragons to pass the trials. 

import hero 
import dragon 
import fire_dragon 
import flying_dragon
import check_input
import random

def main():
  """Presents a menu that allows the user to choose which dragon to attack. Presents another menu that gives them the option of attaackeing with sword or an arrow. If the dragon is defeated, it is removed from the list of dragons. Repeat attacks until the user defeats all three dragons, or the user is knocked out."""
  main_hero = hero.Hero("Hero", 50)
  dragons = [
    dragon.Dragon("Deadly Nadder", 10),
    fire_dragon.FireDragon("Gronckle", 15, 3),
    flying_dragon.FlyingDragon("Timberjack", 20, 5)
  ]

  challenger = input("What is your name, challenger?\n")
  print(f"Welcome to dragon training, {challenger}\nYou must defeat 3 dragons.\n")

  while dragons and main_hero.get_hp > 0:    
    print(f"{challenger}: {main_hero.get_hp}/{main_hero._max_hp}")
    for i in range(len(dragons)):
      print(f"{i + 1}. {dragons[i]}")
    dragon_choice = check_input.get_int_range("Choose a dragon to attack: ", 1, 3)
    print()

    print("Attack with:\n1. Arrow (1 D12)\n2. Sword (2 D6)")
    weapon_choice = check_input.get_int_range("Enter weapon: ", 1, 2)
    print()

    if 0 < dragon_choice <= len(dragons): 
      if weapon_choice == 1:
        print(main_hero.arrow_attack(dragons[dragon_choice - 1]))
      elif weapon_choice == 2: 
        print(main_hero.sword_attack(dragons[dragon_choice - 1]))
  
      if dragons[dragon_choice - 1].get_hp == 0: 
        defeated_dragon = dragons.pop(dragon_choice - 1)
        print(f"You defeated {defeated_dragon._name}.")   
    
      if dragons: 
        attacking_dragon = random.choice(dragons) 
        attack_type = random.choice(["basic", "special"])

        if attack_type == "basic":
          print(attacking_dragon.basic_attack(main_hero))
        elif attack_type == "special":      
          print(attacking_dragon.special_attack(main_hero))

  if not dragons: 
    print("Congratulations! You have defeated all 3 dragons, yuo have passed the trials.")
  else: 
    if main_hero.get_hp == 0: 
      print("You have failed the trials.")

main()
