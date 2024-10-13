import decorator

class Fire(decorator.Decorator): 
  """Fire decoration class."""

  def abilities(self):
    """Number of levels character has in fire magic ability."""
    list = [0, 0, 1, 0]
    list[2] += 1 
    return list

  """Additional stat values for fire magic."""
  def constitution(self):
    return super().constitution() - 3

  def strength(self):
    return super().strength() - 1

  def wisdom(self):
    return super().wisdom() + 5
