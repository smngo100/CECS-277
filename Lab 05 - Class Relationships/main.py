# Authors: Sophia Ngo, Melanie Lopez, Sara Tfaili
# Date: 2/26/2024
# Description: This program is a dice game called Yahtzee that awards the user points for pair, three-of-a-kind, or a series. 

import check_input
import die 
import player

def take_turn(Player): 
  """Rolls player's dice, displays  the dice, checks for and displays any win types, and displays the updated score."""
  while True: 
    print("-Yahtzee-")  
    Player.roll_dice() 
    print(Player)
    
    if Player.has_pair():
      print("You got a pair!")      
    elif Player.has_series():   
      print("You got a series of 3!")  
    elif Player.has_three_of_a_kind():
      print("You got 3 of a kind!") 
    else: 
      print("Aww. Too bad.")
  
    play_again = check_input.get_yes_no("Play again? (Y/N): ")
    print()
    
    if play_again: 
      print(f"Score = {Player.get_points()}")
    else: 
      print(f"Game Over.\nFinal Score = {Player.get_points()}")
      break
  
if __name__ == "__main__":
  my_player = player.Player() 
  take_turn(my_player)
  