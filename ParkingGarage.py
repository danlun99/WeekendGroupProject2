'''
Your parking gargage class should have the following methods:

- takeTicket
- This should decrease the amount of tickets available by 1
- This should decrease the amount of parkingSpaces available by 1

- payForParking
- Display an input that waits for an amount from the user and store it in a variable
- If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
- This should update the "currentTicket" dictionary key "paid" to True

-leaveGarage
- If the ticket has been paid, display a message of "Thank You, have a nice day"
- If the ticket has not been paid, display an input prompt for payment
- Once paid, display message "Thank you, have a nice day!"
- Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
- Update tickets list to increase by 1 (meaning add to the tickets list)


You will need a few attributes as well:
- tickets -> list
- parkingSpaces -> list
- currentTicket -> dictionary
'''
class Garage():

    def __init__(self): # initialize class instances
        self.tickets = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] # list of available tickets
        self.parkingspaces = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] # list of available parking spaces
        self.takenparkingspaces = [] # store the parking spot that has been taken
        self.takentickets = [] # store the ticket number that has been taken
        self.currentTicket = {} # store payment status of each parking ticket

    def taketicket(self): # distribute ticket numbers when customers decide to take parking tickets
        for x in self.tickets:
            if x in self.takentickets:
                continue
            else:
                space = int(input(f'Which parking spot do you want to park? Please choose a spot among these currently available parking spots: {self.parkingspaces}'))
                try:
                    if space not in self.parkingspaces:
                        space = int(input(f'This parking spot is not available. Please choose your spot again among these currently available parking spots: {self.parkingspaces}'))
                        
                    self.takenparkingspaces.append(space)
                    self.parkingspaces.remove(space)
                    self.takentickets.append(x)
                    self.tickets.remove(x)
                    self.currentTicket[x] = False
                    print(f'Your ticket number is {x}')
                    print(f'Your parking spot is {space}')
                    print(f'Payment Status: unpaid')
                    print(f'Current taken tickets: {self.takentickets}')
                    print(f'Current available parking spaces: {self.parkingspaces}')
                    print(f'Current available tickets: {self.tickets}')
                    print(f'Current taken parking spaces: {self.takenparkingspaces}')
                    break

                except ValueError:
                    print(f'{space} is not a valid parking spot. Please try again')

    def payforparking(self,payinput): # calculte payment amount that corresponds to the hours of parking
        try:
            if int(payinput) in self.takentickets:
                costinput = input("How many hours did you stay? Please enter a number.")
                try:
                    finalinput = input(f'Your total is ${int(costinput)*5}. Please enter the payment amount to pay.')
                    if int(finalinput) == int(costinput) * 5:
                        self.currentTicket[int(payinput)] = True
                        print(f'Your ticket has been paid. You have 15 minutes to leave the garage.')
                    else: 
                        print(f'Incorrect input. Please try again')
                
                except ValueError:
                    print(f'{costinput} is not a valid number. Please try again.')
                
            else:
                print(f'{payinput} is not a valid ticket. Please try again.')
           
        except ValueError:
            print(f'{payinput} is not a valid ticket. Please try again')
        
    
    def leavegarage(self,ticketnumber, parkingspot): 
        # check payment status of parking ticket, if already paid then customer can leave, 
        # if not it asks customer to pay for the parking ticket
        try:
            if int(ticketnumber) in self.takentickets:
                if self.currentTicket[int(ticketnumber)] == True:
                    self.parkingspaces.append(parkingspot)
                    self.takenparkingspaces.remove(parkingspot)
                    self.tickets.insert(0, int(ticketnumber))
                    self.takentickets.remove(int(ticketnumber))
                    del self.currentTicket[int(ticketnumber)]
                    print(self.tickets)
                    print(f'Thank you, have a nice day!')
                elif self.currentTicket[int(ticketnumber)] == False:
                    leavepay = input('Your ticket has not been paid. How many hours did you stay? Input a number.')
                    try:
                        leaveinput = input(f'Your total is ${int(leavepay)*5}. Please input the payment amount to pay.')
                        if int(leaveinput) == int(leavepay) * 5:
                            self.parkingspaces.append(parkingspot)
                            self.takenparkingspaces.remove(parkingspot)
                            self.tickets.insert(0, int(ticketnumber))
                            self.takentickets.remove(int(ticketnumber))
                            del self.currentTicket[int(ticketnumber)]
                            print(self.tickets)
                            print(f'Thank you, have a nice day!')
                    
#                         else: 
#                             print(f'Incorrect payment. Please try again')
                        
                    except ValueError:
                        print(f'Not a valid number. Please try again.')
                else:
                    print(f'{ticketnumber} does not exist in our system. Please try again.')
            else:
                print(f'{ticketnumber} is not a valid ticket. Please try again.')
        except ValueError:
            print(f'{ticketnumber} is not a valid ticket. Please try again')


def parkinggarage():
    ticket = Garage()
    while True: 
        question1 = input("What would you like to do? Take ticket, pay for parking, leave garage, or exit garage without parking? Input 'take', 'pay', 'leave' or 'exit' ")
        # 'exit' is for leaving the garage without parking (or for leaving the program when accidentally running it)
        if question1.lower().strip() == "take":
            ticket.taketicket()
        elif question1.lower().strip() == "pay":
            pay = input("What is your ticket number?")
            ticket.payforparking(pay)
        elif question1.lower().strip() == 'leave':
            leave = input('What is your ticket number?')
            spot = int(input('What is your parking spot number?'))
            ticket.leavegarage(leave,spot)
        elif question1.lower().strip() == 'exit':
            print(f'Thank you! See you again!')
            break
        else:
            print('Invalid input. Please try again')
    
parkinggarage()       
        

