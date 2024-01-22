from dataclasses import dataclass

from typing import List, Dict

from IntrigueWeb.relations import RelationSet

class Person(object):

    def __init__(self, name, renown, affiliation):
        self._name = name
        self._renown = renown
        self._affiliation = affiliation
        self._relations = RelationSet()
        self._owed_favours: Dict[str, int] = {}
        self._owed_hooks: Dict[str, int] = {}



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


class PersonSet(Dict[str, Person]):

    pass
