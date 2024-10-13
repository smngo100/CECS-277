import state_asleep

class Puppy: 
  """Represents a puppy that the user interacts with.
  Attributes:
  <<get>> _plays (int): Number of times the puppy has been played with.
  <<get>> _feeds (int): Number of times the puppy has been fed.
  _state: The puppy's state."""

  def __init__(self):
    """Iniitializes the puppy's state to asleep, then initializes the number of feeds and plays."""
    self._plays = 0 
    self._feeds = 0 
    self._state = state_asleep.StateAsleep()

  @property 
  def plays(self):
    return self._plays

  @property 
  def feeds(self):
    return self._feeds

  def change_state(self, new_state): 
    """Updates the puppy's state to the new state."""
    self._state = new_state

  def throw_ball(self): 
    """Calls play method afor whichever state the puppy is in."""
    return self._state.play(self)

  def give_food(self):
    """Calls feed method for whichever state the puppy is in."""
    return self._state.feed(self)

  def inc_feeds(self):
    """Increments # of times puppy has been fed."""
    self._feeds += 1

  def inc_plays(self):
    """Increments # of times puppy has played."""
    self._plays += 1

  def reset(self):
    """Reinitializes the feeds and plays attributes."""
    self._plays = 0
    self._feeds = 0 
