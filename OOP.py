#voter regitration app

import random

class Voter(object):
    year = 2017
    number = 0
    
    
    
    def __init__(self,name="Voter",id_number=0):
        self.name = name
        self.id_number = id_number

    def capture_details(self,age,residence):
        self.age = age
        self.residence = residence

        print "Age and Residence details captured"

    def generate_voter(self,number = 0):
        
        self.number=number
        self.number = random.randint(1000,1000000000)
        return self.number

    def print_details(self):
        print "Voter Name: " + self.name
        print "Voter id_number: " + str(self.id_number)
        print "voter Age: " + str(self.age)
        print "VOter Residence: " + self.residence
        print "voter number: " + str(self.number)

        


class Aspirant(Voter):
    def ward(self,ward,party):
        self.ward = ward
        self.party = party

    def position(self,position):
        self.position=position

    def describe_aspirant(self):
        print "Aspirant %s is %s years old, Id Number %s from %s is vying for % seat for %s ward" %(self.name,self.age,str(self.id_number),self.residence,self.position,self.ward) 
    
        print "Aspirant's voter number is: %s" %str(self.number)

def main():
    
    aseey = Voter()
    aseey.name = (raw_input("Enter the voters Name: "))
    aseey.id_number=(raw_input("Enter the voter\'s Id Number: "))
    aseey.capture_details(raw_input("Enter voter's age: "),raw_input("Enter the voter's residence: "))
    aseey.generate_voter()

    aseey.print_details()

main()

raw_input("press <enter> to exit")
    
        

    

    
