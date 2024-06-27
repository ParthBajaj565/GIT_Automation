#read the file and store all the lines in the list
#reverse the list
#write the list back to the file

with open('Text', 'r') as reader:      #file named text opened in read mode
    content = reader.readlines()       #text coverted into list format
    reversed(content)                  #List got reversed
    with open('Text', 'w') as writer:  #file named text opened in write mode
        for line in reversed(content): #content under the file got out from the list
            writer.write(line)         #line by line content got written