import enemy_factory
import beg_goblin
import beg_troll
import random

class BeginnerFactory(enemy_factory.EnemyFactory): 
  """Factory that creates easy enemies."""

  def create_random_enemy(self): 
    """Randomizes and constructs one of the beginner enemies."""
    beg_enemies = [beg_goblin.BegGoblin, beg_troll.BegTroll]
    selected_enemy = random.choice(beg_enemies)
    return selected_enemy
    