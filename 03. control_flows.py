
'''1) Using conditionals, check if a number is positive, negative or zero, and print out an appropriate message in each case.'''

x=4
if x > 0:
    print("number is positive")
elif x < 0:
    print("number is negative")
elif x == 0:
    print("number is zero")
else:
    print("input is not a number")


'''2) Using a for loop and conditional statements, find and print the minimum value in a list of integers. 
Your list of integers can be anything of your choosing.'''

num = [102, 10, 1,2,3,-6, 4,5]
minnum = num[0]
for i in num:
    if i < minnum:
        minnum = i

minnum

'''3) Using a while loop and conditional statements, find and print the maximum value in your list of integers.'''

num = [102, 10, 1,2,3,-6, 4,5]
maxnum = num[0]
for i in num:
    if i > minnum:
        maxnum = i


'''4) Using a loop, calculate the sum of all the elements in odd index positions in a list.

E.g. if my list L = [324,76,12,34,97,47,23,89] then the output should be 246.'''

L=[324,76,12,34,97,47,23,89]

sumcount=0
for i in range(1,len(L),2):
    sumcount= sumcount + L[i]

print(sumcount)



'''5) Using a loop and conditional statements, calculate the sum of all of the positive values in a list.

E.g. if my list L = [34,-14,10,45,-2,-39,17,-32] then the output should be 106.'''

L = [34,-14,10,45,-2,-39,17,-32]
counter=0
for i in range(len(L)):
    if L[i] > 0:
        counter += L[i]

print(counter)



'''6) The code below generates a random number and asks the user to provide an input number. Using conditionals, 
compare the input provided by the user to the random number and give the user some feedback. 
If their input was greater than the random number, then print a message saying their guess was too large. 
If their input was less than the random number, print a message saying so. 
If the number was the same then print a message out saying their guess was correct. '''
import random
x = random.randint(0,10)    #This generates a random integer between 0 and 10 (inclusive)

y = int(input("Please enter a number:"))    #This asks the user to input a number and casts it to an integer
print("You guessed", y)

#
if y > x:
    print("your guess was too large.")
elif y<x:
    print("your guess was too small.")
else:
    print("you guessed the number!")


'''7) Lets edit your code from above to allow the user to have multiple guesses at the number. 
Wrap your conditionals in a while loop in such a way that the user can keep guessing numbers until they correctly identify the random number.'''

x = random.randint(0,10)    #This generates a random integer between 0 and 10 (inclusive)


trial = 0
while trial <5:
    y = int(input("Please enter a number:"))    #This asks the user to input a number and casts it to an integer
    print("You guessed", y)
    if y > x:
        print("your guess was too large.")
        trial += 1
    elif y<x:
        print("your guess was too small.")
        trial+=1
    else:
        print("you guessed the number! you win!")
        trial+= 1
        break
    if trial >4:
        print("GAME OVER")



'''8) Using for loops and conditionals, print out all of the prime numbers between 5 and 25. 
Remember that a prime number is a number only divisible by 1 and itself. 
You will likely find the modulo (%) operator very useful. Have a think about how to make your code more 
efficient (Hint: think about using range function with a different step). '''

primes=[]
for i in range(5,25,2):
    if i <2:
        continue
    if i :
        loopbreak = False
        for num in range(2,i):
            if i%num==0:
                loopbreak = True
                break

        if not loopbreak:
            # we found a prime number
            primes.append(i)