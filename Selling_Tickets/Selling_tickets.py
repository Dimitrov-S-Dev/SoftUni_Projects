TICKET_PRICE = 10
tickets_remaining = 100
while tickets_remaining:
    print(f"There are {tickets_remaining} remaining tickets.")
    name = input("What is your name?\n")
    ticket_req = (input(f'How many tickets would like to order {name}?\n'))
    try:
        ticket_req = int(ticket_req)
        if ticket_req > tickets_remaining:
            raise ValueError(f'There are only {tickets_remaining} remaining')
    except ValueError as err:
        print(f"Oh no we run into issue. Please try again.")
    else:
        total_cost = TICKET_PRICE * ticket_req
        print(f"Total cost of requested tickets is: ${total_cost}")
        answer = input("Would you like to purchase them? Y/N \n")
        if answer.lower() == "y":
            print(f"SOLD!")
            tickets_remaining -= ticket_req
        else:
            print("Thank you for visiting {name}.")


print(f"Sorry the tickets are all SOLD OUT!!!")
