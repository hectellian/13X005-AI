from assignment2.datastructures.variable import Variable
from assignment2.datastructures.csp import CSP

from typing import Callable, List, Tuple, Any, Dict, Optional

class BacktrackingSolver:
    """
    Solves a CSP problem using backtracking with forward checking.
    """
    def __init__(self, csp: CSP):
        """
        Initializes a new BacktrackingSolver.
        
        :param csp: CSP problem to solve.
        """
        self.csp = csp
        self.solutions: List[Dict[str, Any]] = []
    
    def forward_checking(self, var: Variable) -> bool:
        """
        Perform forward checking to prune the domain of unassigned variables.
        
        :param var: Recently assigned variable.
        :return: True if forward checking succeeds, False otherwise.
        """
        for constraint in self.csp.constraints: # for all constraints
            if var in constraint.variables:
                for neighbor in constraint.variables:
                    if not neighbor.is_assigned():
                        new_domain = [value for value in neighbor.domain if constraint.is_satisfied()] # remove values that violate the constraint
                        if len(new_domain) == 0: # if the domain is empty, forward checking fails
                            return False
                        neighbor.domain = new_domain
        return True
    
    def solve(self, collect_all: bool = True) -> List[Dict[str, Any]]:
        """
        Solves the CSP problem using backtracking and collects all solutions.
        
        :param collect_all: If True, collects all solutions. If False, stops after finding the first solution.
        :return: List of dictionaries containing variable assignments for all solutions.
        """
        if self.csp.is_complete(): # if the assignment is complete, add it to the list of solutions
            solution = {var.name: var.assigned_value for var in self.csp.variables} # convert the list of variables to a dictionary
            self.solutions.append(solution)
            return self.solutions if collect_all else [solution]
        
        # Select an unassigned variable
        var = next(filter(lambda x: not x.is_assigned(), self.csp.variables), None) # get the first unassigned variable
        if var is None:
            return []
        
        # Try to assign each value from its domain
        for value in var.domain:
            var.assigned_value = value
            if self.csp.is_consistent():
                if self.forward_checking(var):
                    result = self.solve(collect_all) # recursively solve the problem
                    if result and not collect_all:
                        return result
            var.assigned_value = None
            
        return self.solutions