import decorator

class Healing(decorator.Decorator): 
  """Healing decoration class."""
  
  def abilities(self):
    """Number of levels character has in healing ability."""
    list = [0, 0, 0, 1]
    list[3] += 1 
    return list

  """Additional stat values for healing."""
  def constitution(self):
    return super().constitution() + 3

  def strength(self):
    return super().strength() - 4

  def wisdom(self):
    return super().wisdom() + 2
