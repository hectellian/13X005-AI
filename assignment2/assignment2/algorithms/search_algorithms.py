from typing import List, Protocol, Any
from assignment2.datastructures.node import Node

class SearchAlgorithm(Protocol):
    def execute(self, start: Node, goal_state: Any) -> List[Node]:
        """Execute the search algorithm and return the path from start to goal."""
        pass
