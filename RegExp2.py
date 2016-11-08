import re

# Read in the file
filename = raw_input("Enter name of file: ") 

if filename == '':
    filename = 'mbox.txt'

handle = open(filename)

# Setting up variables for averaging.
sum = 0
count = 0   

regExp = "^New .+: ([0-9.]+)"

for line in handle:
    line = line.rstrip()
    num = re.findall(regExp, line) # Identify content that finds all numeric text after the colon on lines that start with "New"
    print num
    if len(num) > 0:   
        num = float(num) #Recast value from text to a float.
        sum += num
        count += 1
    else:
        continue
    
print "Count of matching cases: ", count
print "Average: ", sum / count