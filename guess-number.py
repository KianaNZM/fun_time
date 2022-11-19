import random

print("Hi, Welcome to number guessing game")
print("What is your name?")
name = input()
print("Okay " + name + ", I choose one integer number from 1 to 20")
print("and you have 10 times to guess that")
print("--------------------------------------")
my_number = random.randint(1, 20)
print("Start " + name + ", give me one number")

chance = 10

for time in range(10):

  print("time: %d" % (time+1))
  your_number = input()

  if int(your_number) == my_number:
    print("good job :) you guess the number in %d steps" % (time+1))
    break

  elif int(your_number) < my_number:
    print("your guess is low, guess another one!")
    if time + 1 >= 10:
      print("you can not guess my number :( the number is %d" % my_number)

  else:
    print("your guess is high, guess another one!")
    if time + 1 >= 10:
      print("you can not guess my number :( the number is %d" % my_number)
