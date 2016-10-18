# Revise a previous program as follows: Read and parse the From
# lines and pull out the addresses from the line. Count the number of messages from
# each person using a dictionary.
# After all the data has been read, print the person with the most commits by creating
# a list of (count, email) tuples from the dictionary. Then sort the list in reverse order
# and print out the person who has the most commits.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox.txt"
handle = open(name)

freqDict = dict()

for line in handle:
    if not line.startswith('From '):
        continue
    else:
    # Split the line, pull the email, and track its frequency using .get()
        words = line.split()
        email = words[1]
        freqDict[email] = freqDict.get(email,0) + 1

print freqDict

# Create a list so that a tuple shows (freq, email).
freqLst = list()

for key, val in freqDict.items():
    freqLst.append( (val, key) )

freqLst.sort(reverse=True)

for freq, email in freqLst:
    print freq, email
