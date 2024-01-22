from dataclasses import dataclass

from typing import List, Dict


@dataclass
class Relation:
    pull: float
    opinion: int

    def __repr__(self):
        return f"Relation(pull={self.pull}, opinion = {self.opinion})"


class RelationSet(Dict[str, Relation]):

    pass
