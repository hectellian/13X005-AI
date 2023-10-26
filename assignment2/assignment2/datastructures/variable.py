from typing import List, Dict, Any, Optional, Tuple, TypeVar

T = TypeVar('T')

class Variable:
    """
    Represents a variable in a CSP problem.
    """
    def __init__(self, name: str, domain: List[T]):
        """
        Initializes a new Variable.
        
        :param name: Name of the variable.
        :param domain: List of possible values this variable can take.
        """
        self.name = name
        self.domain = domain[:]
        self.assigned_value: Optional[T] = None
    
    def is_assigned(self) -> bool:
        """
        Checks if the variable has an assigned value.
        
        :return: True if variable is assigned, False otherwise.
        """
        return self.assigned_value is not None