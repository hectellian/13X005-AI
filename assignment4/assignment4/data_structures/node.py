class Node:
    """
    Class to represent a node in the decision tree.

    Attributes:
    attribute (str): The attribute used for splitting at this node.
    children (dict): A dictionary mapping attribute values to child nodes or class labels.
    """
    def __init__(self, attribute):
        self.attribute = attribute
        self.children = {}
        
    def __str__(self) -> str:
        """
        Return a string representation of the node.

        Returns:
        str: A string representation of the node.
        """
        return f"Node(attribute={self.attribute}, children={self.children})"
    
    def __repr__(self) -> str:
        """
        Return a string representation of the node.
        
        Returns:
        str: A string representation of the node.
        """
        return self.__str__()
    
    def __eq__(self, other: any) -> bool:
        """
        Compare two nodes.

        Parameters:
        ----------------
        other (any): The other node to compare to.

        Returns:
        ----------------
        bool: Whether the two nodes are equal.
        """
        return self.attribute == other.attribute and self.children == other.children