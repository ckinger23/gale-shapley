import sys
import random



boysNameList = [
    'Liam',
    'Noah',
    'William',
    'James',
    'Logan',
    'Benjamin',
    'Mason',
    'Elijah',
    'Oliver',
    'Jacob',
    'Lucas',
    'Michael',
    'Alexander',
    'Ethan',
    'Daniel',
    'Matthew',
    'Aiden',
    'Henry',
    'Joseph',
    'Jackson',
    'Samuel',
    'Sebastian',
    'David',
    'Carter',
    'Wyatt',
    'Jayden',
    'John',
    'Owen',
    'Dylan',
    'Luke',
    'Gabriel',
    'Anthony',
    'Isaac',
    'Grayson',
    'Jack',
    'Julian',
    'Levi',
    'Christopher',
    'Joshua',
    'Andrew',
    'Lincoln',
    'Mateo',
    'Ryan',
    'Jaxon',
    'Nathan',
    'Aaron',
    'Isaiah',
    'Thomas',
    'Charles',
    'Caleb',
    'Josiah',
    'Christian',
    'Hunter',
    'Eli',
    'Jonathan',
    'Connor',
    'Landon',
    'Adrian',
    'Asher',
    'Cameron',
    'Leo',
    'Theodore',
    'Jeremiah',
    'Hudson',
    'Robert',
    'Easton',
    'Nolan',
    'Nicholas',
    'Ezra',
    'Colton',
    'Angel',
    'Brayden',
    'Jordan',
    'Dominic',
    'Austin',
    'Ian',
    'Adam',
    'Elias',
    'Jaxson',
    'Greyson',
    'Jose',
    'Ezekiel',
    'Carson',
    'Evan',
    'Maverick',
    'Bryson',
    'Jace',
    'Cooper',
    'Xavier',
    'Parker',
    'Roman',
    'Jason',
    'Santiago',
    'Chase'
    ]

girlsNameList = [
    'Emma',
    'Olivia',
    'Ava',
    'Isabella',
    'Sophia',
    'Mia',
    'Charlotte',
    'Amelia',
    'Evelyn',
    'Abigail',
    'Harper',
    'Emily',
    'Elizabeth',
    'Avery',
    'Sofia',
    'Ella',
    'Madison',
    'Scarlett',
    'Victoria',
    'Aria',
    'Grace',
    'Chloe',
    'Camila',
    'Penelope',
    'Riley',
    'Layla',
    'Lillian',
    'Nora',
    'Zoey',
    'Mila',
    'Aubrey',
    'Hannah',
    'Lily',
    'Addison',
    'Eleanor',
    'Natalie',
    'Luna',
    'Savannah',
    'Brooklyn',
    'Leah',
    'Zoe',
    'Stella',
    'Hazel',
    'Ellie',
    'Paisley',
    'Audrey',
    'Skylar',
    'Violet',
    'Claire',
    'Bella',
    'Aurora',
    'Lucy',
    'Anna',
    'Samantha',
    'Caroline',
    'Genesis',
    'Aaliyah',
    'Kennedy',
    'Kinsley',
    'Allison',
    'Maya',
    'Sarah',
    'Madelyn',
    'Adeline',
    'Alexa',
    'Ariana',
    'Elena',
    'Gabriella',
    'Naomi',
    'Alice',
    'Sadie',
    'Hailey',
    'Eva',
    'Emilia',
    'Autumn',
    'Quinn',
    'Nevaeh',
    'Piper',
    'Ruby',
    'Serenity',
    'Willow',
    'Everly',
    'Cora',
    'Kaylee',
    'Lydia',
    'Aubree',
    'Arianna',
    'Eliana',
    'Peyton',
    'Melanie',
    'Gianna',
    'Isabelle',
    'Julia',
    'Valentina',
    'Nova',
    'Clara',
    'Vivian',
    'Reagan',
    'Mackenzie',
    'Madeline',
    ]


def main():
    numPerson = int(input("Enter how many matches you would like? "))
    proposerFile = open("proposer75.txt","w+" )
    proposeeFile = open("proposedTo75.txt", "w+")
    proposersBeingUsed = []
    proposedToBeingUsed = []
    for x in range(numPerson):
        proposersBeingUsed.append(boysNameList[x])
        proposedToBeingUsed.append(girlsNameList[x])
    for j in proposersBeingUsed:
        prefList = proposedToBeingUsed
        random.shuffle(prefList)
        proposerFile.write(j+":       "+str(prefList).replace('\'',"").replace(" ","").strip("["+"]")+"\n")
    for y in proposedToBeingUsed:
        womanprefList = proposersBeingUsed
        random.shuffle(womanprefList)
        proposeeFile.write(y+":       "+str(womanprefList).replace('\'',"").replace(" ","").strip("["+"]")+"\n")
    proposeeFile.close()
    proposerFile.close()

main()