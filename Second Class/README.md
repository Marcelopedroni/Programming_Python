<h2>Second Class</h2>


In this class there were presented a few examples of how can we calculate square root and cube root of any number using two methods.

<h3><i>cubeRoot.py</i> and <i>squareRoot.py</i></h3>

The first method is simple, it is based on incrementing by a little portion (like 0.01) and declaring epsilon = 0.01 and compare if the absolute result from the difference between the guess ** 2 and epsilon (for square root) or guess ** 3 and epsilon (for cube root).
It will iterate several times 'till it comes to a conclusion, or it will be close enough (will attend the condition at the loop) and will bring us some result real close from the expected or it will fail the loop condition and will return a message telling us that wasn't sucessful.

<h3><i>cubeRootBinarySearch.py</i> and <i>squareRootBinarySearch.py</i></h3>

The second method is way more elaborated, smart but not that hard to understand.
It apply the binary search method, wich is based not on incrementing little "steps" in each iterate, but giving a smart guesses based on the half between two initial points, each of one on extremes. 
Here, the condition of the loop uses the guess ** 2 ou guess ** 3 to do the difference with the number itself and compares with (the same) epsilon.
And if the answer ** 2 or ** 3 for the current iteration is lower than the number itself, we can forget about any number that is lower than the previous answer. The same logic is valid when the answer ** 2 or answer ** 3 is highest than number itself, this time we forget about any interval of numbers geater than the previous answer.

The number of iterations will severaly decreased, because each iteration the algorithm discards half of intervals, that's the thing about binary search method.

<h3><i>secretNumber.py</i></h3>

That is one challenge to apply the binary search in a famous guessing game. 
From a input of any integer between 0 (included) and 100 (not included) the algorithm has to guess the number. Of course, some input error deals were included. 
That're a few improvements to do, like error dealing when input other data types and other exceptions, but is fine in a didatical meaning.
