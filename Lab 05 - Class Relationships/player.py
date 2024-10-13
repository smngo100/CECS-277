import die

class Player:
  """Represents a list of 3 die objects and the player's points."""

  def __init__(self):
    """Initializes the list of 3 die objects and the player's points."""
    self._dice = [die.Die(), die.Die(), die.Die()]
    self._points = 0

  def get_points(self): 
    """Returns the player's points."""
    return self._points 

  def roll_dice(self): 
    """Calls roll on each of the die objects in the list and sorts the list."""
    for d in self._dice: 
      d.roll()
    self._dice.sort()

  def has_pair(self):
    """Returns true if two dice in the list have the same values."""
    self.roll_dice()
    if self._dice[0] == self._dice[1] or self._dice[1] == self._dice[2]: 
      self._points += 1 
      return True
    return False

  def has_three_of_a_kind(self): 
    """Returns true if all dice in the list have the same value."""
    self.roll_dice()
    if self._dice[0] == self._dice[1] == self._dice[2]: 
      self._points += 3 
      return True 
    return False

  def has_series(self):
    """Returns true if values of each of dice in list are in sequence."""
    self.roll_dice()
    if self._dice[1] - self._dice[0] == 1 and self._dice[2] - self._dice[1] == 1: 
      self._points += 2
      return True 
    return False

  def __str__(self): 
    """Returns a string format."""
    return f"D1={self._dice[0]}, D2={self._dice[1]}, D3={self._dice[2]}"
    