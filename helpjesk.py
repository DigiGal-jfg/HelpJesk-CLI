import os
import json
import textwrap
tickets = []
operators = ["Lara", "Mario", "Luigi"]
next_ticket_id = 0

def load_tickets_json():
    if os.path.exists("tickets.json"):
        tickets = json.load(open("tickets.json", "r"))
        return tickets
    else:
        tickets = []
        json.dump([], open("tickets.json", "w"))
        return tickets

def save_tickets_json(tickets):
    json.dump(tickets, open("tickets.json","w"), indent=4)

def print_red(message):

    print(f"\033[31m{message}\033[0m")

def print_yellow(message):

    print(f"\033[33m{message}\033[0m")

def print_cyan(message):

    return(f"\033[36m{message}\033[0m")

def wrap_text(message, width):
    lines = (textwrap.wrap(message, width))
    for line in lines:
        print(line)

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
        print("-------------------------------")
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

def load_ticket_id():
    
    if tickets:
        next_ticket = tickets[-1]["id"] + 1
        return next_ticket
    else:
        next_ticket = 1
        return next_ticket

def find_ticket_by_id(tickets, ticket_id):
        
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket
    return None

def print_ticket_summary(ticket):

    print("-------------------------------")  
    print("TICKET ID:", print_cyan(ticket["id"]))
    print("TITLE:", print_cyan(ticket["title"]))
    wrap_text("DESCRIPTION: " + print_cyan(ticket["description"]), width=80)
    print("PRIORITY:", print_cyan(ticket["priority"]))
    print("ASSIGNED TO:", print_cyan(ticket["assigned_to"]))
    if ticket["notes"]:
        print("NOTES:", print_cyan(ticket["notes"][0]))
        for note in ticket["notes"][1:]:
            wrap_text("- " + note, width=80)

def print_tickets_list(tickets):

    for ticket in tickets:
        print(f"TICKET ID: {print_cyan(ticket['id'])}  | TITLE: {print_cyan(ticket['title'])} | STATUS: {print_cyan(ticket['status'])} | PRIORITY: {print_cyan(ticket['priority'])} | ASSIGNED TO: {print_cyan(ticket['assigned_to'])}")    

def get_note(note_message):

    note = input(note_message).strip()
    return note
    
def get_ticket_input(input_message):
    
    result = input(input_message).strip()
    if result == "":
        return None
    else:
        return result

def get_valid_id():
    while True:
        get_id = input("Enter ticket ID to view details or Enter for main menu: ").strip()
        
        if get_id == "":
            return
            
        if not get_id.isdigit():
            print_red("Error: enter a valid ticket ID.")
            continue
            
        get_id = int(get_id)
        ticket = find_ticket_by_id(tickets, get_id)

        if ticket is None:
            print_red("Error: enter a valid ticket ID.")
        else:
            return ticket

def create_ticket():
    
    global next_ticket_id
    print("")
    print("-------------------------------")
    print_yellow("   CREATE NEW TICKET")
    print("-------------------------------") 
    
    title = ask_until_valid(get_ticket_input, "Enter ticket title: ", "Error: enter a title.") # Ticket title entry
    description = ask_until_valid(get_ticket_input, "Describe problem: ", "Error: enter a description.") # More detailed description
    priority = ask_until_valid(get_priority_choice, "Choose priority level: 1.Low, 2.Medium, 3.High: ", "Error: invalid choice. Valid options: 1, 2 or 3.")
    operator_choice = choose_operator(operators)
    note = get_note("Add an internal note or press Enter to skip: ")

    notes = []
    if note != "":
        notes.append(note)

    ticket = { # Ticket dictionary
        "id": next_ticket_id,
        "title": title,
        "description": description,
        "status": "New",
        "priority": priority,
        "assigned_to": operator_choice,
        "notes": notes}
    
    tickets.append(ticket)
    next_ticket_id += 1
    save_tickets_json(tickets)

    # --- Ticket summary print ---

    print_ticket_summary(ticket)
    return
               
def view_tickets():  
    print("")
    print("-------------------------------")
    print_yellow("   EXISTING TICKETS")
    print("-------------------------------")
    
    if tickets == []:
        print_red("No tickets found.")
        return  
    
    else:
        print_tickets_list(tickets)
        
        # --- Ask for ID ---

        while True:
            ticket = get_valid_id()
            if ticket is None:
                return

            choose_another = False
            
        # --- Print ticket details --- 
            
            print_ticket_summary(ticket)
                
            # --- Details sub-menu ---

            while True:
                print("-------------------------------")
                print_yellow("   OPTIONS")
                print("-------------------------------")

                print("1. Edit | 2. Back to ticket list | Enter to return to main menu")
                
                details_sub_choice = input("Choose an option: ").strip()
                
                if details_sub_choice == "":
                    return
                if details_sub_choice == "1":
                    print_yellow("Edit function under construction")
                    continue #temporary
                elif details_sub_choice == "2":
                    choose_another = True
                    break
                else:
                    print_red("Error: enter a valid choice.")
                    continue
            
            # --- Reprint Existing Tickets ---
            
            if choose_another == True:
                print_tickets_list(tickets)
            continue

def edit_ticket():
    print("Ticket Editing under construction")
    input("Press Enter to return to main menu")

def main():
    
    global tickets, next_ticket_id
    tickets = load_tickets_json()
    next_ticket_id = load_ticket_id()

    print("")
    print("Welcome to HELPJESK version 0.3")
    
    while True:
        print("")
        print("-------------------------------")
        print_yellow("   MAIN MENU")
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