form input import *

#written by Tommy
def story():
    
    NameOfFood1=getwords (" Enter NameoFFood")
    NameOfFood2=getwords (" Enter NameoFFoood")
    NameOfFood3=getwords (" Enter NameoFFoood")
    Name=getNumber (" Enter Name")
    Noun1=getNumber (" Enter Noun")
    Noun2=getNumber (" Enter Noun")
    Noun3=getNumber (" Enter Noun")
    NameOfFood=getNumber (" Enter NameOfFood")
    food=getNumber (" Enter food")
    NameOfMusic=getNumber ("Enter NameOfMusic")
    
    text = ""
    text += "you get hungry so you go get" + NameOfFood1
    text += " as you get into the car you see a girl" + Name
    text +="you and her talking adout" + Noun1
    text += "you ask her what would you like to eat? " + NameOfFood
    text += " she says I wolud like" + NameOfFood3
    text += "you and the girl go get food and talk adout" + Noun2
    text += "you and the girl are at wallmart looking for" + food
    text += "as you are looking for food you start to hear your favorit song" + NameOfMusic
    text += " you and the girl start to go home and talk about" + Noun3
    text +="Once you two get home, you both say goodbye to eachother while looking in eachothers eyes."
    
    
    return text
