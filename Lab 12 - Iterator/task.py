class Task: 
  """Task class.
  Attributes:
  _description (str): String description of the task.
  _date (str): Due date of the task.
  _time (str): Time the task is due."""

  def __init__(self, desc, date, time): 
    """Assigns the parameters to the attributes."""
    self._description = desc # description of the task
    self._date = date # due date of the task
    self._time = time # time the task is due 

  @property 
  def date(self):
    """Returns the date of the task"""
    return self._date

  def __str__(self):
    """Displays the task's information to the user."""
    return f"{self._description} - Due: {self._date} at {self._time}"
     
  def __repr__(self):
    """Returns a string used to write the task to the file."""
    return f"Task('{self._description}', '{self._date}', '{self._time}')"
  
  def __lt__(self, other):
    """Compares by date, time, and description."""
    if self._date != other._date: 
      return self._date < other._date
    elif self._time != other._time: 
      return self._time < other._time
    else: 
      return self._description < other._description 
