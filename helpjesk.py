tickets = []
operators = ["Lara", "Mario", "Luigi"]
next_ticket_id = 1

def print_error(error):
    # Skriver ut felmeddelanden i rött (ANSI escape codes).

    print("")
    print(f"\033[31m{error}\033[0m")
    print("")

def ask_until_valid(get_function, message, print_error_message): # generic loop
    while True:
        result = get_function(message)

        if result is not None:
            return result
        else:
            print_error(print_error_message)

def get_priority(prio_message):

    prio_choice = input(prio_message).strip()
    
    if prio_choice == "1":
        return "Low"
    elif prio_choice == "2":
        return "Medium"
    elif prio_choice == "3":
        return "High"
    else:
        return None

def find_ticket_by_id(tickets, ticket_id):
        
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket
    return None


def create_ticket():
    global next_ticket_id
    print("")
    print("-------------------------------")
    print("   CREATE NEW TICKET")
    print("-------------------------------") 
    title = input("Enter ticket title: ") # Ticket title entry
    
    description = input("Describe problem: ") # More detailed description
    
    priority = ask_until_valid(get_priority, "Choose priority level: 1.Low, 2.Medium, 3.High: ", "Error, invalid choice. Valid options: 1, 2 or 3.")

    ticket = { # Ticket disctionary
        "id": next_ticket_id,
        "title": title,
        "description": description,
        "status": "New",
        "priority": priority,
        "assigned_to": "Unassigned",
        "notes": []}
    
    tickets.append(ticket)
    next_ticket_id += 1

    # --- Ticket summary print ---

    print("-------------------------------")  
    print("Ticket ID:", ticket["id"])
    print("Title:", title)
    print("Description:", description)
    print("Priority:", priority)
    print("Assigned to:", ticket["assigned_to"])
    
    # --- Post-create options menu ---

    while True:  
        print("-------------------------------")
        print("   TICKET OPTIONS")
        print("-------------------------------")
        print("1. Assign operator | 2. Add note | Enter to return to main menu")

        new_ticket_option = input("Choose an option: ").strip()

        if new_ticket_option == (""):
            return
        if not new_ticket_option.isdigit():
            print("Error: Select 1 or 2, or press Enter to cancel: ")
            continue
        

    # --- Option 1: Assign operator ---

        if new_ticket_option == ("1"):

            print("-------------------------------")
            print("   ASSIGN OPERATOR")
            print("-------------------------------")  
            while True:    
                for index, name in enumerate(operators, start=1):
                    print(f"{index}. {name}")
                
                op_choice = input("Select an operator or press Enter to cancel: ").strip()
                
                if op_choice == (""):
                    break
                if not op_choice.isdigit():
                    print("Error: Invalid operator.")
                    continue
                op_choice = int(op_choice)
                if op_choice < 1 or op_choice > len(operators):
                    print("Error: Invalid operator.")
                    continue
                
                ticket["assigned_to"] = operators[op_choice - 1]

                print("Assigned operator:", ticket["assigned_to"])
                break
        
    # --- Option 2: Add note ---

        elif new_ticket_option == ("2"):
            print("add note under construction")
               


def view_tickets():  
    if tickets == []:
        print("No tickets found.")
        input("Press Enter to return to main menu")
        return  
    
    # --- Print compact list ---

    else:
        print("")
        print("-------------------------------")
        print("   EXISTING TICKETS")
        print("-------------------------------")

        for ticket in tickets:
            print(f"Ticket ID: {ticket['id']} | Title: {ticket['title']} | Status: {ticket['status']} | Priority: {ticket['priority']} | Assigned to: {ticket['assigned_to']}")
        
        # --- Ask for ID ---

        while True:
            view_id = input("Enter ticket ID to view details or Enter for main menu: ").strip()
            if view_id == "":
                return
            
            if not view_id.isdigit():
                print("Error: enter a valid ticket ID.")
                continue
            
            view_id = int(view_id)
            ticket = find_ticket_by_id(tickets, view_id)
            if ticket is None:
                print("Error: enter a valid ticket ID.")
                continue

            choose_another = False
            
        # --- Print ticket details --- 
            print("")
            print("-------------------------------")
            print("   TICKET DETAILS")
            print("-------------------------------")

            print("Ticket ID:", ticket["id"])
            print("Title:", ticket["title"])
            print("Description:", ticket["description"])
            print("Status:", ticket["status"])
            print("Priority:", ticket["priority"])
            print("Assigned to:", ticket["assigned_to"])
            print("Notes:")
            if not ticket["notes"]:
                print("(none)")
            else:
                for note in ticket["notes"]:
                    print("-", note)
                
            # --- Details sub-menu ---

            while True:
                print("-------------------------------")
                print("   OPTIONS")
                print("-------------------------------")

                print("1. Edit | 2. Back to ticket list | Enter to return to main menu")
                
                det_sub_choice = input("Choose an option: ").strip()
                
                if det_sub_choice == "":
                    return
                if det_sub_choice == "1":
                    print("Edit function under construction")
                    continue #temporary
                elif det_sub_choice == "2":
                    choose_another = True
                    break
                else:
                    print("Error: enter a valid choice.")
                    continue
            
            # --- Reprint Existing Tickets ---
            
            if choose_another == True:
                print("")
                print("-------------------------------")
                print("   EXISTING TICKETS")
                print("-------------------------------")

                for ticket in tickets:
                    print(f"Ticket ID: {ticket['id']} | Title: {ticket['title']} | Status: {ticket['status']} | Priority: {ticket['priority']} | Assigned to: {ticket['assigned_to']}")
            continue


def edit_ticket():
    print("Ticket Editing under construction")
    input("Press Enter to return to main menu")



print("Welcome to HELPJESK version 0.1")
while True:
    print("")
    print("-------------------------------")
    print("   MAIN MENU")
    print("-------------------------------")

    print("1. Create ticket")
    print("2. View all tickets")
    print("3. Edit ticket")
    print("0. Exit ticketing system")

    mm_choice = input("Choose an option: ")
    if mm_choice == "1":
        create_ticket()
    elif mm_choice == "2":
        view_tickets()
    elif mm_choice == "3":
        edit_ticket()
    elif mm_choice == "0":
        break
    else:
        print("Error: invalid choice, try again")
        continue
