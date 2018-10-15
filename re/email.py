import re

mString = "Send Send an email from this@email to test@user.com, 34 times"


"""
^Start
$Stop
. Any character
* Match one character 0+ times
+ Match one character 1+ times
? Non-greedy
\s Whitespace
\S Non-whitespace
[abc] match one character in the specified set
[^abc] Match one character not in the specified set]
"""
#Anything the starts with 'Send'
send = re.findall('^Send', mString)

#Plus sign at the end signifies grouped words, vs w/o single char
result1 = re.findall('[a-z]+', mString)

#Anything but lowercase words
result2 = re.findall('[^a-z]+', mString)

#Returns anything that isn't a whitespace
result3 = re.findall('\S+', mString)

#Gets all emails from string
#All nonwhitespace + @ until the next nonwhite space
result4 = re.findall('\S+@\S+', mString)


print(result4)