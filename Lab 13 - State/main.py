# Authors: Sophia Ngo, Melanie Lopez, Sara Tfaili
# Date: 5/6/24
# Description: This is a puppy simulator program.

import puppy
import check_input

def main():
  """Main functions that displays a menu that allows the user to play with or feed the puppy."""
  
  p = puppy.Puppy()

  print("Congratulations on your new puppy!")
 
  while True: 
    print("What would you like to do? ")
    print("1. Feed the puppy\n2. Play with the puppy\n3. Quit")
    choice = check_input.get_int_range("Enter choice: ", 1, 3)
    print()
  
    if choice == 1: 
      print(p.give_food())
  
    elif choice == 2: 
      print(p.throw_ball())
  
    elif choice == 3: 
      p.reset()
      break
    
main()