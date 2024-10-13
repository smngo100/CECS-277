import entity
import random

class BegGoblin(entity.Entity):
  """Represents a beginner goblin."""

  def __init__(self): 
    super().__init__("Goblin", random.randint(7, 9))

  def melee_attack(self, enemy): 
    """Randomizes the damage and applies it to the enemy."""
    damage = random.randint(4, 6)
    enemy.take_damage(damage)
    return f"{self.name} bites {enemy.name} for {damage} damage."
    