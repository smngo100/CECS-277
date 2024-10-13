import door
import random

class BasicDoor(door.Door): 
  """Represents a basic door.
  Attributes:
  _state (int): the state of the door
  _input (int): the user's input"""

  def __init__(self):
    """Randomizes the initial the state of the door (push or pull)."""
    self._state = random.randint(1,2)
    self._input = 0 

  def examine_door(self): 
    """Returns a string description of the door."""
    return "You encounter a basic door, you can either push it or pull it to open."

  def menu_options(self):
    """Returns the number of options in the above menu."""
    return "1. Push\n2. Pull"

  def get_menu_max(self):
    """Returns the number of options in the above menu."""
    return 2 

  def attempt(self, option):
    """Passes in the user's selection from the menu. Uses that value to update attributes needed to determine whether user has unlocked door. Returns a string describing what the user attempted."""
    if option == 1: 
      self._input = 1
      return 'You push the door.'
    elif option == 2: 
      self._input = 2
      return "You pull the door."

  def is_unlocked(self):
    """Checks to see if the door was unlocked, returns true if it is, false otherwise."""
    return self._state == self._input

  def clue(self):
    """Returns the hint that is returned if the user was unsuccessful at their attempt."""
    return "Try the other way."

  def success(self):
    """Returns the congratulatory message if the user was successful."""
    return "Congratulations, you opened the door.\n"
    