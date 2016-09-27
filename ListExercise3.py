# Rewrite the program that prompts the user for a list of numbers
# and prints out the maximum and minimum of the numbers at the end when the user enters done. 
# Write the program to store the numbers the user enters in a list 
# and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.


#Create list
numList = list()

#Run the loop indefinitely until there is a break.
while True:
    num = raw_input('Please enter a number or "done": ')
    if num == 'done':
        break
    try:
        num = int(num)
        numList.append(num)
    except:
        continue

# Print the max and min, unless the list is empty.
try:        
    print 'Smallest value: ', min(numList)
    print 'Largest value: ', max(numList)
except:
    print 'Error: empty list.'