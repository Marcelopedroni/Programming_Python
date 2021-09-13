n = 0
s = input('Write a word, please: ').lower()
for i in range(len(s)): 
  if s[i:i+3] == "bob":
    n += 1
print('Number of times bob occurs is: {0}'.format(n))
