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
        
    def __str__(self):
        """
        Return a string representation of the node.

        Returns:
        str: A string representation of the node.
        """
        return self.as_tree()

    def as_tree(self, level=0):
        """
        Generate a string representation of the tree with proper indentation for each level.

        Parameters:
        level (int): The current level in the tree.

        Returns:
        str: A string representation of the tree.
        """
        indent = "    " * level
        child_indent = "    " * (level + 1)
        result = f"{indent}Node: {self.attribute}\n"

        for i, (value, child) in enumerate(self.children.items()):
            connector = "└── " if i == len(self.children) - 1 else "├── "
            result += f"{child_indent}{connector}Value: {value}\n"

            if isinstance(child, dict):
                nested_node = Node(child['attribute'])
                nested_node.children = child['children']
                result += nested_node.as_tree(level + 2)
            elif isinstance(child, Node):
                result += child.as_tree(level + 2)
            else:
                result += f"{child_indent}    └── Leaf: {child}\n"

        return result