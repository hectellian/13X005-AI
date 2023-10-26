from typing import Any, List, Tuple, Callable, Optional, Union

class Node:
    """
    A node in a search tree.
    
    :param state: The state represented by this node.
    :param parent: The parent node of this node.
    :param cost: The cost to reach this node from the start.
    :param h: The heuristic value for this node.
    """
    def __init__(self, state: Any, parent: Optional['Node'] = None, h: float = 0):
        """
        Initialize a node.

        :param state: The state represented by this node.
        :param parent: The parent node of this node.
        :param cost: The cost to reach this node from the start.
        :param h: The heuristic value for this node.
        """
        self.state = state
        self.parent = parent
        self.h = h  # Heuristic value

    def f(self) -> float:
        """
        Get the total estimated cost of the cheapest solution through this node.

        :return: Total estimated cost.
        """
        return self.h

    def __eq__(self, other: 'Node') -> bool:
        """
        Check if this node's state is equal to another node's state.

        :param other: Another node.
        :return: True if both states are equal, False otherwise.
        """
        return self.state == other.state if isinstance(other, Node) else False

    def __lt__(self, other: 'Node') -> bool:
        """
        Compare this node to another node for ordering.

        :param other: Another node.
        :return: True if this node's total cost is less than the other node's total cost.
        """
        return self.f() < other.f()

    def __str__(self) -> str:
        return str(self.state)

    def __repr__(self) -> str:
        return str(self.state)
    
    def __hash__(self) -> int:
        return hash(self.state)
