from assignment2.datastructures.variable import Variable
from assignment2.datastructures.constraint import Constraint

from typing import List, Dict

class CSP:
    """
    Represents a Constraint Satisfaction Problem.
    """
    def __init__(self, variables: List[Variable], constraints: List[Constraint]):
        """
        Initializes a new CSP problem.
        
        :param variables: List of variables in the problem.
        :param constraints: List of constraints in the problem.
        """
        self.variables = variables
        self.constraints = constraints
        self._var_dict: Dict[str, Variable] = {var.name: var for var in variables}
        
    def get_variable(self, name: str) -> Variable:
        """
        Fetches a variable by its name.
        
        :param name: Name of the variable to fetch.
        :return: Variable object.
        """
        return self._var_dict[name]
    
    def is_complete(self) -> bool:
        """
        Checks if the problem assignment is complete.
        
        :return: True if all variables are assigned, False otherwise.
        """
        return all(var.is_assigned() for var in self.variables)
    
    def is_consistent(self) -> bool:
        """
        Checks if the problem assignment is consistent (satisfies all constraints).
        
        :return: True if all constraints are satisfied, False otherwise.
        """
        return all(constraint.is_satisfied() for constraint in self.constraints)