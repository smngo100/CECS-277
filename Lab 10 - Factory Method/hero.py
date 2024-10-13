import entity
import random

class Hero(entity.Entity): 
  """The user's character."""

  def __init__(self, name): 
    """Initializes the name and default hp."""
    super().__init__(name, 25)

  def melee_attack(self, enemy): 
    """Deals 2D6 damage to the enemy."""
    damage = random.randint(1, 6) + random.randint(1, 6) # The sum of two 6-sided dice
    enemy.take_damage(damage)
    return f"{self._name} slashes a {enemy._name} with a sword for {damage} damage."

  def ranged_attack(self, enemy):
    """Deals 1D12 damage to the enemy."""
    damage = random.randint(1, 12) # A one 12-sided die
    enemy.take_damage(damage)
    return f"{self._name} pierces a {enemy._name} with an arrow for {damage} damage."
    