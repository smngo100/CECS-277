import abc 

class PuppyState(abc.ABC):
  """Interface that represents a puppy's state."""

  @abc.abstractmethod
  def play(self, puppy): 
    pass
    
  @abc.abstractmethod
  def feed(self, puppy): 
    pass
    