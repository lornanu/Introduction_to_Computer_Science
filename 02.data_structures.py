
'''1) Define S to be the string "abcdefgh". Write expressions using S and the index operator to return the following strings:
a) "a"
b) "c"
c) "e" '''

#YOUR CODE GOES HERE
S= "abcdefgh"
a= S[0]
b= S[2]
c= S[4]
print(a,b,c)

#a c e


'2) Using the same string S, this time return a sublist that spells out the word "ace". You should be able to do this with a single line of code using the indexing operator.''' 

#YOUR CODE GOES HERE
ace_list = [a,b,c]


'''3) In the code block below we have defined L to be a list of prices for a new CPU that I would like to buy.

a) Print out the minimum and maximum prices without sorting the list first.'''


L = [199.99, 219.99, 220.00, 222.99, 195.99, 210.00]

#YOUR CODE GOES HERE
print(min(L), max(L))
#195.99 222.99


'''b) Use the built-in sort function to sort the list, and print out the minimum and maximum price using the indexing operator.'''

#YOUR CODE GOES HERE
L.sort()
print(L[0],L[-1])
#195.99 222.99


'''4) Using the built-in len function, and the boolean operators we saw in the previous topic, check if the two strings given in the code block have the same length. 
Print `True` if they do and `False` otherwise.'''

x = "Hello"
y = "Goodbye"

#YOUR CODE GOES HERE
len(x)==len(y)
#False



'''5) Given the list in the code block below, calculate the sum of all of the elements, except for the largest and smallest elements. 
There are multiple ways to solve this problem, try to make your code succinct. '''

L = [9,5,7,10,6,8,1,3,2,4]

#YOUR CODE GOES HERE
sum(L)
# 55



'''6) Given the matrix (list of lists) in the code block below, try to calculate the following and return your answers as a list:

a) Row Sums'''
L = [[0,1,2],[3,4,5],[6,7,8]]

#YOUR CODE GOES HERE
row_sum = [L[0][0] + L[1][0] + L[2][0],L[0][1] + L[1][1] + L[2][1], L[0][2] + L[1][2] + L[2][2]]
print("the sum of rows are:", row_sum)


'''b) Column Sums'''
col_sum = [sum(L[0]),sum(L[1]),sum(L[2])]
print("the sum of columns are:", col_sum)

#YOUR CODE GOES HERE

'''7) Check if the element "E" exists in the tuple defined below:'''

T = ("A", "e", "I", "O", "U")

#YOUR CODE GOES HERE
print("E" in T)


'''8) Replace the element "e" with the element "E" in the data structure below:'''


T = (["A", "e", "I", "O", "U"],["B","C"])

#YOUR CODE GOES HERE
T[0][1] = "E"
print(T)

'''9) Using the dictionary defined below, calculate the total population of all of the settlements. 
Then add a new key-value pair to the dictionary with the key "County X", and the value being that total population. '''

D = {
    "CITY 1" : 92363,
    "CITY 2" : 88855,
    "CITY 3" : 82729,
    "CITY 4" : 47785,
    "CITY 5" : 35392
}

#YOUR CODE GOES HERE
total_pop = sum(D.values())
print(total_pop)

D["County X"] = total_pop
print(D)


'''10) Using the sets defined in the code block below, work out which set operator to use to answer the following questions:

a) The set of odd numbers that are not prime.'''


odd = {1,3,5,7,9,11,13,15,17,19,21,23,25}
even = {2,4,6,8,10,12,14,16,18,20,22,24}
prime = {2,3,5,7,11,13,17,19,23}

#YOUR CODE GOES HERE
odd.difference(prime)
#{1, 9, 15, 21, 25}



'''b) The set of prime numbers that are not odd (try to find multiple ways in which to do this).'''

#YOUR CODE GOES HERE
prime.difference(odd)
prime.intersection(even)
#{2}



'''c) All of the numbers between 1 and 25 that are not prime.'''

#YOUR CODE GOES HERE
odd.union(even).difference(prime)
#{1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25}


