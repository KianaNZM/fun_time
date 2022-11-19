import random

class GuessNumber1:
  def __init__(self, min_number, max_number, chances):
    self.random_number = random.randint(min_number,max_number)
    self.chances = chances
    self.tries = 0

  def evaluate(self, user_input):
    if self.random_number == user_input:
      return 0
    elif user_input > self.random_number:
      return 1
    else:
      return -1

  def result_interaction(self, result):
    if result == 0:
      return f'Win after {self.tries}'
    elif result == 1:
      return 'Greater'
    else:
      return 'Less'

  def get_input(self):
    return input('Please enter your guess: ')
  
  def interact(self):
    while(self.tries < chances):
      self.tries += 1
      user_input = self.get_input() 
      result = self.evaluate(user_input)
      print(result_interaction(result))
    