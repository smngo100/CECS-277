# Authors: Sophia Ngo, Melanie Lopez, Sara Tfaili
# Date: 4/8/2024
# Description: Program that allows the user to wander through a maze that is guarded by a minotaur. The user wins if they reach the maze's exist without being captured by the minotaur. 

from maze import Maze
from hero import Hero
from minotaur import Minotaur

def main():
  """Displays the maze and prompts the user to enter a direction to move the Hero in."""

  m = Maze()
  h = Hero()
  mt = Minotaur() 

  game_done = False
  while not game_done:
    print(m)
    dir = input("Choose a direction (WASD): ")
    dir = dir.upper()
    result = ""
    if dir == "W":
      result = h.go_up()
    elif dir == "A":
      result = h.go_left()
    elif dir == "S":
      result = h.go_down()
    elif dir == "D":
      result = h.go_right()
    else:
      print("Invalid input")
      continue
   
    if(result == "*"):
      print("You ran into a wall!")
    elif(result == "M"):
      print("You ran into the minotaur!\nGame Over!")
      game_done = True
      continue 
    elif(result == "f"):
      print("You found the exit!")
      game_done = True
      continue
    if mt.move_minotaur() == "H":
      print("The minotaur captured you!\nGame Over!")
      game_done = True

main()