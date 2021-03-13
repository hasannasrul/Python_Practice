class Passenger:
    def __init__(self,passName,passAge,disTravel):
        self.passName = passName
        self.passAge = passAge
        self.disTravel = disTravel

#keep track of price of the ticket with tax included for every age and return total price
def calculateTicketFare(listOfPassenger,fairPerKm):
        total = 0
        for i in listOfPassenger:
            if i.passAge < 12 or i.passAge >= 60:
                total+= i.disTravel*fairPerKm
            elif i.passAge >= 12 and i.passAge <= 20:
                total+= (i.disTravel*fairPerKm) + ((i.disTravel*fairPerKm) * 0.10)
            elif i.passAge >= 21 and i.passAge <= 59:
                total+= (i.disTravel*fairPerKm) + ((i.disTravel*fairPerKm) * 0.12)
        return total

# count no of junior and seior passengers in the ticket and return the number
def calculateSeniorJuniorPassenger(listOfPassenger):
        count=0
        for i in listOfPassenger:
            if i.passAge >=60 or i.passAge < 12:
                count+=1
        return count


if __name__ == '__main__':

    no_of_passenger = int(input("Enter Number of Passenger : "))
    pl = []
    for i in range(no_of_passenger):
        nm = input("Enter name of Passenger : ")
        ag = int(input("Enter Age of Passenger : "))
        dis = int(input("Enter Dis Travel By Passenger : "))
        p_obj = Passenger(nm,ag,dis)
        pl.append(p_obj)
    
    fair = int(input("Enter Fair Per Km : "))

    print(calculateTicketFare(pl,fair))
    print(calculateSeniorJuniorPassenger(pl))


   