#~2.5 years. Simple emotions but getting more complex. 3 years will have more in-depth emotions.
import random
import os


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
    msgEmote = input("emotion (1 - 10): ")
    idCount = 1
    stop = 0

    if convMsg == key:
        pass
    else:
        callList = open("calls.txt","a")
        callList.write(convMsg+" "+key+" "+msgEmote+" "+str(idCount)+"\n")
        callList.close()
        #print(os.stat("wordList.txt").st_size)
        if os.stat("wordList.txt").st_size == 0:
            for word in convMsg.split(" "):
                if stop == 0:
                    wordListA = open("wordList.txt","a")
                    wordListA.write(word + "\n")
                    wordListA.close()
                    stop = 1
                else:
                    pass
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
            pass
        else:
            respList = open("responses.txt","a")
            callList = open("calls.txt","a")
            msgEmote = input("emotion (1 - 10): ")
            idCount += 1
            callList.write(convMsg+" "+key+" "+msgEmote+" "+str(idCount)+"\n")
            respList.write(convMsg+" "+key+" "+msgEmote+" "+str(idCount-1)+"\n")
            respList.close()
            callList.close()
            

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

    callList.close()
    respList.close()

def percentCalc(similarity, wordList1, wordList2):
    similarity += round((1/max(len(wordList1),len(wordList2)))*100)
    return similarity

def talk():
    global key
    message = input("Your message: ")
    similarLines = []
    words = message.split(" ")
    bottomPercent = 0
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
    print(similarLines)
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
                for i in range(1,int(response.split(" ")[-2])):
                    specificResponses.append(onlyWordsResp)
            else:
                pass
    
    avgLen = 0
    for response in specificResponses:
        avgLen += len(response)
    avgLen /= len(specificResponses)
    avgLen = int(round(avgLen))

    potentialResp = ""
    for i in range(1,avgLen+1):
        wordList = open("wordList.txt","r")
        randWord = random.choice(wordList.readlines()).strip()
        potentialResp += randWord + " "
    potentialResp = potentialResp[0:-1]
    #now choose the response to compare it with. this will be done randomly out of the list of responses, with each response being added to that list a number of times equal to its emotional score.
    idealResp = random.choice(specificResponses)
    

keyGen()
train()
while True:
    talk()