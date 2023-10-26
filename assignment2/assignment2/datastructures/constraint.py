from assignment2.datastructures.variable import Variable

from typing import List, Dict, Union

class Constraint:
    """
    Represents a constraint in a CSP problem.
    """
    def __init__(self, variables: List[Variable]):
        """
        Initializes a new Constraint.
        
        :param variables: List of variables that are part of this constraint.
        """
        self.variables = variables

    def is_satisfied(self) -> bool:
        """
        Checks if the constraint is satisfied.
        
        :return: True if constraint is satisfied, False otherwise.
        """
        raise NotImplementedError("This method should be overridden by subclass")
    
class HouseConstraint(Constraint):
    def is_satisfied(self) -> bool:
        # Fetch variables involved in this constraint
        var_dict = {var.name: var for var in self.variables}
        C = var_dict.get('C', None)
        F = var_dict.get('F', None)
        P = var_dict.get('P', None)
        
        if C is None or F is None or P is None:
            return True  # Incomplete assignment
        
        if not (C.is_assigned() and F.is_assigned() and P.is_assigned()):
            return True  # Incomplete assignment
        
        c_val, f_val, p_val = C.assigned_value, F.assigned_value, P.assigned_value
        
        # F cannot be in C or adjacent to C
        adjacent_to_C = {1: [2], 2: [1, 3], 3: [2, 4], 4: [3]}
        if f_val == c_val or f_val in adjacent_to_C.get(c_val, []):
            return False
        
        # C and P cannot be on the same side
        if (c_val in [1, 2] and p_val in [1, 2]) or (c_val in [3, 4] and p_val in [3, 4]):
            return False
        
        return True