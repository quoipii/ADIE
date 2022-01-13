#~2.5 years WITH BRAIN DAMAGE. Simple emotions but getting more complex. 3 years will have more in-depth emotions.
import random
import os
firstTime = 1


open("wordList.txt","w").close()
#Words are formatted as [WORD]
open("calls.txt","w").close()
#Calls are formatted as [MESSAGE] [KEY] [ID] || to be added ---> [MEMORY] [EMOTIONAL SCORE] <-- unhappy eScore would mean unhappy responses as replies to this and vice versa
open("responses.txt","w").close()
#Responses are formatted as [MESSAGE] [KEY] [EMOTE] [ID] || to be added ---> [MEMORY] [EMOTIONAL SCORE] <-- unhappy eScore would mean it is an unhappy response and vice versa

def keyGen():
    global key
    key = ""
    for i in range(1,9):
        key += str(random.choice(range(1,9)))
    return print("Your key is " + key)

def train():    
    global idCount
    convMsg = input(": ")
    msgEmote = input("emotion (-10 - 10): ")
    idCount = 1
    stop = 0

    if convMsg == key:
        pass
    else:
        callList = open("calls.txt","a")
        callList.write(convMsg+" "+key+" "+str(50+int(msgEmote))+" "+str(idCount)+"\n")
        callList.close()
        #if the file is empty write the first word in
        if os.stat("wordList.txt").st_size == 0:
            for word in convMsg.split(" "):
                if stop == 0:
                    wordListA = open("wordList.txt","a")
                    wordListA.write(word + "\n")
                    wordListA.close()
                    stop = 1
                else:
                    pass
        #get all da new words and no double ups
        wordListR = open("wordList.txt","r")
        for line in wordListR.readlines():
            for word in line.split(" "):
                for msgWord in convMsg.split(" ")[1:]:
                    #print("comparing: " + msgWord + " " + word)
                    if word.lower().strip() == msgWord.lower():
                        pass
                        #print(word + " and " + msgWord + " are the same.")
                    else:
                        #print(word + " and " + msgWord + " are different.")                        
                        wordListR.close()
                        wordListA = open("wordList.txt","a")
                        wordListA.write(msgWord + "\n")
                        wordListA.close()
                        wordListR = open("wordList.txt","r")
        wordListR.close()
    
    while convMsg != str(key):
        convMsg = input(": ")
        if convMsg == str(key):
            callListR = open("calls.txt","r")
            entireCallFile = callListR.readlines()
            callListR.close()
            callListW = open("calls.txt","w")
            for line in entireCallFile[0:-1]:
                callListW.write(line)
        else:
            msgEmote = input("emotion (-10 - 10): ")
            #check if this has been said before in order to change emotion score if so
            callListR = open("calls.txt","r")
            entireCallFile = callListR.readlines()
            callListR.close()
            respListR = open("responses.txt","r")
            entireRespFile = respListR.readlines()
            respListR.close()
            respListR = open("responses.txt","r")
            callListR = open("calls.txt","r")
            callRepeat = 0
            respRepeat = 0
            targetCallLine = ""
            targetRespLine = ""

            for line in callListR.readlines():
                #print(line.split(" "))
                if line.split(" ")[0:-3] == convMsg.split(" "):
                    callRepeat = 1
                    #print("the same")
                    #targetLine is set to the lines ID
                    targetCallLine = line.split(" ")[-1]
                    callListW = open("calls.txt","w") 
                else:
                    pass

            for line in respListR.readlines():
                #print(line.split(" "))
                if line.split(" ")[0:-3] == convMsg.split(" "):
                    respRepeat = 1
                    #print("the same")
                    #targetLine is set to the lines ID
                    targetRespLine = line.split(" ")[-1]
                    respListW = open("responses.txt","w") 
                else:
                    pass

            callListR.close()
            respListR.close()

            if callRepeat == 1:
                for line in entireCallFile:
                    if line.split(" ")[-1] == targetCallLine:
                        if int(line.split(" ")[-2]) + int(msgEmote) < 1 or int(line.split(" ")[-2]) + int(msgEmote) > 100:
                            callListW.write(line)
                            #print(f"wrote {line}")
                        else:
                            newEmote = int(line.split(" ")[-2]) + int(msgEmote)
                            lineList = line.split(" ")
                            lineList[-2] = str(newEmote)
                            newLine = ""
                            for item in lineList:
                                newLine += item + " "
                            newLine = newLine[0:-1]
                            callListW.write(newLine)
                            #print(f"wrote {line}")
                    else:
                        callListW.write(line)
                        #print(f"wrote {line}")
                callListW.close()
            
            if respRepeat == 1:
                for line in entireRespFile:
                    if line.split(" ")[-1] == targetRespLine:
                        if int(line.split(" ")[-2]) + int(msgEmote) < 1 or int(line.split(" ")[-2]) + int(msgEmote) > 100:
                            respListW.write(line)
                            #print(f"wrote {line}")
                        else:
                            newEmote = int(line.split(" ")[-2]) + int(msgEmote)
                            lineList = line.split(" ")
                            lineList[-2] = str(newEmote)
                            newLine = ""
                            for item in lineList:
                                newLine += item + " "
                            newLine = newLine[0:-1]
                            respListW.write(newLine)
                            #print(f"wrote {line}")
                    else:
                        respListW.write(line)
                        #print(f"wrote {line}")
                respListW.close()
            
            else:
                respListA = open("responses.txt","a")
                callListA = open("calls.txt","a")
                idCount += 1
                callListA.write(convMsg+" "+key+" "+str(50 + int(msgEmote))+" "+str(idCount)+"\n")
                respListA.write(convMsg+" "+key+" "+str(50 + int(msgEmote))+" "+str(idCount-1)+"\n")
                respListA.close()
                callListA.close()
            

            killme = 0 #variable thats just another counting thing. its here to make sure if a word is in the wordlist, it doesnt keep comparing it
            for msgWord in convMsg.split(" "):
                wordListR = open("wordList.txt","r")
                killme = 0
                for word in wordListR.readlines():
                    #print("comparing: " + msgWord + " and " + word)
                    if word.lower().strip() == msgWord.lower().strip():
                        #print(word.lower().strip() + " and " + msgWord.lower().strip() + " are the same.")
                        killme = 1
                        #print("killme has been set to 1")
                        #print(msgWord.lower().strip() + " is already known.")
                    else:
                        pass
                        #print(word.lower().strip() + " and " + msgWord.lower().strip() + " are different.")                     

                #print(f"killme: {killme}")
                if killme == 1:
                    pass
                else:
                    wordListR.close()
                    wordListA = open("wordList.txt","a")
                    wordListA.write(msgWord + "\n")
                    wordListA.close()
                    #wordListR = open("wordList.txt","r")
                #print("killme has been reset to 0.")
                
            wordListR.close()

