def compute_ticket(miles):

    if miles >= 30:
        price = 12

    elif miles >= 20:
        price = 10

    elif miles >= 10:
        price = 8

    else:
        price = 5

    return price


choice = "YES"

total_tickets = 0

while choice == "YES":

    lastname = input("Enter last name: ")
    miles = float(input("Enter miles from downtown Chicago: "))

    ticket = compute_ticket(miles)

    total_tickets = total_tickets + ticket

    print("Last Name:", lastname)
    print("Ticket Price: $", format(ticket, ".2f"))

    choice = input("Do another? (YES/NO): ").upper()

print("Total Ticket Sales: $", format(total_tickets, ".2f"))