import decorator

class Fighting(decorator.Decorator): 
  """Fighting decoration class."""

  def abilities(self):
    """Number of levels character has in fighting ability."""
    list = [0, 1, 0, 0]
    list[1] += 1 
    return list

  """Additional stat values for fighting."""
  def constitution(self):
    return super().constitution() + 2

  def strength(self):
    return super().strength() + 2

  def wisdom(self):
    return super().wisdom() - 3
