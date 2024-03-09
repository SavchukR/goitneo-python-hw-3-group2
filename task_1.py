
#region Decorators 

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner

def input_error_show_contact(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Give me name please."
        except KeyError:
            return "Contact was not found."

    return inner

#endregion

def parse_input(user_input: str) -> (str, [str]):
    """
        Parse user input from console to command and arguments

        Args:
            user_input (str): command from user.
                Format: {command name} [{arguments}, ...]

        Returns:
            string: command name, array of arguments
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
        
    return cmd, *args


@input_error
def add_contact(args: [str], contacts: {}) -> str:
    """
        Add contact to contact dictionary

        Args:
            args ([str]): contact parameter (expected format: name phone)
            contacts (_type_): contacts catalog

        Returns:
            string: message of contact added
    """
    
    name, phone = args
    
    contacts[name] = phone
    
    return "Contact added."


@input_error
def update_contact(args: [str], contacts: {}) -> str:
    """
        Update contact to contact dictionary

        Args:
            args ([str]): contact parameter (expected format: name phone)
            contacts (_type_): contacts catalog

        Returns:
            string: message of contact updated
    """
    
    name, phone = args
    
    contacts[name] = phone
    
    return "Contact updated."

@input_error_show_contact
def show_contact(args: [str], contacts: {}) -> str:
    """
        Find and show contact in contact dictionary

        Args:
            args ([str]): contact name
            contacts (_type_): contacts catalog

        Returns:
            string: contact phone
    """

    name = args[0]
    
    return f"{contacts[name]}"

def showall_contact(contacts: {}) -> str:
    """
        Return table with all contacts

        Args:
            contacts (_type_): contacts catalog

        Returns:
            str: table with contact information sorted by name
    """
    message = "\n"
    
    len_format = str(min(max([ max(len(key), len(value)) for key, value in (contacts.items()) ] ), 30))
    
    message += ("| {0:-^30} | {0:-^30} |\n").format("-")
    message += ("| {0:^30} | {1:^30} |\n").format("Name", "Phone")
    message += ("| {0:-^30} | {0:-^30} |\n").format("-")
    for name, contact in sorted(contacts.items()):
        message += ("| {0:<30} | {1:^30} |\n").format(name, contact)
    message += ("| {0:-^30} | {0:-^30} |\n").format("-")
    
    return message

def command_helper(command: str) -> str:
    """
        Help user to correctly pick command

    Args:
        command (str): user input command

    Returns:
        str: _description_
    """
    commands = {
        "help": ["--help", "h", "-h"],
        "hello": ["hello", "h", "-h"],
        "add {name} {phone}": ["ad", "plus", "create"],
        "change {name} {phone}": ["change", "update"],
        "phone {name}": ["phone", "show"],
        "all": ["a", "al"],
        "close": ["quit", "close", "q"],
        "exit": ["close"]
    }
    
    similar_command = []
    
    for cmd, names in commands.items():
        if command in names:
            similar_command.append(cmd) 
            
        for name in names:
            if name in command:
                similar_command.append(cmd) 

    guess_str = "\n    ".join(set(similar_command))
    if len(similar_command) == 1:
        return f"The most similar command is \n\n    {guess_str}"
    if len(similar_command) > 1:
        return f"The most similar command are \n\n    {guess_str}"

    return ""

def help() -> str:
    return """

How to use contact manager:

- help - show help

- hello - print hello

- add {name} {phone number} - add name and phone to catalog
- change {name} {phone number} - update phone for name in catalog
- phone {name}  - show phone by name in catalog
- all - show all phones

- exit, close - exit

Could print error in case of missing parameter or invalid action

"""


def main():
    """
        Contact manager (console)
        
        Able to add/change/show user contacts (name & phone) and print all contacts
    """
    contacts = {}
    
    print("Welcome to the assistant bot!")
    
    while True:
        try:
        
            command = input("Enter a command: ")
            command, *args = parse_input(command)
            
            if command == "hello":
                print("How can I help you?")
            
            elif command in ["close", "exit"]:
                print("Good bye!")
                break
            
            elif command == "help":
                print(help())

            # contact commands
            elif command == "add":
                print(add_contact(args, contacts))
                
            elif command == "change":
                print(update_contact(args, contacts))
                    
            elif command == "phone":
                print(show_contact(args, contacts))
                
            elif command == "all":
                print(showall_contact(contacts))
                
            
            # invalid command handler
            else:
                print("Invalid command.")
                
                print(command_helper(command))
            print()
        
        # handle exceptions
        except Exception as e:
            print(f"Unexpected error: {str(e)} - class: {e.__class__}")
        
if __name__ == "__main__":
    main()
