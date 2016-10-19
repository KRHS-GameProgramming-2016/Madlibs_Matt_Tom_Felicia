from input import *

#Written by Matthew 
def story():
	time = getNumber("Enter the time: ")
	talk1 = getTalk("Enter what you say: ")
	verb1 = getWord("Type in a verb, don't end with ing: ")
	noun1 = getWord("Type in a  noun: ")
	talk2 = getTalk("Enter what you say: ")
	verb2 = getWord("Type in a verb, don't end with ing: ")
	verb3 = getWord("Type in a verb, don't end with ing: ")
	noun2 = getWord("Type in a noun: ")
	verb4 = getWord("Type in a verb, don't end with ing: ")
	talk3 = getTalk("Enter what you say: ")
	verb5 = getWord("Type in a verb, don't end with ing: ")
	verb6 = getWord("Type in a verb, don't end with ing: ")
	verb7 = getWord("Type in a verb, don't end with ing: ")
	talk4 = getTalk("Enter what you say: ")
	
	
	
	text = ""
	text += "The  time is " + time
	text += ". You say " + talk1
	text += ". You see a clown walking on the road, you " + verb1
	text += ". The clown sees you coming towards him"
	text += ". The clown looks inside his bag a grabs out a " + noun1
	text += ". You think to yourself " + talk2
	text += ". You decided to " + verb2
	text += ". The clown starts to " + verb3
	text += ". You look around and find a " + noun2
	text += ". The clown begins to " + verb4
	text += ". The clown says " + talk3
	text += ". You decied to " + verb5
	text += ". The clown " + verb6
	text += ". You saw the clown and " + verb7
	text += ". You told the clown " + talk4
	text += ". You then walked away from the clown like a boss"
	
	
	
	
	return text 
