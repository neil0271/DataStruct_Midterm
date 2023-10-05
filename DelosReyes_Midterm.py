#Algorithmn and Psuedocode
'''
Step 1: Make a 2D array
Step 2: Input the elements inside the 3x3 array that you have made
Step 3: Make a variable that holds the value of the maximum number of the elements of the array
Step 4: Intialize the data type and class of the variable used to hold maximum element
Step 5: Use a loop to access each elements in the array and iterates by comparing the current element and the latest highest elements as of the moment
Step 6: Use a condtitional statement inside the loop which test each elements of the array and after reaching the last element it will then proceed to finalize the largetst element
Step 7: Print the maximum element in the array


Psuedocode
Start
Define a 3x3 array named "array"
Input the values of elements inside the array 

    [1, 2, 3],

    [4, 5, 6],

    [7, 9, 9]

let MaxElement be a float('inf') that indicates positive infinity
initialize this variable to the minumum possible integer value

for each "row" in "array":
    for each element in "row":
        if "element" is greater than "MaxElement":
            Set the "MaxElement" to the value of "element"

Print ("Maximum element: " use the variable MaxElement that holds the maximum element in the array)

End

'''




array = [
    [1, 2, 3],

    [4, 5, 6],

    [7, 8, 9]
]

MaxElement = float('-inf') 

for row in array:

    for element in row:

        if element > MaxElement:

            MaxElement = element
print("Maximum element:", MaxElement)