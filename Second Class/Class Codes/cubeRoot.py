cube = int(input('Please write a number to know the cube root of it: '))
epsilon = 0.01
guess = 0.0
increment = 0.01
num_guesses = 0
while abs(guess**3 - cube) >= epsilon and guess <= cube:
  guess += increment
  num_guesses += 1
print('Number of guesses: {} '.format(num_guesses))
if (abs(guess**3 - cube >= epsilon)):
  print('Failed to find the cube root of {}.'.format(cube))
else:
  print('{} is close to cube root of {}.'.format(guess, cube))
