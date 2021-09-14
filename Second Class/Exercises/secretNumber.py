number = int(input('Please think of a number between 0 and 100: '))
verification = False
low = 0
high = 100
guess = (high + low)/2
answer = ''

while(verification == False):
  if(number >= 0) and (number <= 99):
    break
  else:
    number = int(input('Please think of a number between 0 and 100: '))

while (answer != 'c'):
  answer = input("Is your secret number {}?\n Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly: ".format(guess)).lower()
  if(answer == 'h'):
    high = guess
  if(answer == 'l'):
    low = guess
  guess = (high + low)//2
  if(answer not in 'chl'):
    print('Sorry, I did not understand your input.')

print('Game over. Your secret number was: {}'.format(guess))
