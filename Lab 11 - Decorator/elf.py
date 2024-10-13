import character 

class Elf(character.Character): 
  """Represents an Elf character."""

  def __init__(self, n):
    """Initilizes the name with the Elf."""
    super().__init__(n + "the Elf")

  def abilities(self):
    """Starting list of levels for Elf abilities."""
    return [1, 0, 0, 0]

  """Returns the starting stats of con, str, and wis."""
  def constitution(self):
    return 13 

  def strength(self):
    return 10

  def wisdom(self):
    return 15
