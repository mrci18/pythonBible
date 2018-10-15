import re
text = open('shakespeare.txt')

for line in text:
    line = line.rstrip()
    #Match Anything starting with A
    #Match anything
    #One or more or else it would have just matched one character
    #Till the end
    if re.search('^A.+$', line):
        print(line)

    #Finds characters starting with 'T'
    #Matches any multiple characters
    #Finds lowercase t
    #Matches any multiple characters
    #Finds a comma and ends
    if re.search('^T.+t.+,$', line):
        print(line)

    #Finds a line with capital A with the word again
    if re.search('^A.+again.$', line):
        print(line)

    #Finds any words that start with capital
    #How many times we want that character to be found(3 or more times in this case)
    if re.search('^[A-Z]{3,6}$', line):
        print(line)