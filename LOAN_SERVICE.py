

################################################################################################################################
#                                                                                                                              #
#                                                        KOPESHA LOAN                                                          #
#                                                                                                                              #
################################################################################################################################






#FIRST CLASS: THIS IS THE PARENT CLASS

class MainLoan:

    name=None
    age=None
    genre=None
    occupation=None
    loan=None
    Days=None
    

    def __init__(self,name,age,genre,occupation,loan,Days):
        
        self.name=name
        self.age=age
        self.genre=genre
        self.occupation=occupation
        self.loan=loan
        self.Days=Days
        
    def SimpleLoan(self,another_loan):

        MaxDays=30 # past this number of days, the loan is going to be increasing by the fine.
        while True:
            print()
            self.name=input("what is your full name: ")
            self.loan=int(input("enter amount of loan: "))
            self.Days=int(input("Enter days with loan: "))
            if self.Days<=MaxDays:
                interest=self.loan*(10/100)
                payment=self.loan+interest
                print()
                print(f"Dear {self.name.split()[0]} ,after {self.Days} days, you will pay an amount of {payment}")
                print("thank you!!😁")
                print()
                another_loan=input("wanna take another loan? ")
                
                if another_loan=="yes" or another_loan=="Yes" or another_loan=="YES":
                    continue
                else:
                    print("THANK YOU FOR TRUSTING US!!!")
                    print()
                    break
            else:
                interest=self.loan*(10/100)
                extraDays=self.Days-MaxDays
                TotalFine=extraDays*(self.loan*(1/100))
                payment=self.loan+interest+(TotalFine)
                print(f"because of the extra {extraDays} days, you will be charged a fine of {TotalFine} on top of the interest")
                print()
                print(f"So,Dear {self.name.split()[0]} , after {self.Days} days, you will pay an amount of {payment} which include the {self.loan} of loan , the interest of {interest} plus a fine of {TotalFine}")
                print()
                print("thank you!!😁")
                
                if another_loan=="yes" or another_loan=="Yes" or another_loan=="YES":
                    continue
                else:
                    print("THANK YOU FOR TRUSTING US!!!")
                    print()
                    break


#SECOND CLASS: FOR STUDENT LOAN
                
class EduLoan(MainLoan): # here we are inheriting from the base or parent class called "MainLoan"

    level=None

    def __init__(self,name,age,genre,occupation,loan,Days,level):
        self.name=name
        self.age=age
        self.genre=genre
        self.occupation=occupation
        self.loan=loan
        self.Days=Days
        self.level=level

    def SimpleLoan(self,another_loan):

        print()
        print("Hello dear student, this is KOPESHA, the solution to your loan aquisition problems")
        print()

        MaxDays=280 # past this number of days, the loan is going to be increasing by the fine.
                    # the academic year in uganda is arround 240, so we add 40 days to help them
                    # finish paying at the end of the academic year (arround 280 days)
        while True:
            print()
            self.name=input("what is your full name: ")
            self.loan=int(input("enter amount of loan: "))
            self.Days=int(input("Enter days with loan: "))
            self.level=input("level of studies please: ")
            if self.Days<=MaxDays:
                naame=self.name
                interest=self.loan*(10/100)
                payment=self.loan+interest
                print()
                print(f"Dear {naame.strip().lower().split()[0]},After further verification you succesfully got the {self.level} student loan of ${self.loan}, after {self.Days} days, you will pay an amount of ${payment}")
                print("thank you!!😁")
                print()
                another_loan=input("do you want to take another loan? ")
                
                if another_loan=="yes" or another_loan=="Yes" or another_loan=="YES":
                    continue
                else:
                    print("THANK YOU FOR TRUSTING US!!!")
                    print("We wish you success in your studies, remember, KOPESHA is here to ensure your future")
                    print()
                    break
            else:
                naame=self.name
                interest=self.loan*(10/100)
                extraDays=self.Days-MaxDays
                TotalFine=extraDays*(self.loan*(1/100))
                payment=self.loan+interest+(TotalFine)
                print()
                print(f"hey {naame.strip().lower().split()[0]}, because of the extra {extraDays} days, you will be charged a fine of ${TotalFine} on top of the interest")
                print()
                print(f"So,Dear {self.name.split()[0]} , after {self.Days} days, you will pay an amount of ${payment} which include the ${self.loan} of loan , the interest of ${interest} plus a fine of ${TotalFine}")
                print()
                print("thank you!!😁")
                
                if another_loan=="yes" or another_loan=="Yes" or another_loan=="YES":
                    continue
                else:
                    print("THANK YOU FOR TRUSTING US!!!")
                    print()
                    break






