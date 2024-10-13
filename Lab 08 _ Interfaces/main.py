# Authors: Sophia Ngo, Melanie Lopez, Sara Tfaili
# Date: 3/19/2024
# Description: This program simulates an escape room by having the user open a series of three doors randomly chosen from several different types of doors.

import basic_door
import dead_bolt_door
import combo_door
import check_input
import random

def open_door(door):
  print(door.examine_door())
  open = False
  while not open: 
    print(door.menu_options())
    choice = check_input.get_int_range("", 1, door.get_menu_max())

    print(door.attempt(choice))
    if door.is_unlocked(): 
      print(door.success())
      open = True
    else: 
      print(door.clue())

def main(): 
  print("Welcome to the Escape Room.\nYou must unlock 3 doors to escape...")

  for i in range(3): 
    rand = random.randint(1,3)
    door = basic_door.BasicDoor()
    if rand == 2: 
      door = combo_door.ComboDoor()
    elif rand == 3: 
      door = dead_bolt_door.DeadboltDoor()
  
    open_door(door)
    print()
  
  print("Congratulations! You escaped... this time.")

main()  