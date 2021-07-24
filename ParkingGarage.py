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

class parkingGarage():
    # attributes
    tickets = [1 for i in range(31)] # list of tickets, initializing 30 tickets, value of "1" stands for available ticket, "0" stands for no available ticket
    parkingspaces = [1 for i in range(31)] # list of parking spaces, initializing 30 tickets, value of "1" stands for available space, "0" stands for no available space
    currenttickets = {
        paid: False
    } # dictionary to store the payment status of current tickets, "True" if paid, "False" if not paid
    # methods
    def takeTickets(): # decrease # of available tickets by 1 and # of available parking spaces by 1
        tickets -= 1
        parkingspaces -= 1

    def payforParking():

    def leaveGarage():

