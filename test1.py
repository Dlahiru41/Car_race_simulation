import random
import sys
from operator import itemgetter
from datetime import datetime
import json

#----IMPORTANT LISTS THAT ARE USED BY THE PROGRAM------

players=[]
allRaces=[]
oneRace=[]
teams=[]
#``````````````````````````````````````````````````````

#------------------------------------------------------------------------------------------------------  
def addAPlayer(): #add driver's detials
    name=input('enter the name of the player')#-----take the player name input from the user
    while True:#------take the player age as a input and validate
        try:
            age=int(input('enter the age of the player'))
            break
        except ValueError:#----if the user input is not an integer interate until a valid input is given
            print("Enter a valid age")
            continue
    team=input('enter the team of the player')#-------take the team as an input
    car=input('enter the car of the player')#----take the car name as an input
    while True:#-----take the points as an input and validate it
        try:
            currentPoint=int(input('enter the current points of the player'))
            break
        except ValueError:#----if the user input is not an integer interate until a valid input is given
            print("Enter a valid point")
            continue
    player=[name,age,team,car,currentPoint]#-----append the user input to a single list as player
    players.append(player)#------append one single player list to the players list which contains all the players 


#------------------------------------------------------------------------------------------------------  
def deleteAPlayer():#delete a player from the list
    count=0
    sameNameIndexes=[]#-------if the players list have same names user want to delete, the indexes of those users will append to this list
    deletePlayer=input('enter the name of the player you want to delete') # -----take user input to delete the name
    for i in players:#-----validate if there players with the same name
        if i[0]==deletePlayer:
            index=players.index(i)
            #players.pop(index)
            count=count+1
            sameNameIndexes.append(index)#-------append the indexes of the players with the same name
            
    if count==0:#----if the user input name is not in the players list the program will print 
        print('player is not available')
        
    elif count==1:#------if the user input name has only one occurance in the player list
        print(deletePlayer,' is deleted')
        players.pop(index)
        
    elif count!=1:#------if the user input name has many occurances in the player list
        print('many')
        for i in sameNameIndexes:
            index1=sameNameIndexes.index(i)
            print (players[i],i)#-----display the indexes of the players with same name
    
        while True:#------give the user the option to delete the players by using the index (this is a sub menu)
            try:#------validate the user input
                deleteplayerIndex=int(input('input the index of the player you want to delete'))
                if deleteplayerIndex not in sameNameIndexes:
                    print('invalid index')
                    continue#----if the user input a invalid index interate until a correct index is given
                else:
                    players.pop(deleteplayerIndex)
                    print('player is deleted')
                    break
            except ValueError:#-----habdle the valueError exception
                print('Input should be an integer')
                continue

#------------------------------------------------------------------------------------------------------  

def updateDriverDetails():#--update the drivers'/players' details
    
    updateDriver=input('input the name of the driver you want to update')#---allow the user to input the name of the player want to update
    count=0
    index=0#---store the index of the player who with the input name
    for i in players:#-----loop for interate through the list and find the player with the input name
        if i[0]==updateDriver:
            index=players.index(i)#-----get the index
            count=1
            #print('okay')

    if count==1:#-----if the loop able to find the player print a sun menu
        inputValuesMustBe=['N','A','T','C','P']#-----user input should be in this list

        #submenu
        print('enter N if you want to update the name of the player \n'
              'enter A if you wand to update the age of the player \n'
              'enter T if you want to update the team of the player \n'
              'enterr C if you want to update the car of the player \n'
              'enter P if you want to update the points of the player')

        while True:#-------validate the user input
            updateInput=input()#-----store the user input
            upperInput=updateInput.upper()#---------------user can input the options either in uppercase or lowercase
            if upperInput not in inputValuesMustBe:
                print('invalid input')#--------------if the user input not in the iist
                continue#----------iterate until the user inputs a valid input

            elif upperInput=='N':#------if the user want to update the name
                updateName=input('enter the new name')
                players[index][0]=updateName#-----update the new details accessing the relevent index of the player list
                break
            elif upperInput=='A':#------if the user want to update the age
                while True:#------age should be a integer , program interate until user gives a valid input
                    try:
                        updateAge=int(input('enter the new age'))
                        players[index][1]=updateAge#-----update the new details accessing the relevent index of the player list
                        break
                    except ValueError:#-----handle the valueerror exception
                        print("Enter a valid age")
                        continue
                break
            elif upperInput=='T':#------if the user want to update the team
                updateTeam=input('enter the new team')
                players[index][2]=updateTeam
                break
            elif upperInput=='C':#------if the user want to update the car
                updateCar=input('enter the new car')
                players[index][3]=updateCar#-----update the new details accessing the relevent index of the player list
                break
            elif upperInput=='P':#------if the user want to update the points
                while True:#-----data type of the points should be integer, program iterates until the user gives a valid input
                    try:
                        updatePoints=int(input('enter the new points'))
                        players[index][4]=updatePoints#-----update the new details accessing the relevent index of the player list
                        break
                    except ValueError:
                        print("Enter a valid point")
                        continue
                break
        
    else:
        print("player is not available")#------if the user input name is not in the players list ,print 
#------------------------------------------------------------------------------------------------------          

def sortdescendingOrder():#---sort the player list according to the descending order of the points
    
    playersInAscendingOrder = sorted(players, key=lambda x: x[4])#----lamda function to take the forth element of a list inside the players list
    playersInAscendingOrder.reverse()#--------reverse the order of the element list playersInAscendingOrder which are in ascending order to make them to descending order
    for i in playersInAscendingOrder:
        print(i)#-----print the sorted player list
    header=['Name','age','team','car','points']#------topics of the columns of the table
    print(f'{header[0]:<15}{header[1]:<10}{header[2]:<10}{header[3]:<10}{header[4]:<10}')#----use formated sting to present the data in a table type
    for i in playersInAscendingOrder:
        print(f'{i[0]:<15}{i[1]:<10}{i[2]:<10}{i[3]:<10}{i[4]:<10}')
