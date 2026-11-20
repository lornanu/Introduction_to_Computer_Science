


'''1. Below are two functions that solve problems that we have seen previously. They are different methods by which we can generate lists of prime numbers. 
Use the timing and profiling magic functions to determine how these algorithms scale as you change the size of the input. 
You could try doubling the value of maxPrime repeatedly and see how that impacts the data that is output. 
There is printing code commented out - you can uncomment this to prove the algorithms work, but for profiling it is best if these are commented.'''

# Add the timing and profiling magic functions wherever you think appropriate
import timeit
def primeFunctionA(max):
    for i in range(3,max,2):
        prime = True
        for j in range (3,i,2):
            if i%j == 0:
                prime = False
                break
        #if prime:
           #print(i, end = ', ')
        
def primeFunctionB(max):
    L = [True] * ((max//2)-1)
    counter = 3
    for i in range(len(L)):
        if L[i]:
            for j in range(counter,len(L),counter):
                if i+j < len(L):
                    L[i+j] = False
        counter += 2

    #for i in range(len(L)):
        #if L[i]:
           #print(3+2*i, end = ', ')
    
maxPrime = 100
'''NOTE: Jupyter notebook specific code below.'''
#%timeit primeFunctionA(maxPrime) 

#%timeit primeFunctionB(maxPrime)

#13.5 μs ± 255 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)
#4.17 μs ± 11.6 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)


'''2. Use your knowledge of the random module to generate a list of random integers called `L`. You should be able to control the size of this list with a 
variable. Make a copy of your list using the copy module, and call it `L1`, so you have two independant copies of that list. 
Vary the size of your list using the variable you assigned for this purpose, and see how the performance of these functions scale as you change that 
size of the input list. You might notice some interesting differences between using quite small lists (under 200 elements) and larger lists (over 1000 elements).'''

import numpy as np
import random

def pySort(L):
    L.sort()

    
def npSort(arr):
    np.sort(arr)
    
    
#----------------------------------------------------------------------------------------
# Define L and L1, and add any imports you need to the top of the codeblock
# Put your timing magic functions wherever seems most appropriate 
L=[5,1,2,43,6,7,8,6,4,3,2314]
L1=L.copy()
L= [random.randint(0,100)]

#----------------------------------------------------------------------------------------    
'''NOTE: Jupyter notebook specific code below.'''
#%timeit pySort(L)
arr = np.asarray(L1)
#%timeit npSort(arr)

#36.9 ns ± 0.0653 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
#792 ns ± 1.71 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)


'''3. Using the string manipulation techniques seen in notebook 6.3, design a game of hangman. You should assign a string to a variable, 
and then blank out the letters in some way. Request a user to guess the letters and update the string on display to the user with every guess 
they make. This will test quite a few techniques that we have used previously! If you've done a lot of Python before and want to try drawing a 
hangman to go along with the guessing part feel free to do so.
'''

import random
wordlist= ["apple", "banana", "orange", "strawberry", "pineapple", "watermelon",
    "chocolate", "pizza", "burger", "sandwich", "pancake", "spaghetti",
    "dog", "cat", "elephant", "giraffe", "penguin", "dolphin", "tiger",
    "butterfly", "kangaroo", "crocodile", "flamingo", "squirrel",
    "house", "kitchen", "bedroom", "garden", "window", "blanket",
    "mirror", "umbrella", "backpack", "bicycle", "airplane", "submarine",
    "guitar", "piano", "camera", "computer", "telephone", "television",
    "mountain", "ocean", "forest", "desert", "shamrock", "island", "volcano",
    "rainbow", "thunder", "snowflake", "sunshine", "tornado", "hurricane",
    "doctor", "teacher", "firefighter", "astronaut", "pirate", "vampire",
    "wizard", "dragon", "unicorn", "mermaid", "zombie", "ghost",
    "football", "basketball", "tennis", "swimming", "skateboard", "bowling",
    "birthday", "holiday", "adventure", "mystery", "treasure", "secret",
    "shadow", "whisper", "laughter", "memory", "promise", "journey",
    "diamond", "emerald", "crystal", "lantern", "compass", "anchor",
    "castle", "bridge", "museum", "library", "hospital", "stadium",
    "penguin", "octagon", "pyramid", "skeleton", "dinosaur", "nintendo", "rocket", "pokemon"]
goal = random.choice(wordlist)
def hangman(word):
    score = 10 #starting score
    hiddenword=word #temp copy
    for c in word:
        hiddenword = hiddenword.replace(c, "-") #censoring the real word
    print(hiddenword)
    while score > 0:
            Guess = input(str("Guess a letter in lowercase: "))
            if len(Guess) != 1:
                print("Please only submit one character.")
                continue
            if Guess in word:
                print("Yes! This letter is in the word.")
                for c in range(len(word)):
                    if word[c] == Guess:
                        hiddenword= hiddenword[:c] + Guess +hiddenword[c+1:] #slicing so we can change the - into the letter
                print(hiddenword)
                if "-" not in hiddenword: #if there is no - in the word then that means all the letters have been found
                    print(f"You win! The word was {goal}.")
                    break
            else:
                score = score - 1
                print("Wrong! Try again. Your score is now " + str(score)+ ".")
            if score == 0:
                print(f"You ran out of points! You lose. The word was {goal}.")

hangman(goal)

'''4. Design a simple substitution cipher using string manipulation. There are lots of ways to tackle this problem. 
An easy way to start might be to say that all plaintext messages are in capital letters, and encrypted text is in lower case.''' 

#A = Z, B=Y etc
alphabet="abcdefghijklmnopqrstuvwxyz"
backwards="zyxwvutsrqponmlkjihgfedcba"

def cipher(word):
    cipherword = ""
    for c in word:
        if c.isupper():
            cipherword = cipherword + backwards[alphabet.index(c.lower())]
            cipherword= cipherword[-1].upper()
        elif c in alphabet:
            cipherword = cipherword + backwards[alphabet.index(c)]
        
        else:
            cipherword = cipherword + c
    print(cipherword)

cipher("Hello world")
cipher("text here")

#Svool dliow
#gvcg sviv


'''5. Using regular expressions, try to identify all of the emails in the file *emails.txt* that could be valid Durham University email addresses. 
Valid addresses can end with either *@UNI1.ac.uk* or *@UNI2.ac.uk*. They may start with `<forename>.<surname>` or `<forename>.<initial>.<surname>` or 
`<initial>.<initial>.<surname>` or `<username>`. You can use any many regular expressions as you like, but maybe try to see how few you can manage this in. '''

import re
infile = open("emails.txt")
email= infile.read()
emailuni = re.compile(r'[a-z0-9]+(?:\.[a-z])?(?:\.[a-z]+)?@uni(?:versity)?\.ac\.uk')
print(emailuni.findall(email))