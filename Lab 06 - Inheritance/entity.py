class Entity: 
  """Represents the entity.
  Attributes: 
    _name (str): name of the entity
    _max_hp (int): maximum health of the entity
    _hp (int): current health of the entity"""
  
  def __init__(self, name, max_hp):
    """Initializes the entity's name, max health, and current health."""
    self._name = name 
    self._max_hp = max_hp
    self._hp = max_hp
  
  @property
  def get_name(self):
    """Accesses the entity's name."""
    return self._name 

  @property
  def get_hp(self):
    """Accesses the entity's current health."""
    return self._hp 

  def take_damage(self, dmg):
    """Subtracts the damage from the entity's hp."""
    self._hp -= dmg
    if self._hp < 0: 
      self._hp = 0 
    return dmg 

  def __str__(self):
    """Returns the entity's name and hp."""
    return f"{self._name}: {self._hp}/{self._max_hp}"
