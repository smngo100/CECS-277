import door
import random

class DeadboltDoor(door.Door):
  """Represents a deadbolt door.
  Attributes:
  _bolt1 (int): the state of the door
  _bolt2 (int): the state of the door"""
  
  def __init__(self):
    """Randomizes the state of the two bolts (either locked or unlocked)."""
    self._bolt1 = random.randint(0,1)
    self._bolt2 = random.randint(0,1)

  def examine_door(self):
    """Returns a string description of the door."""
    return "You encounter a double deadbolt door, both deadbolts must be unlocked to open it, but you can't tell from looking at them whether they're locked or unlocked."

  def menu_options(self):
    """Returns the number of options in the above menu."""
    return "1. Toggle bolt 1\n2. Toggle bolt 2"

  def get_menu_max(self):
    """Returns the number of options in the above menu."""
    return 2

  def attempt(self,option):
    """Passes in the user's selection from the menu. Uses that value to update attributes needed to determine whether user has unlocked door. Returns a string describing what the user attempted."""
    if option == 1: 
      if self._bolt1 == 1:
        self._bolt1 = 0
      else: 
        self._bolt1 = 1
      return "You toggle the first bolt."
    else:
      if self._bolt2 == 1: 
        self._bolt2 = 0
      else: 
        self._bolt2 = 1
      return "You toggle the second bolt."    

  def is_unlocked(self):
    """Checks to see if the door was unlocked, returns true if it is, false otherwise."""
    return self._bolt1 == 1 and self._bolt2 == 1

  def clue(self):
    """Returns the hint that is returned if the user was unsuccessful at their attempt."""
    if self._bolt1 == 1 or self._bolt2 == 1: 
      return "You jiggle the door... it seems like one of the bolts is unlocked."
    else: 
      return "You jiggle the door... it's completely locked."
    
  def success(self):
    """Returns the congratulatory message if the user was successful."""
    return "You unlocked both deadbolts and opened the door."
    