def percentCalc(similarity, wordList1, wordList2):
    similarity += round((1/max(len(wordList1),len(wordList2)))*100)
    return similarity

def talk():
    global key, idCount, firstTime
    message = input("Your message: ")
    msgEmote = input("emotion (-10 - 10): ")
    similarLines = []
    words = message.split(" ")
    bottomPercent = 75
    wordRange = 2

    #Gets new words
    for msgWord in message.split(" "):
        wordListR = open("wordList.txt","r")
        killme = 0
        for word in wordListR.readlines():
            #print("comparing: " + msgWord + " and " + word)
            if word.lower().strip() == msgWord.lower().strip():
                #print(word.lower().strip() + " and " + msgWord.lower().strip() + " are the same.")
                killme = 1
                #print("killme has been set to 1")
                #print(msgWord.lower().strip() + " is already known.")
            else:
                pass
                #print(word.lower().strip() + " and " + msgWord.lower().strip() + " are different.")                    
        #print(f"killme: {killme}")
        if killme == 1:
            pass
        else:
            wordListR.close()
            wordListA = open("wordList.txt","a")
            wordListA.write(msgWord + "\n")
            wordListA.close()
            #wordListR = open("wordList.txt","r")
        #print("killme has been reset to 0.")
        
        wordListR.close()

    while len(similarLines) == 0:
        callList = open("calls.txt","r")
        for line in callList.readlines():
            stop = 0
            callSim = 0
            callLine = ""
            
            for word in line.split(" "):
                if word == key:
                    stop = 1
                if stop == 0:
                    callLine += word + " "

            splitCallLine = callLine.split(" ")

            if (message.lower() + " ") == callLine.lower():
                callSim += 1000
            elif len(splitCallLine) == 0 and len(words) == 0: 
                callSim += 1000
            elif len(splitCallLine) == 0 and len(words) != 0:
                pass
            else:
                for callWord in splitCallLine:
                    for i in range(-wordRange, wordRange+1):
                        #pass if it's out of range in "splitCallLine" or "words"
                        if splitCallLine.index(callWord) + i <0 or splitCallLine.index(callWord) + i >= len(splitCallLine) or splitCallLine.index(callWord) + i >= len(words):
                            pass
                        elif callWord.strip() == words[splitCallLine.index(callWord) + i]:
                            callSim += round((1/max(len(words),len(splitCallLine)))*100)
                            maximum = max(len(words),len(splitCallLine))
                            #callSim = percentCalc(callSim, words, splitCallLine)
                        else:
                            pass
                        #print(words[splitCallLine.index(callWord) + i] + " and " + callWord + " have a similarity of " + str(round(callSim)))
                            
            #if its over a certain percent of similarity then add to list
            if callSim >= bottomPercent:
                similarLines.append(line)
        #lower ur standards if you dont recognise the call
        if len(similarLines) == 0:
            if bottomPercent > 0:
                bottomPercent -= 5
            else: 
                pass
        #most satisfying fix to an issue  [wrong.]
        callList.close()    
    #print(similarLines)
    #to do: make it randomly generate sentences and compare them to known responses to calls in the similarLines list, potentially add feature to facilitate learning during conversation where after ADIE responds you can either say the response was appropriate or not appropriate, causing her to either add that interaction to the call response list or not.
    #find all known responses
    specificResponses = []
    specificResponsesFull = []
    for call in similarLines:
        callID = call.split(" ")[-1]
        respList = open("responses.txt","r")
        for response in respList.readlines():
            respID = response.split(" ")[-1]
            if callID == respID:
                onlyWordsResp = ""
                stop = 0
                specificResponsesFull.append(response)
                for word in response.split(" "):
                    if word == key:
                        stop = 1
                        onlyWordsResp = onlyWordsResp[0:-1]
                    if stop == 0:
                        onlyWordsResp += word + " "
                #print(onlyWordsResp)
                for i in range(0,int(response.split(" ")[-2])):
                    specificResponses.append(onlyWordsResp)
            else:
                pass
    #print(specificResponses)
    chosenLen = 0
    listOLen = []
    #print(str(specificResponses) + " len: " + str(len(specificResponses)))
    for response in specificResponses:
        listOLen.append(len(response.split(" ")))
    #print(listOLen)
    chosenLen = random.choice(listOLen)

    #potentialResp = ""
    #for i in range(1,avgLen+1):
    #    wordList = open("wordList.txt","r")
    #    randWord = random.choice(wordList.readlines()).strip()
    #    potentialResp += randWord + " "
    #potentialResp = potentialResp[0:-1]
    #now choose the response to compare it with. this will be done randomly out of the list of responses, with each response being added to that list a number of times equal to its emotional score.
    idealResp = random.choice(specificResponses)
    #print(idealResp)
    respSimilarity = 0
    splitIdeal = idealResp.split(" ")
    potentialResp = ""
    #splitPotential = potentialResp.split(" ")

    while respSimilarity < 40:
        potentialResp = ""
        respSimilarity = 0
        for i in range(0,len(idealResp.split(" "))):
            wordList = open("wordList.txt","r")
            randWord = random.choice(wordList.readlines()).strip()
            potentialResp += randWord + " "
        potentialResp = potentialResp[0:-1]
        splitPotential = potentialResp.split(" ")
        #print(potentialResp)
        if potentialResp.lower() == idealResp.lower():
            respSimilarity += 1000
        elif len(potentialResp) == 0 and len(idealResp) == 0: 
            respSimilarity += 1000
        elif len(potentialResp) == 0 and len(idealResp) != 0:
            pass
        else:
            for idealWord in splitIdeal:
                for i in range(-wordRange, wordRange+1):
                    #pass if it's out of range in "splitCallLine" or "words"
                    if splitIdeal.index(idealWord) + i <0 or splitIdeal.index(idealWord) + i >= len(splitIdeal) or splitIdeal.index(idealWord) + i >= len(splitPotential):
                        pass
                    elif idealWord.strip() == splitPotential[splitIdeal.index(idealWord) + i]:
                        respSimilarity += round((1/max(len(splitPotential),len(splitIdeal)))*100)
                    else:
                        pass
        #print(potentialResp + " " + str(respSimilarity))
    emoSub2 = int(msgEmote)-2
    emoAdd2 = int(msgEmote)+2
    ADIEemote = random.choice(range(emoSub2,emoAdd2))
    print("ADIE: " + potentialResp + " (Tone = " + str(ADIEemote) + ")")
    isGood = input("Did this response make sense? (Y/N) ")
    if isGood.lower() == "y":
        callList = open("calls.txt","a")
        idCount += 1
        callList.write(message+" "+key+" "+str(50 + int(msgEmote))+" "+str(idCount)+"\n")
        callList.close()
        respList = open("responses.txt","a")
        respList.write(potentialResp+" "+key+" "+str(50 + int(ADIEemote))+" "+str(idCount)+"\n")
    elif isGood.lower() == "n":
        pass

keyGen()
train()
while True:
    talk()