from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

V = TypeVar('V') # for variabletyp
D = TypeVar('D') # for domaintyp

# Construct for all conditions
class Constraint(Generic[V, D], ABC):
    # Variables between which the condition exists
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables


    # has to be overwritten by sub-class
    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        ...

