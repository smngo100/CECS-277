import character 

class Dwarf(character.Character): 
  """Represents a Dwarf character."""
  
  def __init__(self, n):
    """Initilizes the name with the Dwarf."""
    super().__init__(n + "the Dwarf")

  def abilities(self):
    """Starting list of levels for Dwarf abilities."""
    return [0, 1, 0, 0]

  """Returns the starting stats of con, str, and wis."""
  def constitution(self):
    return 13 
  
  def strength(self):
    return 15
  
  def wisdom(self):
    return 10 
