#Write a program that categorizes each mail message by which day of the week the commit was done. 
#To do this look for lines that start with 'From', 
#then look for the third word and keep a running count of each of the days of the week. 
#At the end of the program print out the contents of your dictionary (order does not matter).

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

topName = 0
topCount = 0

dayDict = dict()
for line in handle:
    if not line.startswith('From '):
        continue
    else:
        words = line.split()
        for word in words[2]:
            day = words[2]
            dayDict[day] = dayDict.get(day,0) + 1

print dayDict.items()