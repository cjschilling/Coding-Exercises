# Change the socket program socket1.py to prompt the user for the
# URL so it can read any web page. You can use split(/) to break the URL into
# its component parts so you can extract the host name for the socket connect call.
# Add error checking using try and except to handle the condition where the user
# enters an improperly formatted or non-existent URL.

import urllib
import re

# Get the URL and check to make sure it is valid

inputURL = raw_input('Enter valid URL beginning with "http://": ')

try:
    html = urllib.urlopen(inputURL).read()
except:
    print "Invalid URL."
    quit()
    
# Get and print host name using split to extract it.

urlParts = inputURL.split('/')
hostname = urlParts[2]

print hostname,', '

# Retrieve contents of URL using URLlib

print 'HTML contents:'
print html

# Make a socket connect call to the input URL 
# Note: this hasn't worked becuase cmd and GET are dumb
# and won't let us put in variables.

#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect((hostname, 80))
#cmd = 'GET inputURL HTTP/1.0\n\n'
#print cmd
#mysock.send(cmd)

#while True:
    #data = mysock.recv(512)
   # if (len(data) < 1):
  #      break
 #   print(data.decode())
#mysock.close()
