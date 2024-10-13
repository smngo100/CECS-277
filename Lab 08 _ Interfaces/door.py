import abc

class Door(abc.ABC):
  """Represents a door."""
  
  @abc.abstractmethod
  def examine_door(self):
    """Returns a string description of the door."""
    pass

  @abc.abstractmethod
  def menu_options(self): 
    """Returns a string of the menu options that user can choose from when attempting to unlcok the door."""
    pass

  @abc.abstractmethod
  def get_menu_max(self): 
    """Returns the number of options in the above menu."""
    pass

  @abc.abstractmethod
  def attempt(self, option):
    """Passes in the user's selection from the menu. Uses that value to update attributes needed to determine whether user has unlocked door. Returns a string describing what the user attempted."""
    pass

  @abc.abstractmethod
  def is_unlocked(self): 
    """Checks to see if the door was unlocked, returns true if it is, false otherwise."""
    pass 

  @abc.abstractmethod
  def clue(self):
    """Returns the hint that is returned if the user was unsuccessful at their attempt."""
    pass

  @abc.abstractmethod
  def success(self):
    """Returns the congratulatory message if the user was successful."""
    pass
    