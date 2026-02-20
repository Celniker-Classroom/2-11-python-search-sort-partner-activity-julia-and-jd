#write your python code here
import statistics as stc
from random import randint #This line imports the randint function from the random module. The randint function generates a random integer between two specified values

randomList = [] #name your list and make sure it is empty!
randomList2forFun = []

# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
for number in range(10): #for loop appends 5 numbers to your list, but make sure you name your variable
    randomList.append(randint(1,50)) #this adds a random number between 1-50 to the list
for number in range(10): #for loop appends 5 numbers to your list, but make sure you name your variable
    randomList2forFun.append(randint(1,50)) #this adds a random number between 1-50 to the list

searchNumber = int(input("Write a number from 1-50 to search for in the first list: "))

print(f"the first list is {randomList}") #print the list!
print(f"the second list is {randomList2forFun}")
partThreeFunUserAdding = int(input("Give me a number to add to your first list that is NOT the number you are searching for: "))

randomList.append(partThreeFunUserAdding)
print(f"the first list is {randomList}") #print the list!

print(f"Searching for number {searchNumber} in the first list")

comparisons = 0  # Initialize the counter for comparisons
found = False  # Variable to track if the number was found

for number in randomList:  # Name your variable in the for loop
    comparisons += 1  # Increment the counter for each comparison
    if number == searchNumber:
        found = True  # Set found to True if the number is in the list
        break  # Exit the loop early if the number is found

if found == True:
    print(f"The number, {searchNumber} has been found after {comparisons} comparisons")
else:
    print(f"The number, {searchNumber} has not been found after {comparisons} comparisons")

print(f"the smallest number in the list is {min(randomList)}")
print(f"the largest number in the list is {max(randomList)}")

numberSum = 0
for index in range(len(randomList)):
    numberSum += randomList[index]
print(f"the sum of the numbers in the first list is {numberSum}")



randomList.sort()
print(f"The first list sorted is {randomList}")


medianList = stc.median(randomList)
print(f"The median of the sorted list is {medianList}")

randomList2forFun.extend(randomList)
print(f"The first list added to the second list is {randomList2forFun}")