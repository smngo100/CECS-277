import character 

class Halfing(character.Character): 
  """Represents a Halfing character."""

  def __init__(self, n):
    """Initilizes the name with the Halfing."""
    super().__init__(n + "the Halfing")

  def abilities(self): 
    """Starting list of levels for Halfing abilities."""
    return [0, 0, 0, 1]

  """Returns the starting stats of con, str, and wis."""
  def constitution(self):
    return 15

  def strength(self):
    return 10

  def wisdom(self):
    return 13
