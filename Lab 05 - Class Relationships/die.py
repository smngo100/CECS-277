import random

class Die:
  """Represents a die with the number of sides and the value of the rolled die."""
  
  def __init__(self, sides = 6): 
    """Assigns the number of sides from value passed in."""
    self._sides = sides
    self._value = 0 
    self.roll()

  def roll(self): 
    """Generates a random number between 1 and the number of sides, then assign it to the die's value."""
    self._value = random.randint(1, self._sides)
    return self._value
  
  def __str__(self):
    """Returns the die's value as a string."""
    return str(self._value)
  
  def __lt__(self, other): 
    """Returns whether  the value of self is less than the value of other."""
    if self._value < other._value:
      return True 
    return False

  def __eq__(self, other):
    """Returns whether the value of self is equal to the value of other."""
    if self._value == other._value: 
      return True 
    return False
    
  def __sub__(self, other): 
    """Returns the difference between the value of self and the value of other."""
    return self._value - other._value 
