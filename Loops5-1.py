# Write a program which repeatedly reads numbers until the user enters
# done. Once done is entered, print out the total, count, and average of
# the numbers. If the user enters anything other than a number, detect their mistake
# using try and except and print an error message and skip to the next number.

# Initialize variables to be updated during loop

count = 0
total = 0
inputString = ''

# Check to make sure input can be converted into an integer
# Update total and count variables as needed
# Otherwise, prompt again.

while inputString != 'done':
    inputString = raw_input("Please enter any number or 'done': ")
    if inputString == 'done':
        break
    try:
        inputNum = int(inputString)
        total += inputNum # Same as total = total + inputNum
        count += 1
    except:
        print 'Invalid input.'

average = float(total/count)

print 'Total: ', total, '\nCount: ', count, '\nAvg.: ', average"# Coding-Exercises" 
