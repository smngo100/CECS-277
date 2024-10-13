import abc 

class Character(abc.ABC): 
  """Abstract class for a character in the game.
  Attributes:
  _name (str): The name of the character"""
  
  def __init__(self, n):
    """Initializes the character's name."""
    self._name = n 

  @property 
  def name(self): 
    return self._name

  def __str__(self): 
    """Character's name, abilities, and stats."""
    return f"Name: {self._name}\nAbilities: {self.abilities()}\nConstitution: {self.constitution()}\nStrength: {self.strength()}\nWisdom: {self.wisdom()}"

  @abc.abstractmethod
  def abilities(self): 
    pass

  @abc.abstractmethod
  def constitution(self): 
    pass 

  @abc.abstractmethod
  def strength(self): 
    pass 

  @abc.abstractmethod
  def wisdom(self): 
    pass 
