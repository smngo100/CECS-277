# Authors: Sophia Ngo, Melanie Lopez, Sara Tfaili
# Date: 4/29/2024
# Description: A program that maintains a task list for the user.

import tasklist
import check_input

def main_menu(): 
  """Displays main menu."""
  print("1. Display current task\n2. Display all tasks\n3. Mark current task complete\n4. Add new task\n5. Search by date\n6. Save and quit")
  menu_choice = check_input.get_int_range("Enter choice: ", 1, 6)
  return menu_choice

def get_date(): 
  """Prompts the user to enter the month, day, and year.""" 
  month = check_input.get_int_range("Enter month: ", 1, 12)
  day = check_input.get_int_range("Enter day: ", 1, 31)
  year = check_input.get_int_range("Enter year: ", 2000, 2100)

  if month < 10 or day < 10: 
    month = f"0{month}"
    day = f"0{day}"

  return f"{month}/{day}/{year}" # MM/DD/YYYY

def get_time(): 
  """Prompts the user toenter the hour (military time) and minute."""
  print("Enter time: ")
  hour = check_input.get_int_range("Enter hour: ", 0, 23)
  minute = check_input.get_int_range("Enter minute: ", 0, 59)
  print()
  
  if hour < 10 or minute < 10: 
    hour = f"0{hour}"
    minute = f"0{minute}"
  
  return f"{hour}:{minute}" # HH:MM

def main():
  task_list = tasklist.Tasklist()
  task_count = len(task_list)
  
  while True: 
    print("-Tasklist-")
    print(f"Tasks to complete: {task_count}")
    choice = main_menu()

    if choice == 1: # Displays current task
      current_task = task_list.get_current_task()
      if current_task: 
        print(f"Current task is: ")
        print(current_task)
        print()

    elif choice == 2: # Displays all tasks 
      print("Tasks: ")
      for task in task_list:
        print(task)
      print()

    elif choice == 3: # Marks current task complete
      mark_complete = task_list.mark_complete()
      if mark_complete:
        print(f"Marking current task as complete:\n{mark_complete}")
        current_task = task_list.get_current_task()
        if current_task: 
          print(f"New current task is:\n{current_task}\n")

    elif choice == 4: # Adds new task
      desc = input("Enter a task: ")
      print("Enter due date: ")
      date = get_date()
      time = get_time()
      task_list.add_task(desc, date, time)
      task_count += 1

    elif choice == 5: #Searches task by date
      print("Enter date to search: ")
      search_date = get_date()
      print(f"Tasks due on {search_date}: ")
      found_tasks = [task for task in task_list if task.date == search_date]
      if found_tasks: 
        for task in found_tasks:
          print(task)
          print()
          
    elif choice == 6: # Saves and quit
      task_list.save_file()
      print("Saving List...")
      break

main()