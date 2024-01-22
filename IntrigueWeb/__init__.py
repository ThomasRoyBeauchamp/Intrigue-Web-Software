
from IntrigueWeb.people import Person, PersonSet
from IntrigueWeb.relations import Relation, RelationSet

from typing import Optional

class Web:


    def __init__(self, name: str):
        self._name = name
        self._members = PersonSet()

    @property
    def members(self):
        return self._members


    @property
    def name(self):
        return self._name

    def add_member(self, name: Optional[str] = None, renown: Optional[int] = None, affiliation: Optional[str] = None):
        while True:
            if name is None:
                name = input("Name: ")
            else:
                print(f"Name: {name}")
            if renown is None:
                renown = int(input("Renown: ").strip())
            else:
                print(f"Renown: {renown}")
            if affiliation is None:
                affiliation = input("Affiliation: ")
            else:
                print(f"Affiliation: {affiliation}")


            new_member = Person(name, renown, affiliation)

            decision = input(f"Adding person: {new_member} Continue (Y), Restart (R) or cancel (N): ")[0].upper()

            match decision:
                case 'Y':
                    self._members[new_member.name] = new_member
                    print(f"Added {new_member.name}")
                    return
                case 'R':
                    continue
                case _:
                    print('Cancelling...')
                    return

    def add_relation(self):

        while True:
            source = input("Source: ")
            target = input("Target: ")

            if source not in self.members:
                decision = input(f"{source} is not known. Would you like to add them (Y), "
                                 f"Restart(R) or Cancel (N): ")
                decision = decision[0].upper() if decision != '' else ''

                match decision:
                    case 'Y':
                        self.add_member(name=source)

                    case 'R':
                        continue
                    case _:
                        return
            if target not in self.members:
                decision = input(f"{target} is not known. Would you like to add them (Y), "
                                 f"Restart(R) or Cancel (N): ")[0].upper()
                match decision:
                    case 'Y':
                        self.add_member(name=target)
                    case 'R':
                        continue
                    case _:
                        return

            old_relation = None

            if target in self.members[source].relations:
                decision = input(f"{source} already has a relationship with {target}. Would you like to overwrite it (Y), "
                                 f"Restart(R) or Cancel (N): ")[0].upper()
                match decision:
                    case 'Y':
                        old_relation = self.members[source].relations.pop(target)
                    case 'R':
                        continue
                    case _:
                        return


            while True:
                try:
                    pull = float(input(f"Pull of {source} on {target}: ").strip())
                    if not (0 < pull < 1):
                        raise ValueError
                    break
                except ValueError:
                    print("Please enter a valid float in (0,1)")
                    continue

            while True:
                try:
                    opinion = int(input(f"Opinion of {target} about {source}:").strip())
                    break
                except ValueError:
                    print("Please enter a integer value")
                    continue



            new_relation = Relation(pull=pull, opinion=opinion)



            decision = input(f"Adding relation: {new_relation} from {source} to {target}. Continue (Y), Restart (R) or "
                                        f"cancel (N): ")[0].upper() if old_relation is None else input(f"Replacing relation {old_relation} from {source} to {target} with {new_relation}. Continue (Y), Restart (R) or "
                                        f"cancel (N): ")[0].upper()
            match decision:
                case 'Y':
                    self.members[source].relations[target] = new_relation
                    return
                case 'R':
                    self.members[source].relations[target] = old_relation
                    continue
                case _:
                    self.members[source].relations[target] = old_relation
                    return

    def add_favours(self):

        while True:
            source = input("Favours owed to: ")
            target = input("Favours owed by: ")
            if source not in self.members:
                decision = input(f"{source} is not known. Would you like to add them (Y), "
                                 f"Restart(R) or Cancel (N): ")[0].upper()
                match decision:
                    case 'Y':
                        self.add_member(name=source)

                    case 'R':
                        continue
                    case _:
                        return
            if target not in self.members:
                decision = input(f"{target} is not known. Would you like to add them (Y), "
                                 f"Restart(R) or Cancel (N): ")[0].upper()
                match decision:
                    case 'Y':
                        self.add_member(name=target)
                    case 'R':
                        continue
                    case _:
                        return

            while True:
                try:
                    fta = int(input(f"Number to add: ").strip())
                    if 0 <= fta:
                        raise ValueError
                    break
                except ValueError:
                    print("Please enter a valid positive integer")
                    continue

            decision = input(f"Adding {fta} favours owed by {target} to {source}. Would you like to add them (Y), "
                             f"Restart(R) or Cancel (N): ")[0].upper()
            match decision:
                case 'Y':
                    self.members[source].add_favours(target, fta)
                case 'R':
                    continue
                case _:
                    return

    def remove_favours(self):

        while True:
            source = input("Favours owed to: ")
            target = input("Favours owed by: ")
            if source not in self.members:
                print(f"{source} is not known")
                return

            if target not in self.members:
                print(f"{target} is not known")
                return

            while True:
                try:
                    fta = int(input(f"Number to remove: ").strip())
                    if 0 <= fta:
                        raise ValueError
                    break
                except ValueError:
                    print("Please enter a valid positive integer")
                    continue

            decision = input(f"Removing {fta} favours owed by {target} to {source}. Would you like to continue (Y), "
                             f"Restart(R) or Cancel (N): ")[0].upper()
            match decision:
                case 'Y':
                    self.members[source].remove_favours(target, fta)
                case 'R':
                    continue
                case _:
                    return











