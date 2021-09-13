s = input('Write a word or phrase, please: ')
c = s[0]
sub_list = []
for i in s[1:]:
  if (i >= c[-1]):
    c += i
  else:
    sub_list.append(c)
    c = i
  sub_list.append(c)

print('The largest alphabetic sequence in your sentence is: {0}'.format(max(sub_list, key=len)))
