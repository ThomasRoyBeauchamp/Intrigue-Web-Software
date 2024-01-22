from dataclasses import dataclass

from typing import List, Dict

from rich.table import Table

from IntrigueWeb.relations import RelationSet
from rich import print as rprint


class Person(object):

    def __init__(self, name, renown, affiliation):
        self._name = name
        self._renown = renown
        self._affiliation = affiliation
        self._relations = RelationSet()
        self._owed_favours: Dict[str, int] = {}
        self._owed_hooks: Dict[str, int] = {}

    HELP = """
A person has three pieces of identifying information:
1. The name of the person
2. The renown of the person
3. The affiliation of the person

They can also be owed favours and hooks by other people.   

When you show a person's information, you will see that person's information, as well as their relationships/favours owed to them by other people.

This table has the form 

┏━━━━━━━━┳━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Name   ┃ Pull ┃ Opinion ┃ Favours Owed ┃ Hooks Owed ┃
┡━━━━━━━━╇━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ Joseph │ 0.9  │ 10      │ 0            │ 0          │
└────────┴──────┴─────────┴──────────────┴────────────┘

 - 'Pull' is the pull of the person on Name,
 - 'Opinion' is the option of Name about the person
 - 'Favours/Hooks Owed' is the number of favours/hooks owed by Name to the person 

A dash in the pull and opinion column indicates there is no known relation between the parties. 

    see also [favours]
        """



    @property
    def name(self):
        return self._name

    @property
    def renown(self):
        return self._renown

    @property
    def affiliation(self):
        return self._affiliation

    @property
    def relations(self):
        return self._relations

    def __str__(self):
        return f"\n\tName: {self.name}\n\tRenown: {self.renown}\n\tAffiliation: {self.affiliation}\n"

    def __repr__(self):
        return f"Person(name='{self.name}', renown={self.renown}, affiliation='{self.affiliation})'"

    def add_favours(self, target: str, number: int):
        if number < 0:
            raise ValueError

        if target in self._owed_favours:
            self._owed_favours[target] += number

        else:
            self._owed_favours[target] = number

    def remove_favours(self, target: str, number: int):
        if number < 0:
            raise ValueError

        if target not in self._owed_favours:
            return

        if number >= self._owed_favours[target]:
            self._owed_favours.pop(target)
        else:
            self._owed_favours[target] -= number

        return

    def print_relations(self):

        table = Table(show_header=True, title="Relations")
        table.add_column("Name")
        table.add_column("Pull")
        table.add_column("Opinion")
        table.add_column("Favours Owed")
        table.add_column("Hooks Owed")

        for person in self.relations:
            table.add_row(*[person, str(self.relations[person].pull), str(self.relations[person].opinion),
                       str(self._owed_favours[person]) if person in self._owed_favours else '0',
                       str(self._owed_hooks[person]) if person in self._owed_hooks else '0'])

        for person in self._owed_favours:
            if person not in self.relations:
                table.add_row(*[person, '-', '-',
                                str(self._owed_favours[person]) if person in self._owed_favours else '0',
                                str(self._owed_hooks[person]) if person in self._owed_hooks else '0'])

        for person in self._owed_hooks:
            if person not in self.relations and person not in self._owed_favours:
                table.add_row(*[person, '-', '-', '0',
                                str(self._owed_hooks[person]) if person in self._owed_hooks else '0'])

        rprint(table)


class PersonSet(Dict[str, Person]):

    pass
