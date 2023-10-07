"""
Description: Node Interface for the Research Tree Data Structure

Author: Anthony CHRISTOFOROU
Date: 1-9-2023

This is a module for the AI course project of the University of Geneva.
"""

class Node:
    def __init__(self, state, transition: callable, parent=None):
        self.state = state
        self.transition = transition
        self.parent = parent
        self.children = []
        
    def is_valid(self) -> bool:
        """Check if the current node's state is valid (follows the rules of the game)

        Returns
        -------
        bool
            Validity of the current node's state
        """
        raise NotImplementedError
    
    def extend(self, child: 'Node'):
        """Add a child to the current node

        Parameters
        ----------
        child : Node
            The child to add to the current node
        """
        if child.is_valid():
            self.children.append(child)
    
    def get_ancestry(self) -> list:
        """Get the ancestry of the current node

        Returns
        -------
        list
            The ancestry of the current node
        """
        node, ancestors = self, []
        while node:
            ancestors.insert(0, node)
            node = node.parent
        return ancestors
    
    def next(self, gamma: callable) -> 'Node':
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
        return NotImplementedError
    
    def spawn_valid_children(self) -> list:
        """Spawn all valid children of the current node

        Returns
        -------
        list
            The valid children of the current node
        """
        raise NotImplementedError
    
    def __eq__(self, other: 'Node') -> bool:
        return self.state == other.state
    
    def __str__(self) -> str:
        return str(self.state)
    
    def __repr__(self) -> str:
        return str(self.state)