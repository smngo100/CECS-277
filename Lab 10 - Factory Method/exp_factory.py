import enemy_factory
import exp_goblin
import exp_troll
import random

class ExpertFactory(enemy_factory.EnemyFactory):
  """Factory that creates difficult enemies."""

  def create_random_enemy(self):
    """Randomizes and constructs one of the expert enemies."""
    exp_enemies = [exp_goblin.ExpGoblin, exp_troll.ExpTroll]
    selected_enemy = random.choice(exp_enemies)
    return selected_enemy
  