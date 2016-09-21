# Write a program to prompt for a file name, and then read through
# the file and look for lines of the form:
# X-DSPAM-Confidence:

#Get filename, open the file
inputFile = raw_input("Enter filename: ")
if inputFile == "":
    inputFile = 'mbox-short.txt'
handle = open(inputFile)

#Initialize values
count = 0
total = 0

#Read lines for X-DSPAM-Confidence values
for line in handle:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        print line
        startPos = line.find(':') # Find where the colon is
        num = line[(startPos + 2):] # Start two characters to the right of the colon.  Assign everything to the right of that to num.
        num = float(num) # Convert to a floating variable
        print num
        
        total += num # Update total
        count += 1 # Update count
    else:
        continue
        
print 'Count ', count
print 'Total ', total
print 'Average: ', (total / count)
