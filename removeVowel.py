def anti_vowel(text):
    list = []
    retValue = ""
    for x in range(len(text)):
        list.append(text[x])
    for letter in list:
        if letter == "A" or letter == "O" or letter == "E" or letter == "U" or letter == "I" or letter == "a" or letter == "o" or letter == "e" or letter == "u" or letter == "i":
            list.remove(letter)
    for letter in list:
        retValue += letter
    return retValue
print ("Disclaimer: 0 to exit")
keepGoing = True
while (keepGoing == True):
    word = input("Enter a word you would like to purge: ")
    if word == "0":
        keepGoing = False
    else:
        print (anti_vowel(word))