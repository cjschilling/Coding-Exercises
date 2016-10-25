import re

grepString = raw_input("Enter a regular expression: ")
handle = open('mbox-short.txt')

for line in handle:
    lst = re.findall(grepString, line)

print len(lst), 'lines matched the regular expression in the file.'