def isSwear(word):
    swearList = ["poop",
                 "pee",
                 "ass",
                 "dick",
                 "fuck",
                 "shit",
                 "cunt",
                 "bitch",
                 "slut",
                 "slutty",
                 "nigger",
                 "penis",
                 "tits",
                 "boobs",
                 "cock",
                 "anus",
                 "vagina"]
    if word in swearList:
        return True
    else:
        return False

def getMenuOption():
    goodInput = False
    goodResponses = ["1",
                     "2",
                     "3",
                     "q"]
    while not goodInput:
        response = raw_input("Make a selection: ")
        if response.lower() in goodResponses:
            goodInput = True
        else:
            print "Please make a valid selection!"
    return response.lower()

def getWord(prompt):
    goodInput = False
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True
        if isSwear(response):
            goodInput = False
            print "Don't use that kind of language with me!"
        return response

# by matthew     
def getTalk(prompt):
	goodInput = False
	while not goodInput:
		response = raw_input(prompt)
		if response[0] == '"' and response[-1] == '"':
			goodInput = True
		else:
			print "Make sure you got quotes around the sentence!"
	return str(response) 
		

def getNumber(prompt):
    goodInput = False
    numbers = "0123456789."
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True
        for character in response:
            if character not in numbers:
                goodInput = False
                print "Numbers only please!"
    return str(response)
        
        
#by Tommy
def getGender(prompt):
    goodInput = False
    genders = "Man","Girl"
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True
        if getNumber(response):
            goodInput = False
            print " please only gender!"
    return str(response)

 

















