"""
Description: Node Class for the Research Tree Data Structure (Hanoi Towers Problem)

Author: Anthony CHRISTOFOROU
Date: 1-9-2023

This is a module for the AI course project of the University of Geneva.
"""
from src.nodes.node_interface import Node
from typing import Tuple

class HanoiNode(Node):
    def __init__(self, state, n: int, transition: callable, parent=None):
        super().__init__(state, transition, parent)
        self.n = n

    def is_valid(self) -> bool:
        """Check if the current node's state is valid (follows the rules of the game)

        Returns
        -------
        bool
            Validity of the current node's state
        """
        # state (X, Y, X) where X, Y, Z are lists of integers representing the disks on each tower 
        # (e.g. [1, 2, 3] means that the tower has 3 disks, the smallest one being 1 and the largest one being 3)
        x, y, z = self.state
        return all(x[i] < x[i + 1] for i in range(len(x) - 1)) and \
                all(y[i] < y[i + 1] for i in range(len(y) - 1)) and \
                all(z[i] < z[i + 1] for i in range(len(z) - 1))
    
    def next(self, gamma: callable) -> 'HanoiNode':
        """Spawn a new node from the current node using the given gamma function

        Parameters
        ----------
        gamma : callable
            Lambda function to apply to the current node's state

        Returns
        -------
        Node
            The new node spawned from the current node
        """
        return HanoiNode(gamma(self.state), self.n, self.transition, self)

    def children(self) -> list:
        """Spawn all valid children of the current node

        Returns
        -------
        list
            List of all valid children of the current node
        """
        children = []
        values = [(i, j) for i in range(self.n) for j in range(self.n) if i != j] # All moves (i, j) where i != j
        for i, j in values:
            gamma = self.transition(i, j)
            child = self.next(gamma)
            if child.is_valid():
                children.append(child)
        return children