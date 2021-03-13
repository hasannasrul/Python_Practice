# Create Traveler object
class Traveler:
    def __init__(self,tn,tc,ta,c):
        self.tn = tn
        self.tc = tc
        self.ta = ta
        self.c = c

# Travel Agency taking list of Traveler Object
class TravelAgency:
    def __init__(self,tl):
        self.tl = tl
    
    # take country as a parameter and return number of travellers who visited that country 
    def countTravelersTraveledCountry(self,name_of_country):
        count=0
        for i in self.tl:
            for j in i.tc:
                if j == name_of_country:
                    count+=1
        return count

    # Return Traveller name who visited maximum number of countries
    def getTravelerTravelledMaxCountry(self ):
        max=0
        name=""
        for i in self.tl:
            for j in i.tc:
                if len(j) > max:
                    max = len(j)
                    name = i.tn

        return name

if __name__ == '__main__':


    tl=[] #traveller list initiation and to be append later in the code
    noOfTravelers = int(input("Enter Number Of Travelers : "))

    for i in range(noOfTravelers):
        tn = input("Enter Traveler Name: ")
        n = int(input("number of countries traveller visit: "))
        tc=[]
        for j in range(n):
            tc.append(input("Enter Country name you visits: "))
        ta = int(input("Enter Your Age : "))
        c = input("Enter Your Home Country : ")
        traveler = Traveler(tn,tc,ta,c)
        tl.append(traveler)
    
    o1 = TravelAgency(tl)
    nameofcountry = input("Enter Name of Country Agency wanna Check : ")
    print(o1.countTravelersTraveledCountry(nameofcountry))
    print(o1.getTravelerTravelledMaxCountry())