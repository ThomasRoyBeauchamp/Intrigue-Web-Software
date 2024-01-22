from dataclasses import dataclass

from typing import List, Dict


@dataclass
class Relation:
    pull: float
    opinion: int

    HELP = """
    
A relation between two people has two properties. 

The 'pull' describes the rate at which favours can be converted during an Influence Play
The opinion describes the opinion of the target about the source.

Far example, say Alice has the relation Relation(pull = 0.5, opinion = 2) with Bob. 
This means that: 
 1. during an Influence Play any favours owed by Alice can be converted into favours owed by bob at a rate of 2:1.
 2. Bob has an opinion of +2 about Alice 
    
    see also [person]
    """

    def __repr__(self):
        return f"Relation(pull={self.pull}, opinion = {self.opinion})"


class RelationSet(Dict[str, Relation]):

    pass
