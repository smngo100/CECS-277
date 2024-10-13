import task

class Tasklist: 
  """Tasklist class.
  Attributes: 
  _tasklist (task): List of tasks.
  _n (int): Counter for the iterator."""
  
  def __init__(self):
    """Read in list of tasks from file and store them in the tasklist."""
    self._tasklist = []

    file = open("tasklist.txt")
    for line in file: 
      desc, date, time = line.strip().split(',')
      self._tasklist.append(task.Task(desc, date, time))
    self._tasklist.sort()

  def add_task(self, desc, date, time):
    """Adds a new task to the tasklist."""
    self._tasklist.append(task.Task(desc, date, time))
    self._tasklist.sort()

  def get_current_task(self):
    """Returns the task at the beginning of the list."""
    if len(self._tasklist) > 0:
      return self._tasklist[0]
    else: 
      return None

  def mark_complete(self):
    """Removes and returns the current task from the tasklist."""
    if len(self._tasklist) > 0:
      return self._tasklist.pop(0)
    else: 
      raise IndexError("No tasks to mark as complete.")

  def save_file(self):
    """Writes the contents of the tasklist to the file."""
    with open("tasklist.txt", "w") as file:
      for task in self._tasklist: 
        file.write(repr(task) + "\n")

  def __len__(self):
    """Returns the number of items in the tasklist."""
    return len(self._tasklist)
  
  def __iter__(self):
    """Initialize the iterator attribute n and returns self."""
    self._n = 0 
    return self
    
  def __next__(self):
    """Iterates the iterator one position at a time."""
    if self._n < len(self._tasklist):
      current_task = self._tasklist[self._n]
      self._n += 1 
      return current_task
    else: 
      raise StopIteration
 