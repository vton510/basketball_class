#Assignment 10.1 - Vinh Ton
#I made a class that is about a sport, basketball, that I played in highschool and there are functions that I use to make it more cool
import random #Importing 

class basketball: #This is my class name 
    max_roster = 15 #these are my two class variables
    min_roster = 5
    def __init__(self, city, mascot, team, head_coach, team_color, school_rivals): #These are my data varables 
        self.city = city # is a string
        self.mascot = mascot # is a string
        self.team = team #This is a dictionary
        self.color = team_color #team color 
        self.coach = head_coach #The headcoach
        self.rivals = school_rivals #List of team rivals 
    #This is one of my get method where I can my team name that is based on the city and the mascot
    def get_team_name(self):
        team = self.city + " " + self.mascot #Just add two strings together to make the team name
        return team
    #this is a function that allow me to change my team mascot, because I always wanted a cool mascot but I couldn't but now I can
    def change_mascot(self, new_mascot): 
        self.mascot = new_mascot #Changing the mascot by giving it an argument
        return new_mascot
    #This function allows me to get the list of keys that is in the dictionary of the team
    def roster(self):
        return self.team[self.coach]
    #using this get method roster() I can add players and remove players by using the max_roster and min_roster class variables
    def add_player(self, new_name):
        if len(self.roster()) >= self.max_roster:
            return "Too many players on Roster please cut your players down to 15" #Tellingg the coach that he is cheating and he needs to cut down his player
        else:
            return self.team[self.coach].append(new_name)
    
    def remove_player(self, name):
        if len(self.roster()) <= self.min_roster: #If the eamount of players on the team is less than 5
            return "You're tripping coach, how are you're going to win with 4 players>"  #Telling the coach that he needs some help
        else: 
            self.team[self.coach].remove(name)
            return self.roster()
    #using the import function I can give my players diff jersey number, like my jv coach in Highschool (1ST OTHER METHOD)
    def jersey(self):
        list_players =[] #an empty list
        for i in self.roster(): #a for loop to check the name of each rosteer
            jersey_number = random.randrange(0,99) #what can be the jersey of each player
            player_jersey = self.color + ": " + i + ": " + str(jersey_number) #What will the jersey say 
            list_players.append(player_jersey) #Add it to the list and loop it for the entire list
        return list_players
    #Using the Random module I can make up a game that is like a rivarly game and it would be a close scores. (2nd other METHOD)
    def game_play(self):
        opponent = random.choice(self.rivals) #using the rival game it will give us a random opponent
        scores = opponent + ": " + str(random.randrange(90,105)) + " vs. " + self.get_team_name() + ": " + str(random.randrange(90,105)) #This is to show the scoreboards 
        return scores


def main():
#In order to call the class("a string of a city", "Mascot", {Dictionary of the headcoach and a list opf players}, "string of headcoach", "str Jersey color", [list of rivals and their mascot])
    x = basketball("Oakland", "Goats", {"Ryan": ["Sol","joey", "Vinh","Yq","Bin","Garson", "Giheyon"]}, "Ryan", "red",["Segre Eagle","Archer Angel","Dulin Sharks","San Jose Tiger"]) 
    print(x.get_team_name()) #This is the team name
    x.remove_player("joey")#Removing a player
    x.remove_player("Bin")#Removing a nother player
    print(x.remove_player("Yq")) #This is to test out the if statement because if you 4 players how can one play
    x.add_player("Jalen") #add new player
    x.add_player("Gil") #add new player
    print(x.roster()) #updating the new roster
    print(x.jersey()) #Give all the players jersey #
    print(x.game_play())#This give you game play when it is a rival game
    print(x.game_play())
    print(x.game_play())

if __name__ =="__main__":
    main()
