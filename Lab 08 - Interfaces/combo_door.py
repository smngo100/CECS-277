import door
import random

class ComboDoor(door.Door): 
  """Represents a combo door.
  Attributes:
  _correct_value (int): the state of the door
  _input (int): the user's input"""

  def __init__(self): 
    """Randomizes the value to a number 1-10."""
    self._correct_value = random.randint(1, 10)
    self._input = 0

  def examine_door(self):
    """Returns a string description of the door."""
    return "You encounter a door with a combination lock, you can spin the dial to a number 1-10."

  def menu_options(self):
    """Returns the number of options in the above menu."""
    return "Enter a number 1-10: "

  def get_menu_max(self):
    """Returns the number of options in the above menu."""
    return 10 

  def attempt(self,option):
    """Passes in the user's selection from the menu. Uses that value to update attributes needed to determine whether user has unlocked door. Returns a string describing what the user attempted."""
    self._input = option
    return "You turn the dial to... " + str(option)

  def is_unlocked(self):
    """Checks to see if the door was unlocked, returns true if it is, false otherwise."""
    return self._input == self._correct_value

  def clue(self):
    """Returns the hint that is returned if the user was unsuccessful at their attempt."""
    if self._input < self._correct_value: 
      return f"Try a higher value."
    elif self._input > self._correct_value: 
      return f"Try a lower value."

  def success(self):
    """Returns the congratulatory message if the user was successful."""
    return "You found the correct value and opened the door.\n"
    