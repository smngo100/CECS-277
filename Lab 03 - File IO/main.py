# Authors: Sophia Ngo, Melanie Lopez, Sara Tfaili 
# Date: 2/13/2024
# Description: Program that quizzes the user on the state capitals of the United States. 

import random

def main():
  """Main function of the program. Loops 10 times, asking the user to guess the capital of a random state. Displays the number of correct answers at the end."""
  
  total_points = 0
  
  statecapitals = open("statecapitals.txt")
  states_and_capitals = read_file(statecapitals)
  statecapitals.close()

  for i in range(1, 11):
    correct_state, correct_capital = get_random_state(states_and_capitals)
    possible_answers = get_random_choices(states_and_capitals, correct_capital)
    correct_choice = ask_question(correct_state, possible_answers)

    if correct_choice == possible_answers.index(correct_capital):
      total_points += 1 
      print("Correct!")
    else: 
      print(f"Incorrect! The correct answer is: {correct_capital}.")

  print(f"End of test. You got {total_points} correct.")

def read_file(statecapitals):
  """Takes file and reads in a single line of the file as a string. Returns a list of the state and capital pairs."""
  list2d = []
  for row in statecapitals: 
    state, capital = row.strip().split(",")
    list2d.append([state, capital])
  return list2d

def get_random_state(states):
  """Takes a list of state and capital pairs and returns a random state and capital pair."""
  return random.choice(states)


def get_random_choices(states, correct_capital):
  """Takes list of state and capital pairs and returns a list of four random capital choices, including the correct capital."""
  choices = [correct_capital]
  while len(choices) < 4:
    random_choice = random.choice(states)[1] 
    if random_choice != correct_capital and random_choice not in choices:
      choices.append(random_choice)
  random.shuffle(choices)
  return choices 

# DON'T KNOW HOW TO DO THIS PART WITHOUT ADDING AN EXTRA PARAMETER FIX!
def ask_question(correct_state, possible_answers):
  """Prints question, gives four possible answers, prompts user to enter selection."""
  print(f"The capital of {correct_state} is: ")
  options = ['A', 'B', 'C', 'D']
  for i in range(4):
    print(f"{options[i]}. {possible_answers[i]}", end = " ")
    if i < 3: 
      print(" ", end = " ")
  print()
  user_input = input("Enter selection: ").upper()
  while user_input not in options: 
    print("Invalid input. Input choice A-D.")
    user_input = input("Enter selection: ").upper()         
  return options.index(user_input)

if __name__ == "__main__":
  main()