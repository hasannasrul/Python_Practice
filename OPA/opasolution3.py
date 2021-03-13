class Player:
    def __init__(self,p_name,p_country,p_age,noOfMatch,noOfRuns,noOfWickets):
        self.p_name = p_name
        self.p_country = p_country
        self.p_age = p_age
        self.noOfMatch = noOfMatch
        self.noOfRuns = noOfRuns
        self.noOfWickets = noOfWickets

class Team:
    def getMinRuns(self,listOfPlayers):
        min = listOfPlayers[0].noOfRuns

        for i in listOfPlayers:
            if i.noOfRuns < min:
                min = i.noOfRuns
                ans1 = i
        return ans1

    def getMaxWickets(self,listOfPlayers):
        max = 0

        for i in listOfPlayers:
            if i.noOfWickets > max:
                max = i.noOfWickets
                ans2 = i
        return ans2

if __name__ == "__main__":

    plist = []
    num = int(input("Enter The Number Of Players : "))
    for i in range(num):
        name = input("Enter Player Name : ")
        country = input("Enter Country of the Player : ")
        age = int(input("Enter Age of the Player : "))
        matches = int(input("Enter Number of Matches : "))
        runs = int(input("Enter Number of runs player scored : "))
        wickets = int(input("Enter number of wickets he takes : "))
        pl = Player(name,country,age,matches,runs,wickets)
        plist.append(pl)
    
    tobj = Team()
    min = tobj.getMinRuns(plist)
    Rname = min.p_name
    Rrun = min.noOfRuns
    Rcoun = min.p_country

    max = tobj.getMaxWickets(plist)
    Wname = max.p_name
    Wwick = max.noOfWickets
    Wcoun = max.p_country

    print(Rname)
    print(Rrun)
    print(Rcoun)

    print(Wname)
    print(Wwick)
    print(Wcoun)