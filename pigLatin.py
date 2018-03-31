#Ask user for sentence
original = input("Enter a sentence to be translated into pig latin: ").strip().lower()
#Split sentence into words
words = original.split()

#Loop through words and convert to pig latin
new_words = []
 
for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"   
        new_words.append(new_word)     
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou": #if starts with vowel add "yay"
                vowel_pos = vowel_pos + 1
            else: #Otherwise move the first consonant cluster to end, and "ay"
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word) 

output = " ".join(new_words)   #Put those words back into sentence

print(output) #Output the final string