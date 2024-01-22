

from IntrigueWeb import Web


if __name__ == '__main__':

    load_file = input("Enter location of IntrigueWeb to load or blank to start a new web: ")
    if load_file != "":
        raise NotImplementedError

    else:
        web = Web(input("Enter name for IntrigueWeb: ").strip())

    while True:

        new_command = input(f"IntrigueWeb({web.name})>>>").lower().split(' ')

        match new_command[0]:
            case 'add':
                match new_command[1]:
                    case 'person':
                        web.add_member()
                    case 'relation':
                        web.add_relation()

            case 'print':
                print(web.members)

            case 'exit':
                quit(0)

            case _:
                print(f"Command {' '.join(new_command)} not known")