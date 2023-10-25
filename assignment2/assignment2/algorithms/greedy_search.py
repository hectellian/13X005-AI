from assignment2.datastructures.node import Node

from typing import List, Tuple, Any, Callable
import heapq # Priority queue

class GreedyBestFirstSearch:
    def __init__(self, goal_test: Callable[[Any], bool], successors: Callable[[Any], List[Tuple[Any, float]]], heuristic: Callable[[Any], float]):
        self.goal_test = goal_test
        self.successors = successors
        self.heuristic = heuristic
        self.search_steps = []  # List to store each search step
    
    def execute(self, start: Node, goal_state: Any) -> List[Node]:
        # Priority queue for nodes to explore, prioritized by heuristic value
        frontier = [(self.heuristic(start.state), start)]
        explored = set()  # Set to keep track of explored nodes

        while frontier:
            # Get the node with the lowest heuristic value
            _, current = heapq.heappop(frontier)
            
            # Store the current state of search
            self.search_steps.append(current)

            # Check if current state is the goal state
            if self.goal_test(current.state):
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