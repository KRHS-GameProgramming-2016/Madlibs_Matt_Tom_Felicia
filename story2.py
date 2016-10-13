from input import *

#Written by Matthew 
def story():
	time = getNumber("Enter the time: ")
	talk = getTalk("Enter what you say: ")
	verb1 = getWord("Type in a verb: ")
	noun1 = getWord("Type in a  noun: ")
	verb2 = getWord("Type in a verb: ")
	verb3 = getWord("Type in a verb: ")
	noun2 = getWord("Type in a noun: ")
	verb4 = getWord("Type in a noun: ")
	
	text = ""
	text += "The time is " + time
	text += ". You say " + talk
	text += ". You see a clown walking on the road, you " + verb1
	text += ". The clown sees you coming towards him"
	text += ". The clown looks inside his bag a grabs out a " + noun1
	text += ". You decided to " + verb2
	text += ". The clown starts to " + verb3
	text += ". You look around and find a " + noun2
	text += ". The clown begins to " + verb4
	

	
	
	
	
	return text 
