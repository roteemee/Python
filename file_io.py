myfile = open("fruits.txt") #creates the file in memory
content = myfile.read()
myfile.close() #closes the file from memory
print(content)