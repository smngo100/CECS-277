import decorator

class Archery(decorator.Decorator):
  """Archery decoration class."""
  
  def abilities(self):
    """Number of levels character has in archery ability."""
    list = [1, 0, 0, 0]
    list[0] += 1
    return list

  """Additional stat values for arhcery."""
  def constitution(self):
    return super().constitution() - 2

  def strength(self):
    return super().strength() + 5

  def wisdom(self):
    return super().wisdom() - 2
