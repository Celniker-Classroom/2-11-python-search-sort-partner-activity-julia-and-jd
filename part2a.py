#write your python code here
from random import randint #This line imports the randint function from the random module. The randint function generates a random integer between two specified values


randomList = [] #name your list and make sure it is empty!


# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
for number in range(10): #for loop appends 5 numbers to your list, but make sure you name your variable
    randomList.append(randint(1,50)) #this adds a random number between 1-50 to the list

print(f"the list is {randomList}") #print the list!

searchNumber = randint(1, 20)

print(f"Searching for number {searchNumber} in the list")
if searchNumber in randomList:
    print("Number", searchNumber,"found in the list!")
else:
    print("Number", searchNumber,"not found in the list.")



