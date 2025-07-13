def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def input_error(func):
    def inner (*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Where is the name or phone, bro?"
        except KeyError:
            return "I`m blind or i can`t find it"
        except IndexError:
            return "Enter the argument for the command"
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    name = name.lower()  
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    name = name.lower() 
    if name in contacts:
        contacts[name] = phone
        return "Contact updated, bro!"
    else:
        return "I can't find this contact, sorry!!!"

@input_error    
def show_all(contacts):
    if not contacts:
        return "There are no contacts yet."
    result = ""
    for name, phone in contacts.items():
        result += f"{name.title()}: {phone}\n"
    return result.strip()

@input_error    
def show_phone(args, contacts):
    name = args[0].lower()
    if name in contacts:
        return f"{name.title()}: {contacts[name]}"
    else:
        return "this is nothing here, sry."

def show_help():
    return (
        "Available commands:\n"
        "  hello                   - Greet the bot\n"
        "  add <name> <phone>      - Add a new contact\n"
        "  change <name> <phone>   - Change the phone number for an existing contact\n"
        "  phone <name>            - Show the phone number of a contact\n"
        "  show all                - Show all contacts\n"
        "  help                    - Show this help message\n"
        "  close / exit            - Exit the assistant"
    )

def main():
    print("Welcome to the super duper terminal bot")
    contacts = {} 

    while True:
        user_input = input("Enter command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("See you later!!!")
            break

        elif command == "hello":
            print("What can I do for you, bro?")

        elif command == "add":
            print(add_contact(args, contacts))  

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "show":
            if args and args[0].lower() == "all":
                print(show_all(contacts))
            else:
                print("To see all contacts, type: show all")

        elif command == "help":
            print(show_help())
        else:
            print("something wrong.")

if __name__ == "__main__":
    main()