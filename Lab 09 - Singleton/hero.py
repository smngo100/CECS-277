from maze import Maze

class Hero:
  """Represents the player's character."""
  
  def __init__(self):
    """Sets the hero's starting location by finding the start position in the maze ('s') and then placing an 'H' in the maze at that location."""
    maze = Maze()
    start_position = maze.search_maze("s")
    maze[start_position[0]][start_position[1]]='H'

  def go_up(self):
    """Updates the hero's location by moving up."""
    maze = Maze() 
    loc = maze.search_maze("H")
    new_location = maze[loc[0] - 1][loc[1]]
    if new_location == ' ':
      maze[loc[0] - 1][loc[1]] = 'H'
      maze[loc[0]][loc[1]] = " "
    return(new_location)     

  def go_down(self):
    """Updates the hero's location by moving down."""
    maze = Maze()
    loc = maze.search_maze("H")
    new_location = maze[loc[0] + 1][loc[1]]
    if new_location == " ":
      maze[loc[0] +1][loc[1]] = "H"
      maze[loc[0]][loc[1]] = " "
    return new_location

  def go_left(self):
    """Updates the hero's location by moving left."""
    maze = Maze()
    loc = maze.search_maze("H")
    new_location = maze[loc[0]][loc[1] -1]
    if new_location == " ":
      maze[loc[0]][loc[1] -1] = "H"
      maze[loc[0]][loc[1]] = " "
    return new_location

  def go_right(self):
    """Updates the hero's location by moving right."""
    maze = Maze()
    loc = maze.search_maze("H")
    new_location = maze[loc[0]][loc[1] + 1]
    if(new_location == " "):
      maze[loc[0]][loc[1] + 1] = "H"
      maze[loc[0]][loc[1]] = " "
    return new_location
