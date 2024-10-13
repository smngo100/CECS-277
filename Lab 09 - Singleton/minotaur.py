import random
from maze import Maze


class Minotaur:
  """Represents the monster that guards the maze."""
  
  def __init__(self):
    """Randomizes the starting location of the minotaur to any blank spaces in the maze."""
    maze = Maze()
    
    placed = False 
    while not placed: 
      r = random.randint(1, len(maze)-2) 
      c = random.randint(1,len(maze[0])-2)
      if(maze[r][c] == " "):
        placed = True
        maze[r][c] = "M"  
    
  def move_minotaur(self) :
    """Minotaur detects the hero's location in the maze and moves toward the direction."""
    maze = Maze()
    loc = maze.search_maze("M")
    result = self._move(loc, "H")
    if(result == -1):
      result = self._move(loc, "f")
    return result
    
  def _move(self, loc, target):
    maze = Maze()
    target_loc = maze.search_maze(target)

    if(target_loc[0] > loc[0] and self._check_tile(loc[0]+ 1, loc[1])):
      old = maze[loc[0]+1][loc[1]]
      maze[loc[0]][loc[1]] = " "
      maze[loc[0]+1][loc[1]] = "M"
      return old

    elif(target_loc[0] < loc[0] and self._check_tile(loc[0]-1,loc[1])):
      old = maze[loc[0] -1][loc[1]]
      maze[loc[0]][loc[1]] = " "
      maze[loc[0]-1][loc[1]] = "M"
      return old

    elif(target_loc[1] > loc[1] and self._check_tile(loc[0],loc[1]+1)):
      old = maze[loc[0]][loc[1]+1]
      maze[loc[0]][loc[1]] = " "
      maze[loc[0]][loc[1]+1] = "M"
      return old

    elif(target_loc[1] < loc[1] and self._check_tile(loc[0],loc[1]-1)):
      old = maze[loc[0]][loc[1]-1]
      maze[loc[0]][loc[1]] = " "
      maze[loc[0]][loc[1] - 1] = "M"
      return old
    else:
      return -1

  def _check_tile(self,x,y)->bool:
    '''Checks if the minotaur can move to maze[x][y]'''
    maze = Maze()
    return maze[x][y] != "*" and maze[x][y] != "f"
    