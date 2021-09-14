x = int(input('Please, write a number to know its root: '))
epsilon = 0.01
guess = x/2.0
num_guesses = 0

while abs(guess**2 - x) >= epsilon:
  num_guesses += 1

  #Newton-Raphson formula applied to calculate square root
  guess = guess - ((guess**2)-x) / (2*guess)
print('It only took {} guesses.'.format(num_guesses))
print('Square root of {} is closely to {}.'.format(x, guess))
