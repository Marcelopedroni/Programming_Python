from time import sleep
word = input("Give me a word and i'll cheer for you: ")
interable = int(input('How much of enthusiasm are you? (1-10): '))
i = 0
vowels = 'aeiou'
while i < len(word):
  if word[i] in  vowels:
    print('Give me an {}: {}!!'.format(word[i], word[i]))
    sleep(0.5)
  else:
    print('Give me a {}: {}!!'.format(word[i], word[i]))
    sleep(0.5)
  i += 1
i = 0
print('What does that spell??')
print('==========')
while i < interable:
  print('{} !!!'.format(word))
  i += 1
  sleep(1)
