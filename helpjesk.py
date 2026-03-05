tickets = []
operators = ["Lara", "Mario", "Luigi"]
next_ticket_id = 1

def print_red(message):

    print("")
    print(f"\033[31m{message}\033[0m")
    print("")

def ask_until_valid(get_function, message, error_message):
    
    while True:
        result = get_function(message)

        if result is not None:
            return result
        else:
            print_red(error_message)

def main_menu_choice(mm_message):

    mm_options= ["1", "2", "3", "0"]    

    mm_choice = (input(mm_message)).strip()

    if mm_choice in mm_options:
        return int(mm_choice)
    else:
        return None

def get_priority_choice(prio_message):

    prio_choice = input(prio_message).strip()
    
    if prio_choice == "1":
        return "Low"
    elif prio_choice == "2":
        return "Medium"
    elif prio_choice == "3":
        return "High"
    else:
        return None

def choose_operator(operators):
    while True:    
        for index, name in enumerate(operators, start=1):
            print(f"{index}. {name}")
        
        operator_choice = input("Select an operator or press Enter to skip: ").strip()
        
        if operator_choice == (""):
            operator_choice = "Unassigned"
            return operator_choice
        
        if not operator_choice.isdigit():
            print_red("Error: Invalid operator.")
            continue

        operator_choice = int(operator_choice)
        
        if operator_choice < 1 or operator_choice > len(operators):
            print_red("Error: Invalid operator.")
            continue

        operator_choice = operators[operator_choice - 1]
        return operator_choice

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
    
    priority = ask_until_valid(get_priority_choice, "Choose priority level: 1.Low, 2.Medium, 3.High: ", "Error, invalid choice. Valid options: 1, 2 or 3.")

    choose_operator(operators)
    
    note = input("Add an internal note or press Enter to skip: ").strip()

    notes = []

    if note != "":
        notes.append(note)

    ticket = { # Ticket disctionary
        "id": next_ticket_id,
        "title": title,
        "description": description,
        "status": "New",
        "priority": priority,
        "assigned_to": operator_choice,
        "notes": notes}
    
    tickets.append(ticket)
    next_ticket_id += 1

    # --- Ticket summary print ---

    print("-------------------------------")  
    print("Ticket ID:", ticket["id"])
    print("Title:", ticket["title"])
    print("Description:", ticket["description"])
    print("Priority:", ticket["priority"])
    print("Assigned to:", ticket["assigned_to"])
    if ticket["notes"]:
        print("Notes:")
        for note in ticket["notes"]:
            print("-", note)
    return
               
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
                
                details_sub_choice = input("Choose an option: ").strip()
                
                if details_sub_choice == "":
                    return
                if details_sub_choice == "1":
                    print("Edit function under construction")
                    continue #temporary
                elif details_sub_choice == "2":
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

def main():
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

        mm_choice = main_menu_choice("Choose an option: ")

        if mm_choice == 1:
            create_ticket()
        elif mm_choice == 2:
            view_tickets()
        elif mm_choice == 3:
            edit_ticket()
        elif mm_choice == 0:
            break
        else:
            print_red("Error: invalid choice, try again")
            continue

main()