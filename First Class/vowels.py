vowel = 'aeiou'
s = input('Please, write a word: ')
_qtd_vowels = len([c for c in s.lower() if c in vowel])
print('There are {0} vowels.'.format(_qtd_vowels))
