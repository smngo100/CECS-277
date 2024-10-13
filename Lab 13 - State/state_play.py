import puppy_state
import state_asleep

class StatePlay(puppy_state.PuppyState):
  """Represents the puppy's play state."""

  def play(self, puppy): 
    puppy.inc_plays()
    if puppy.plays >= 3: 
      puppy.change_state(state_asleep.StateAsleep())
      puppy.reset()
      return "You throw the ball again and the puppy excitedly chases it.\nThe puppy played so much it fell asleep!"
    return "You throw the ball again and the puppy excitedly chases it."
  
  def feed(self, puppy):
    return "The puppy is too busy playing with the ball to eat right now."
    