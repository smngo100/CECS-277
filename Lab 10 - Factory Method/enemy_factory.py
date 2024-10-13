import abc 

class EnemyFactory(abc.ABC):
  """Template for all enemy factories."""
  
  @abc.abstractmethod
  def create_random_enemy(self): 
    """Each concrete factory ovverrides to create and return enemy objects."""
    pass
    