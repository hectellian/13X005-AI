"""
Description: BFSTree Algorithm Implementation

Author: Anthony CHRISTOFOROU
Date: 1-9-2023

This is a module for the AI course project of the University of Geneva.
"""

from collections import deque
import matplotlib.pyplot as plt
import networkx as nx

class BFSTree:
    def __init__(self, root):
        self.root = root
        self.G = nx.DiGraph()
        self.G.add_node(str(self.root))
        self.visited = set()

    def bfs(self, goal_state):
        """Breadth First Search Algorithm

        Parameters
        ----------
        goal_state : tuple
            The goal state to reach
        """
        queue = deque([self.root]) # Use a deque to implement a FIFO queue
        self.visited.add(self.root.state) # Keep track of visited states (kinda hash table)
        path_to_goal = None

        while queue:
            current_node = queue.popleft() # Pop the leftmost element of the queue

            if current_node.state == goal_state:
                path_to_goal = current_node.get_ancestry()
                break

            for child in current_node.spawn_valid_children(): # Spawn all valid children of the current node
                if child.state not in self.visited:
                    queue.append(child)
                    self.visited.add(child.state) # Add the child to the visited states
                    current_node.extend(child) # Add the child to the current node's children
                    
                    self.G.add_edge(str(current_node), str(child))
        
        return path_to_goal

    def visualize(self, path_to_goal):
        pos = nx.spring_layout(self.G, k=0.15, iterations=20) # positions for all nodes
        nx.draw(self.G, pos, with_labels=True, font_weight='bold', node_color='skyblue', node_size=700, font_size=6)

        if path_to_goal:
            edges_in_path = [(str(path_to_goal[i]), str(path_to_goal[i + 1])) for i in range(len(path_to_goal) - 1)]
            nx.draw_networkx_edges(self.G, pos, edgelist=edges_in_path, edge_color='r', width=2, alpha=0.6)

        plt.show()