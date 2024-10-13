import character
import abc 

class Decorator(character.Character, abc.ABC):
  """Abstract class and extends from Character.
  Attributes: 
  _char (str): character"""
  
  def __init__(self, c):
    super().__init__(c.name)
    self._char = c 
  
  def abilities(self):
    return self._char.abilities()

  def constitution(self):
    return self._char.constitution()

  def strength(self): 
    return self._char.strength()

  def wisdom(self): 
    return self._char.wisdom()
    