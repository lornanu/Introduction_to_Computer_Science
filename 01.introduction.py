
'''1) Translate the following sentences into Python algebraic or Boolean expressions, and evaluate them in the notebook

a) The total of £14.99, £27.95 and £19.83'''
round(14.99 + 27.95 + 19.83, 2)
#62.77


'''b) The area of a rectangle with length 20 and width 15'''

20*15
#300



'''c) 2 to the power 10'''
2**10
#1024

'''d) 17 modulo 5'''

17%5
#2


'''e) Check if the number 284 is even'''

284%2==0
#True

'''f) Check if the number 284 is even and is divisible by 3'''

284%2==0 and 284%3==0
#False


'''2) Now for something a little different. In each of the code blocks below is a Boolean expression where I have removed the brackets. Try to add the brackets to each expression in such a way that it evaluates to `True`.

Hint: The Boolean value `False` generally behaves like the integer value `0` and likewise the Boolean value `True` generally behaves like the integer value `1`. '''


a = 0 == (1 == 2)
print(a)
#True

b = 2 + (3 == 4) + 5 == 7
print(b)
#True

c = 3 < 4 and (5 < 4 or 1 < 2) and not 1 < 1
print(c)
#True

d = 1 < 2 and 2 < 1 or not (2 < 4 and 3 < 1)
print(d)
#True
