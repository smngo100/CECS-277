# Authors: Sophia Ngo, Melanie Lopez, Sara Tfaili
# Date: 4/23/2024
# Description: This program allows the user to build a role-playing character with different abilities.

import dwarf
import elf
import halfing
import archery
import fighting
import fire
import healing
import check_input

def main():
  print("Character Maker!\nChoose your character:\n1. Dwarf\n2. Elf\n3. Halfling\n")

  choice = check_input.get_int_range("Enter choice: ", 1, 3)
  print()

  character_name = input("What is your character's name? ")
  main_character = None

  if choice == 1:
      main_character = dwarf.Dwarf(character_name)
  elif choice == 2:
      main_character = elf.Elf(character_name)
  elif choice == 3:
      main_character = halfing.Halfing(character_name)

  print(f"{character_name} the {main_character.__class__.__name__}")
  print("-Abilities-")
  abilities = main_character.abilities()
  ability_names = ["Archery", "Fighting", "Fire Magic", "Healing"]  
  for idx, ability_level in enumerate(abilities):
      if ability_level > 0:
          print(f"{ability_names[idx]}: Level {ability_level}")

  print("-Stats-")
  print(f"Con: {main_character.constitution()}")
  print(f"Str: {main_character.strength()}")
  print(f"Wis: {main_character.wisdom()}")

  abilities = {
      "Archery": archery.Archery,
      "Fighting": fighting.Fighting,
      "Fire Magic": fire.Fire,
      "Healing": healing.Healing
  }
  chosen_abilities = {}

  points_left = 5
  print(f"\nYou have {points_left} points to spend:\nAdd an ability:\n1. Archery\n2. Fighting\n3. Fire Magic\n4. Healing\n")
  while points_left > 0:
      ability_choice = check_input.get_int_range("Enter ability: ", 1, 4)
      chosen_ability_name = ability_names[ability_choice - 1]  
      chosen_ability_class = abilities[chosen_ability_name]

      if chosen_ability_name in chosen_abilities:
          if chosen_abilities[chosen_ability_name] < 2:
              chosen_abilities[chosen_ability_name] += 1
              points_left -= 1
          else:
              print(f"You already have {chosen_ability_name} at Level 2.")
      else:
          chosen_abilities[chosen_ability_name] = 1
          points_left -= 1

      print(f"\n{character_name} the {main_character.__class__.__name__}")
      print("-Abilities-")
      for ability, level in chosen_abilities.items():
          print(f"{ability}: Level {level}")
      print("-Stats-")
      print(f"Con: {main_character.constitution()}")
      print(f"Str: {main_character.strength()}")
      print(f"Wis: {main_character.wisdom()}")

      if main_character.constitution() <= 0 or main_character.strength() <= 0 or main_character.wisdom() <= 0:
          print("You have failed at making a character.")
          break

  if main_character.constitution() > 0 and main_character.strength() > 0 and main_character.wisdom() > 0:
      print("Congratulations! You have created your character.")

main()