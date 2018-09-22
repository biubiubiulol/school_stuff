import sys

fileName = int(sys.argv[1])
file = open(fileName, “r”) 
print file.read() 