def reverse(text):
    list = []
    for x in range(len(text)):
        list.insert(0, text[x])
    retValue = ""
    for a in list:
        retValue += a
    return retValue
print ("Disclaimer: 0 to exit")
keepGoing = True
while (keepGoing == True):
    word = input("Enter a word you would like to reverse: ")
    if word == "0":
        keepGoing = False
    else:
        print (reverse(word))