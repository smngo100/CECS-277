import entity
import random

class ExpTroll(entity.Entity): 
  """Represents an expert troll."""
  
  def __init__(self): 
    super().__init__("Angry Troll", random.randint(15, 18))

  def melee_attack(self, enemy): 
    """Randomizes the damage and applies it to the enemy."""
    damage = random.randint(8, 12)
    enemy.take_damage(damage)
    return f"{self.name} slams {enemy.name} for {damage} damage."
