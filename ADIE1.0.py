import random
alphaFrom = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
alphaSend = {
    'a':10,
    'b':10,
    'c':10,
    'd':10,
    'e':10,
    'f':10,
    'g':10,
    'h':10,
    'i':10,
    'j':10,
    'k':10,
    'l':10,
    'm':10,
    'n':10,
    'o':10,
    'p':10,
    'q':10,
    'r':10,
    's':10,
    't':10,
    'u':10,
    'v':10,
    'w':10,
    'x':10,
    'y':10,
    'z':10,
    ' ':10
}

def inputsetup():
    global mInput, eInput, alphaSend
    mInput = input("Message: ")
    eInput = input("Emotion (Positive(P), Bad(B), Neutral(N)): ")
    if eInput == "P":
        for i in mInput:
            if i == " ":
                pass
            else:
                if (alphaSend[i] + 1) == 11:
                    pass
                alphaSend[i] += 1
            
    elif eInput == "B":
        for i in mInput:
            if i == " ":
                pass
            else:
                if (alphaSend[i] - 1) == -1:
                    pass
                else:
                    alphaSend[i] -= 1

def doInput():
    inputsetup()
    while eInput != "B" and eInput != "P" and eInput != "N":
        print("Follow the instructions, please.")
        inputsetup()

def AIresponse():
    global alphaFrom, alphaSend, mInput, happiness
    AItext = ""
    tone = 0
    #PLEASE shorten if possible. This is essentially a weighted random selection based off of how much the program likes/dislikes letters
    for i in random.choices(alphaFrom,weights=(alphaSend["a"],alphaSend["b"],alphaSend["c"],alphaSend["d"],alphaSend["e"],alphaSend["f"],alphaSend["g"],alphaSend["h"],alphaSend["i"],alphaSend["j"],alphaSend["k"],alphaSend["l"],alphaSend["m"],alphaSend["n"],alphaSend["o"],alphaSend["p"],alphaSend["q"],alphaSend["r"],alphaSend["s"],alphaSend["t"],alphaSend["u"],alphaSend["v"],alphaSend["w"],alphaSend["x"],alphaSend["y"],alphaSend["z"],10),k=round(len(mInput)/2)):
        AItext += i 
    for i in AItext:
        tone += alphaSend[i]
    tone = round(tone/len(AItext))

    return print("AI message: " + AItext + "."), print("AI tone (out of 20): " + str(tone))

while True:
    #get input
    doInput()
    #get reponse
    AIresponse()