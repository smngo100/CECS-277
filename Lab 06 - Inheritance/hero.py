import entity
import random 

class Hero(entity.Entity):
  """Represents the hero."""

  def sword_attack(self, dragon): 
    """Dragon takes a random amount of damage in the range 2D6 (1-6 + 1-6)."""
    damage = random.randint(1, 6) + random.randint(1,6)
    dragon.take_damage(damage)
    self._hp -= damage
    return f"You slash the {dragon._name} with your sword for {damage} damage."

  def arrow_attack(self, dragon): 
    """Dragon takes a random amount of damage in the range 1D12 (1 - 12)."""
    damage = random.randint(1, 12) 
    dragon.take_damage(damage)
    self._hp -= damage
    return f"You hit the {dragon._name} with an arrow for {damage} damage."
