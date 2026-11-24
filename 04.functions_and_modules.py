
'''1) Take a look at the built-in `round` and `sorted` functions in the Python documentation. 
Use them, with any other functions you think might be useful, to convert the unsorted list of floats into a 
sorted list of floats that are all rounded to 2 decimal places.'''

L = [3.765, 2.094, -5.092, -2.43, 2.51, 1.02]
newlist= []
#YOUR CODE GOES HERE
def sort_and_round(lst):
    for i in lst:
        newlist.append(round(i,2))
    return sorted(newlist)

print(sort_and_round(L))

#[-5.09, -2.43, 1.02, 2.09, 2.51, 3.77]



'''2) Define your own function that calculates and returns the value of the expression a*b+c for three variables `a`,`b`, and `c`.'''

def abc(a,b,c):
    total = (a*b) + c
    return total

abc(1,2,3)
abc(5,5,5)


'''3) Define your own function that will print out all prime numbers between 3 and an input `p`. It will probably be
 helpful to reuse a significant portion of code you developed for a similar question in the previous topic.'''


#YOUR CODE GOES HERE
primes=[]
def primenumsfrom3to(p):
    for i in range(3,p+1):
        if i <2:
            continue
        else:
            loopbreak = False
            for num in range(2,i):
                if i%num==0:
                    loopbreak = True
                    break
            if not loopbreak:
                # we found a prime nr
                primes.append(i)
    return primes

print(primenumsfrom3to(100))



'''4) Using the square root function of the math module, write a function to calculate and return the hypotenuse of a right angled triangle, 
where the lengths of the other two sides of the triangle are the inputs to the function. '''

#YOUR CODE GOES HERE
import math
def pythagoras(a,b):
    c = math.sqrt(a**2+b**2)
    return round(c,2)

pythagoras(1,4)




'''5) Write a function that calculates the volume of a cylinder, where the diameter and length are the inputs to the
 function. Compare how the solution varies when using the built-in value of pi from the math module compared to using 
 approximations for pi that you store in a variable yourself.'''

#YOU CODE GOES HERE

def cylinder(dia,leng):
    return math.pi * (dia **2) * leng

cylinder(2,5)
# 62.83185307179586



'''6) Generate a list of random integers using the random module. Write a function that takes this list of random integers and 
returns both the mean and median values. You may find some of the built-in Python functions useful to you again.'''
import random


def meanmedian(x):
    print(f"the number list is {x}")
    print(f"the mean is {sum(x)/len(x)}")
    
    x.sort()
    if len(x)%2 ==1:
        median = x[len(x)//2]
        print(f"the median is {median}")
    else:
        median = (x[len(x)//2] + x[(len(x)//2)-1])/2
        print(f"the median is {median}")

randlist = random.sample(range(100), 10)
meanmedian(randlist)



'''7) Implement a function called `coinToss`. The function should take a variable `n` as input, which represents the number of times to flip 
a coin. The function should return the number of heads, the number of tails, and the length of the longest streak of the same result. You should use a random number generator to implement your coin.

E.g. If the input was 15 and sequence of coin flips was HHTHTTHTTHHHTTH then we should return 8,7,3 as we flipped 8 heads, 7 tails, and there
 was a longest streak of 3 heads in a row.'''

#YOUR CODE GOES HERE
def coinToss(n):
    heads = 0
    tails = 0
    streak = 0
    prev = -1
    longeststreak=0
    for i in range(n):
        num = random.randint(0,1)
        if num ==0:
            heads = heads + 1
        else:
            tails = tails + 1
        if num == prev:
            streak = streak + 1
        else:
            prev = num
            streak = 1
        if streak > longeststreak:
            longeststreak = streak
    return (heads, tails, longeststreak)
coinToss(15)



'''8) Using the copy module, make a copy of the list L. Change some values in your new list, and print both lists out to ensure 
they are both different.'''


L = [2,4,6,8,10,9,7,5,3,1]

#YOUR CODE GOES HERE
Lcopy = L.copy()
L = [1,2,3]
print(L, Lcopy)