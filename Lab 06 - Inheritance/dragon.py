import entity
import random

class Dragon(entity.Entity):
  """Represents the dragon."""
  
  def basic_attack(self, hero): 
    """Tail attack. The hero takes a random amount of damage in the range 3-7."""
    damage = random.randint(3, 7)
    return f"{self._name} smashes you with its tail for {damage} damage!\n"

  def special_attack(self, hero):
    """Claw attack. The hero takes a random amount of damage in the range 4-8."""
    damage = random.randint(4, 8)
    return f"{self._name} slashes you with its claws for {damage} damage.\n"
  