import random
import math
wordDictionary = {}
messageLength = 1
lengthCounter = 1

def inputsetup():
    global mInput, eInput, wordDictionary
    counter = 0
    word = ""
    mInput = input("Message: ")
    eInput = input("Emotion (Positive(P), Bad(B), Neutral(N)): ")
    if eInput.lower() == "p":
        #make good associations for each individual word
        for i in mInput:
            counter += 1
            if i != " ":
                word += i
                if counter == len(mInput):
                    if word in wordDictionary:
                        if wordDictionary[word] + 2 > 100:
                            pass
                            word = ""
                        else:
                            wordDictionary[word] += 2
                            word = ""
                    else:
                        wordDictionary[word] = 65
                        word = ""

            elif word in wordDictionary:
                if wordDictionary[word] + 2 > 100:
                    pass
                    word = ""
                else:
                    wordDictionary[word] += 2
                    word = ""
            else:
                wordDictionary[word] = 65
                word = ""

    elif eInput.lower() == "b":
        #make bad associations for each individual word
        for i in mInput:
            counter += 1
            if i != " ":
                word += i
                if counter == len(mInput):
                    if word in wordDictionary:
                        if wordDictionary[word] - 2 < 0:
                            pass
                            word = ""
                        else:
                            wordDictionary[word] -= 2
                            word = ""
                    else:
                        wordDictionary[word] = 35
                        word = ""

            elif word in wordDictionary:
                if wordDictionary[word] - 2 < 0:
                    pass
                    word = ""
                else:
                    wordDictionary[word] -= 2
                    word = ""
            else:
                wordDictionary[word] = 35
                word = ""

    elif eInput.lower() == "n":
        #make neutral association for each word
        for i in mInput:
            counter += 1
            if i != " ":
                word += i
                if counter == len(mInput):
                    if word in wordDictionary:
                        if wordDictionary[word] > 50:
                            wordDictionary[word] -= 2
                            word = ""
                        elif wordDictionary[word] < 50:
                            wordDictionary[word] += 2
                            word = ""
                        else:
                            pass
                            word = ""

                    else:
                        wordDictionary[word] = 50
                        word = ""

            elif word in wordDictionary:
                if wordDictionary[word] > 50:
                    wordDictionary[word] -= 2
                    word = ""
                elif wordDictionary[word] < 50:
                    wordDictionary[word] += 2
                    word = ""
                else:
                    pass
                    word = ""
            else:
                wordDictionary[word] = 50
                word = ""

def doInput():
    inputsetup()
    while eInput.lower() != "b" and eInput.lower() != "p" and eInput.lower() != "n":
        print("Follow the instructions, please.")
        inputsetup()

def AIresponse():
    global alphaFrom, alphaSend, mInput, messageLength, lengthCounter
    AItext = ""
    #tone = 0
    if lengthCounter <= 5:
        lengthCounter += 1
    elif lengthCounter > 5 and lengthCounter <= 10:
        messageLength = 3
        lengthCounter += 1
    elif lengthCounter > 10:
        messageLength = 6

    toneList = []
    tone = 0
    #make message here
    for j in range(1,messageLength+1):
        totalWeights = 0
        counter = -1
        for i in list(wordDictionary):
            totalWeights += wordDictionary[i]
        randomNum = random.choice(range(0,totalWeights))
        while randomNum > 0:
            counter += 1
            randomNum -= wordDictionary[list(wordDictionary)[counter]]
        
        AItext += list(wordDictionary)[counter]
        toneList.append(wordDictionary[list(wordDictionary)[counter]])
        
        if j != messageLength:
            AItext += " "
    
    #get tone from toneList (its just the average of all the items in the list)
    for i in toneList:
        tone += int(i)
    tone = round(tone/len(toneList))
    #print(wordDictionary)
    #10 = neutral, 20 = positive, 0 = negative <----- for AI tone
    return print("AI message: " + AItext + "."), print("AI tone: " + str(tone))

while True:
    #get input
    doInput()
    #get reponse
    AIresponse()