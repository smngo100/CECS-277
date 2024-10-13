import entity
import random

class ExpGoblin(entity.Entity): 
  """Represents an expert goblin."""

  def __init__(self): 
    super().__init__("Horrible Goblin", random.randint(12, 15))
  
  def melee_attack(self, enemy): 
    """Randomizes the damage and applies it to the enemy."""
    damage = random.randint(5, 8)
    enemy.take_damage(damage)
    return f"{self.name} slams {enemy.name} for {damage} damage."
    