# THIRD CLASS : FOR BUSINESS LOANS

class BusinessLoan(MainLoan): # here we are inheriting from the base or parent class called "MainLoan"

    business=None
    Livelyhood=None

    def __init__(self,name,age,genre,occupation,loan,Days,business,Livelyhood):
        self.name=name
        self.age=age
        self.genre=genre
        self.occupation=occupation
        self.loan=loan
        self.Days=Days
        self.business=business
        self.Livelyhood=Livelyhood # how old is the business (to see if the project has survived without the loan and we can then act accordingly)

    def SimpleLoan(self,another_loan):

        print()
        print("Hello dear, this is KOPESHA, the solution to your loan aquisition problems")
        print()

        MaxDays=365 # past this number of days, the loan is going to be increasing by the fine.
                    # we are considering 365, 
                    # Idealy finish paying at the end of 300 days
        while True:
            print()
            self.name=input("what is your full name: ")
            self.loan=int(input("enter amount of loan: "))
            self.Days=int(input("Enter days with loan: "))
            self.business=input("what is your business: ")
            self.Livelyhood=int(input("for how long (in year) are you holding this business: "))
            if self.Days<=MaxDays:
                naame=self.name
                interest=self.loan*(10/100)
                payment=self.loan+interest
                print()
                print(f"Dear {naame.strip().lower().split()[0]} ,After further verification you succesfully got the special business loan of ${self.loan}, after {self.Days} days, you will pay back an amount of ${payment}")
                print("thank you!!😁")
                print()
                another_loan=input("do you want to take another loan? ")
                
                if another_loan=="yes" or another_loan=="Yes" or another_loan=="YES":
                    continue
                else:
                    print("THANK YOU FOR TRUSTING US!!!")
                    print("We wish you success in your Business, remember, KOPESHA is here to ensure the success of your business")
                    print()
                    break
            else:
                naame=self.name
                interest=self.loan*(10/100)
                extraDays=self.Days-MaxDays
                TotalFine=extraDays*(self.loan*(1/100))
                payment=self.loan+interest+(TotalFine)
                print()
                print(f"hey {naame.strip().lower().split()[0]}, because of the extra {extraDays} days, you will be charged a fine of ${TotalFine} on top of the interest")
                print()
                print(f"So,Dear {self.name.split()[0]} , after {self.Days} days, you will pay an amount of ${payment} which include the ${self.loan} of loan , the interest of ${interest} plus a fine of ${TotalFine}")
                print()
                print("thank you!!😁")
                
                if another_loan=="yes" or another_loan=="Yes" or another_loan=="YES":
                    continue
                else:
                    print("THANK YOU FOR TRUSTING US!!!")
                    print()
                    break





################################################################################################################################
#                                                                                                                              #
#                                            OBJECT CREATION AND CODE RUNNING                                                  #
#                                                                                                                              #
################################################################################################################################




BusinessObject=BusinessLoan(None,None,None,None,None,None,None,None) # 8 values since we have initiated 8 variables
StudentObject=EduLoan(None,None,None,None,None,None,None) # 7 values since we have initiated 7 variables

def TheLoan():
    State=input("who are you: STUDENT OR BUSINES_OWNER: ")
    if State=="student" or State=="Student" or State=="STUDENT":
        StudentObject.SimpleLoan(None)
    elif State=="Businessowner" or State=="businessowner" or State=="BUSINESSOWNER":
        BusinessObject.SimpleLoan(None) 
    else: # the more classes we create, the more elif statements we will add here for each specific class
        print("you're not a STUDENT or a BUSINESS OWNER,KINDLY WAIT FOR YOUR TURN TO START")
        
TheLoan()











