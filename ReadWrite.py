file = open("Text")
#print(file.read())   #print the file

#print("************")

#print(file.read(7))    #how many characters to be printed from text file

#print(file.readline())
#print(file.readline())

#line = file.readline()     #reading line
#while line!="":            #checking whether line = not empty goes to next line
 #   print(line)            #print the line
  #  line = file.readline() #read the another line and the loop continues till line gets empty

#print(file.readlines())   #it will store values in list form

for x in file.readlines():
    print(x)

