

from IntrigueWeb import Web, Relation
from IntrigueWeb.people import Person

import pickle
import os

if __name__ == '__main__':

    while True:
        load_file = input("Enter location of IntrigueWeb to load or blank to start a new web: ")
        if load_file != "":
            if os.path.exists(load_file):
                try:
                    with open(load_file, 'rb') as F:
                        web = pickle.load(F)
                    if isinstance(web, Web):
                        break
                    else:
                        raise FileNotFoundError("")

                except FileNotFoundError:
                    print("File does not exist or is not a pickle of a web file")
                    continue
            else:
                print("File does not exist")
                continue

        else:
            web = Web(input("Enter name for IntrigueWeb: ").strip())
            break

    while True:

        new_command = input(f"IntrigueWeb({web.name})>>>").split(' ')

        match new_command[0]:
            case 'add':
                match new_command[1]:
                    case 'person':
                        web.add_member()
                    case 'relation':
                        web.add_relation()
                    case 'favours' | 'favour':
                        web.add_favours()
                    case _:
                        print(f"Command {' '.join(new_command)} not known")

            case 'remove':
                match new_command[1]:
                    case 'favours' | 'favour':
                        web.remove_favours()
                    case _:
                        print(f"Command {' '.join(new_command)} not known")

            case 'members':
                print(web.members)

            case 'show':
                person = ' '.join(new_command[1:])
                if person in web.members:
                    print(web.members[person])
                    web.members[person].print_relations()
                else:
                    print(f"No such person {person}")

            case 'exit':
                if input("Do you want to save? (Y/N): ").upper() == 'Y':
                    if load_file == '':
                        load_file = 'Webs/'+input(f'Enter file name for IntrigueWeb {web.name}: Webs/')

                    with open(load_file, 'wb') as F:
                        pickle.dump(web, F)

                    print(f"Saved {web.name} to {load_file}")

                quit(0)

            case 'save':
                if load_file == '':
                    load_file = 'Webs/' + input(f'Enter file name for IntrigueWeb {web.name}: Webs/')

                with open(load_file, 'wb') as F:
                    pickle.dump(web, F)

                print(f"Saved {web.name} to {load_file}")

            case "help":
                if len(new_command) == 1:

                    print("""
    Welcome to the Intrigue Web Software!
    
    You can use the following commands to manage your web:
    
    help [|person|relation]:
        This launches this dialog if topic is blank, otherwise it will show the help for the specified topic.
    
    add [person|relation|favour(s)]:
        This launches the dialog to add a person, relation or favours to your web
        
    remove [favours]:
        This launches the dialog to remove favours from your web
        
    members:
        This prints a list of all people currently in the web
    
    show [member]
        Prints a description of 'member' and all their relationships/favours owed
        
    save 
        Saves your Intrigue Web 
        
    exit
        Quits the Intrigue Web software. 
    
    
                    
                    
                    """)
                else:
                    match new_command[1]:
                        case 'person':
                            print(Person.HELP)
                        case 'relation':
                            print(Relation.HELP)
                        case _:
                            print(f"No help dialog available for {new_command[1]}")


            case _:
                print(f"Command {' '.join(new_command)} not known")