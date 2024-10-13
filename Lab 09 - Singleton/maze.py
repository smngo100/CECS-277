class Maze:
  """Singleton class. Represents the minotaur's maze.
  Attributes: 
  <class var> _instance: Maze object
  <class var> _initialized: A boolean to check if the maze has been initialized.
  _maze (char): A 2D list of the maze."""

  _instance = None
  _initialized = False

  def __new__(cls, *args):
    """If maze hasn't been constructed, then construct it and store it in the instance class variable and return. If it has, then return the instance."""
    if(cls._instance == None):
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__(self):
    """Create and fill 2D list from the file contents."""
    if(Maze._initialized == False):
      self._maze = []
      file = open("minomaze.txt","r")
      lines = file.readlines()
      
      for i in range(0,len(lines)):
        column = []
        read_this = lines[i].strip()
        for j in range(0,len(read_this)):
          column.append(read_this[j]) 
        self._maze.append(column)

      Maze._initialized = True
  
  def __getitem__(self, row):
    """Returns the specified row from the maze."""
    return self._maze[row] 

  def __len__(self):
    """Returns the number of rows in the maze."""
    return len(self._maze) 

  def __str__(self):
    """Returns the maze as a string in a grid format."""
    the_string = ""
    for i in range(0,len(self._maze)):
      for j in range(0,len(self._maze[i])):
        the_string += self._maze[i][j] + " " 
      the_string += "\n"

    return the_string

  def search_maze(self,ch):
    """Returns the location of the character in the maze as a two item 1D list."""
    for i in range(0, len(self._maze)):
      for j in range(0, len(self._maze[i])):
        if(self._maze[i][j] == ch):
          return [i,j]
    return [-1,-1] 
  