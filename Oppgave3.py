'''
Write a code that prints the integer 1 to 100, but if the
number is dividable by 3 print “Fizz”, if the number is
dividable by 5 print “Buzz”, and if the number is dividable
by both 5 and 3 print “FizzBuzz”. Dividable is defined as
giving 0 in rest. Hence the result should look like this:
1, 2, Fizz, 4, Buzz, Fizz, 7, ...,14, FizzBuzz, 16, ...
Hint: The modulo operator “%” might be useful.
'''

for i in range(100):
    if (i+1) % 3 == 0 and (i+1) % 5 == 0:
        print('FizzBuzz')
    elif (i+1) % 3 == 0:
        print('Fizz')
    elif (i+1) % 5 == 0:
        print('Buzz')
    else:
        print(i+1)