#------------------------------------------------------------------------------------------------------

        #`````````SIMULATE A RANDOM RACE```````````
        
def randomRace():#---simulate a random race
    try:
        positions=[]#------list that store  numbers in the range of len(players) append as elements
        a=len(players)
        for i in range(a+1):#----loop to append numbers to list positions
            if i !=0:
                positions.append(i)
        res = random.sample(players, len(players))#-------shuffle the players list

        team = list(zip(positions, res))#-------comnbine the positions list and the players list to assign players a postitions
        
        team[0][1][4]=team[0][1][4]+10#-----add 10 points to the player with position 1

        team[1][1][4]=team[1][1][4]+7#-----add 7 points to the player with position 2

        team[2][1][4]=team[2][1][4]+5#-----add 5 points to the player with position 3

        oneRaceStr = ''.join(''.join(map(str, tup)) for tup in team)#----convert the list type to a string
        oneRace.append(oneRaceStr)#-----append the race details to the oneRace list
    except IndexError:
        print('there shoul be atleast three players')


def randomRaceFinished():#------assign location details and the date of the race details
    locations=['Nyirád', 'Höljes','Montalegre', 'Barcelona', 'Rīga', 'Norway']#-------------all the locations to be selecte randomly
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    raceStartDate = now.strftime("%d/%m/%Y %H:%M:%S")
    locationOfTheRace=random.choice(locations)#--------randomly select the location
    oneRace.append(raceStartDate)#------append the date to the race details 
    oneRace.append(locationOfTheRace)#----append the location to the race details
    randomRace()
    
#------------------------------------------------------------------------------------------------------     
def displayAllTheRaces():#-----print the all race details to the console 
    for i in oneRace:
        print(i,'\n')
        if (oneRace.index(i)+1)%3==0:#------print dotted line after one complete race 
            print('-'*50)
#------------------------------------------------------------------------------------------------------        
#-`````````FILE HANDLING```````````

def storeDateIntoFile():#--------form a player list according descending order of the points
    playersInAscendingOrder = sorted(players, key=lambda x: x[4])
    playersInAscendingOrder.reverse()
    for i in playersInAscendingOrder:
        print(i) 
    with open('allTheData.txt') as filehandle:
        json.dump(playersInAscendingOrder, filehandle)
#------------------------------------------------------------------------------------------------------  
def readDatafromTheFile():#------read the data from a previous session to resume perpose
    try:
        print('The Below information is from allTheData.txt')
        with open('allTheData.txt', 'r') as filehandle:
            global players
            players = json.load(filehandle)#------json to indentify the data type 
            print(players)
    except FileNotFoundError:#-------exception handling for FileNotFoundError
        print('allTheData.txt file is not yet created')
    except json.decoder.JSONDecodeError:#----------exceptiom handling for if the file is empty
        print('file is empty')

    
#------------------------------------------------------------------------------------------------------  
#main program
validInput=''


#-----MAIN MENU---------
commands=['ADD','UDD','DDD','VCT','SRR','VRL','STF','RFF','ESC']#-----list containing all the commands

while validInput!='ESC':#-------if the user inputs ESC the loop will stop
    print('-'*50)
    #------menu options---------
    print("Type ADD for adding driver details \n"
"Type DDD for deleting \n"
"Type UDD for updating driver details \n"
"Type VCT for viewing the rally cross standings table \n"
"Type SRR for simulating a random race \n"
"Type VRL for viewing race table sorted according to the date \n"
"Type STF to save the current data to a text file \n "
"Type RFF to load data from the saved text file \n"
"Type ESC to exit the program. ")
    print('-'*50)

    
    while True:#-----input validation
        commandInput=input()
        commandInputUpper=commandInput.upper()

        if commandInputUpper not in commands:#-----check whether the user input in the list of commands
            print('command is not in the input commands')
            continue
        else:
            validInput=commandInputUpper#----if th user input is in the user command list store it for the further proccedings 
            print('your input is valid')
            break
    if validInput=='ADD':#-------implement the addAPlayer function according to the user input
        addAPlayer()
        for i in players:
            print(i)
    elif validInput=='DDD':#-------implement the deleteAPlayer function according to the user input
        deleteAPlayer()
        
    elif validInput=='UDD':#-------implement the updateDriverDetails function according to the user input
        updateDriverDetails()
        
    elif validInput=='VCT':#-------implement the sortdescendingOrder function according to the user input
        sortdescendingOrder()
        
    elif validInput=='SRR':#-------implement the randomRaceFinished function according to the user input

        randomRaceFinished()
        stdoutOrigin=sys.stdout
        sys.stdout=open("studentDatabase.txt","a")#-------store the randome race details in to a file
        for i in oneRace:
            print(i,'\n')
            if (oneRace.index(i)+1)%3==0:
                print('-'*50)
        sys.stdout.close()
        sys.stdout=stdoutOrigin
        
    elif validInput=='VRL':#-------implement the displayAllTheRaces function according to the user input
        displayAllTheRaces()
        
    elif validInput=='STF':#-------implement the storeDateIntoFile function according to the user input
        storeDateIntoFile()

    elif validInput=='RFF':#-------implement the readDatafromTheFile function according to the user input
        readDatafromTheFile()

#------------end--------------------


            
            
         
         
        
        

    
        
