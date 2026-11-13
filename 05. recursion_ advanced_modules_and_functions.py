'''1. Take your code from the fourth exercise from the previous topic which calculates the hypotenuse of a right angled triangle. Modify this function such that is has default arguments with the values 3 and 4. Try calling your function without any providing any arguments, and make sure you get the answer you would expect.'''

##
import math
def pythagoras(a=3,b=4):
    c = math.sqrt(a**2+b**2)
    return round(c,2)

pythagoras() #5.0
pythagoras(10,5) #11.18


'''2. Write a recursive function to calculate the factorial of a given input number `n`. As a reminder `4! = 4 * 3 * 2 * 1` for example, so should return `24`. To help with your recursive function, it is worth remembering that `n! = n * (n-1)!'''
## 
def recursivef(n):
    if (n ==1 or n==0):
        return 1  
    elif n <0:
        print("number is less than 0")
    else:
        return (n * recursivef(n-1))

recursivef(10)




'''3. Explore how the copy and deepcopy functions work with a variety of the data structures that we saw in Topic 2. 
Lists, tuples, dictionaries and sets are all collection types, they can store other objects, including other collection types. 
We saw this in the content in notebook 5.2 looking at lists and lists of lists. 
Create examples of your own where you try to copy and edit these data structures. 
Make sure to consider compound data structures - we saw lists of lists in the content, so try for example copying and editing a tuple of lists, 
or a set of tuples.'''
import copy
a= [[2,4],[7,9]]
b = copy.copy(a)
c=copy.deepcopy(a)
a[0][0]=100
print(b)
print(c)

#normal copy cannot adjust the inner list


tuplelist = ([1,2,3],[4,5,6])

tuple_copy = copy.copy(tuplelist)
tuple_deepcopy = copy.deepcopy(tuplelist)
tuplelist = ([1,2,3,4,5], [4,5,6])
print(tuple_copy)
print(tuplelist)

setoftuples = {(5,6), (12, 20)}
setcopy = copy.copy(setoftuples)
setdeepcopy = copy.deepcopy(setoftuples)
setoftuples = {(5,6,7),(12,20)}

print(setcopy)
print(setdeepcopy)
#neither changed because tuples are immutable


'''4. Write a function that continually asks a user for a filename until they provide a valid filename. 
If the filename the user provides is invalid you should print out a message to indicate this, and then request another filename. 
If the filename is valid then you should read in the file and print out its contents. 
You should use the `try` and `except` structure, and will probably need a `while` loop.'''


def fileopen():
    checker = False
    infile = None
    while checker == False:
        try:
            filename = input("Please enter a file name: ")
            infile = open(filename)
        except:
            print("Failed to open file. Please try again.")
        else:    
            print(infile.readline())
            print("File opened successfully.")
            checker = True
        finally:
            if infile is not None: 
                infile.close()
        

fileopen() #test.txt is the only working txt in the directory


'''5. There is a file containing words in the files folder called `dict.txt`. Write Python code that reads this file, checks through all of the words
 in the file, and identifies which words have 4 letters of more. Create a new file and write to it just those words that contain 4 letters or more.'''

####
infile = open("files/dict.txt") 
newfile=open("fourletters", "w") #create new blank file for the 4+ letter words
fourletters = infile.readlines() #read original doc 
for word in fourletters:
    if len(word) >= 5: #5 because the new paragraph counts as a character 
        newfile.write(word)
infile.close()
newfile.close()
