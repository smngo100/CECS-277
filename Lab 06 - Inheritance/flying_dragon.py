import dragon
import random

class FlyingDragon(dragon.Dragon):
  """Represents the flying dragon."""

  def __init__(self, name, max_hp, swoops):
    """Initializes the flying dragon's name, max hp, and swoops."""
    super().__init__(name, max_hp)
    self._swoops = swoops

  def special_attack(self, hero):
    """Overriden swoop attack. If dragon has swoops left, the hero takes a random amount of damage in the range 5-8. If not, no damage is dealt."""
    if self._swoops > 0: 
      damage = random.randint(5, 8)
      damage_taken = hero.take_damage(damage) 
      self._swoops -= 1 

      return f"The {self._name} swoops down and knocks you over for {damage_taken} damage!\n"

    else: 
      return f"The {self._name} tried to swoop down and knock you over, but failed.\n"

  def __str__(self):
    """Uses super() method to get the __str__ from the entity class, then concatenates on the number of swwops."""
    return super().__str__() + f"\nSwoop attacks remaining: {self._swoops}"
    