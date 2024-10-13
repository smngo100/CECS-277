import dragon 
import random 

class FireDragon(dragon.Dragon):
  """Represents the fire dragon."""

  def __init__(self, name, max_hp, f_shots):
    """Initializes the fire dragon's name, max hp, and fire shots."""
    super().__init__(name, max_hp)
    self._f_shots = f_shots 

  def special_attack(self, hero):
    """Overriden the fire attack. If dragon has fire shots left, the hero takes a random amount of damage in range 5-9. If not, no damage is dealt."""
    if self._f_shots > 0:
      damage = random.randint(5, 9)
      damage_taken = hero.take_damage(damage)
      self._f_shots -= 1 
      
      return f"The {self._name} engulfs you in flames for {damage_taken} damage!\n"

    else: 
      return f"The {self._name} tried to engulf you in flames, but failed.\n"

  def __str__(self): 
    """Uses super() method to get the __str__ from the entity class, then concatenates on the number of fire shots."""
    return super().__str__() + f"\nFire Shots remaining: {self._f_shots}"
    