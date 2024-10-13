import abc

class Entity(abc.ABC): 
  """Represents an entity.
  Attributes: 
  _name (str): Name of the entity.
  _hp (int): Health points of the entity."""
  
  def __init__(self, name, hp):
    """Initializes the entity's name and hp."""
    self._name = name
    self._hp = hp

  @property
  def name(self):
    """Accesses the entity's name."""
    return self._name 

  @property
  def hp(self):
    """Accesses the entity's hp."""
    return self._hp 

  def take_damage(self, dmg): 
    """Deals the damage the entity takes."""
    self._hp -= dmg
    if self._hp < 0: 
      self._hp = 0
    return dmg

  def __str__(self): 
    """Entity's name and hp."""
    return f"{self._name} HP: {self._hp}"

  @abc.abstractmethod 
  def melee_attack(self, enemy):
    """The attack the entity does to another entity."""
    pass
    