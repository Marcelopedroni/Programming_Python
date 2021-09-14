x = 27
epsilon = 0.01
num_guesses = 0
low = 0.0
high = x
ans = (high+low)/2.0

while abs(ans**3 - x) >= epsilon:
    print('low = {} high = {} guess number {}.'.format(low, high, num_guesses))
    num_guesses += 1
    if ans**3 <= x:
        low = ans
    else:
        high = ans
    ans = (high+low)/2.0
print('It took {} times to guess.'.format(num_guesses))
print('The {} is close to square root of {}.'.format(ans, x))
