from assignment2.datastructures.node import Node

from typing import List, Tuple, Any, Callable
import heapq # Priority queue

class GreedyBestFirstSearch:
    def __init__(self, successors: Callable[[Any], List[Tuple[Any, float]]], heuristic: Callable[[Any], float]):
        self.successors = successors
        self.heuristic = heuristic
        self.search_steps = []  # List to store each search step
    
    def execute(self, start: Node, goal_state: Any, logging: bool = False) -> List[Node]:
        # Priority queue for nodes to explore, prioritized by heuristic value
        frontier = [(self.heuristic(start.state), start)]
        explored = set()  # Set to keep track of explored nodes

        while frontier:
            _, current = heapq.heappop(frontier) # Get the node with the lowest heuristic value from the frontier queue

            if current.state == goal_state: #is goeal state
                return self._reconstruct_path(current)

            explored.add(current.state)

            for state in self.successors(current.state):
                if state not in explored:
                    child = Node(state, parent=current)
                    heapq.heappush(frontier, (self.heuristic(state), child))

        return None  # No path found

    def _reconstruct_path(self, node: Node) -> List[Node]:
        """Private method to backtrack and reconstruct the path from the goal to the start."""
        path = []
        while node:
            path.append(node)
            node = node.parent
        return path[::-1]  # Reverse the path for start to goal