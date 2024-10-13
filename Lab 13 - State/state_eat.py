import puppy_state
import state_asleep
import state_play

class StateEat(puppy_state.PuppyState):
  """Represents the puppy's eating state."""

  def play(self, puppy): 
    puppy.inc_plays()
    puppy.change_state(state_play.StatePlay())
    return "The puppy looks up from its food and chases the ball you threw."
  
  def feed(self, puppy):
    puppy.inc_feeds()
    if puppy.feeds >= 3: 
      puppy.change_state(state_asleep.StateAsleep())
      puppy.reset()
      return "The puppy continues to eat as you add another scoop of kibble to its bowl.\nThe puppy ate so much it fell asleep!"
    return "The puppy continues to eat as you add another scoop of kibble to its bowl."
    