import entity
import random

class BegTroll(entity.Entity): 
  """Represents a beginner troll."""

  def __init__(self): 
    super().__init__("Troll", random.randint(8, 10))

  def melee_attack(self, enemy): 
    """Randomizes the damage and applies it to the enemy."""
    damage = random.randint(5, 9)
    enemy.take_damage(damage)
    return f"{self.name} bites {enemy.name} for {damage} damage."
