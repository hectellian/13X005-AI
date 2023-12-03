import random
import numpy as np
import pandas as pd
from anytree import AnyNode, RenderTree

from assignment4.utils import (information_gain, gini_index,)
from assignment4.data_structures.node import Node

class ID3DecisionTree:
	"""
	Implementation of the ID3 decision tree algorithm.

	This class creates a decision tree for classification based on the Information Gain metric.
	"""
	def __init__(self, use_gini: bool = False):
		self.root = None
		self.use_gini = use_gini
  
	def __str__(self) -> str:
		"""
		Return a string representation of the decision tree.

		Returns:
		----------------
		str: A string representation of the decision tree.
		"""
		return str(self.root)

	def __repr__(self) -> str:
		"""
		Return a string representation of the decision tree.

		Returns:
		----------------
		str: A string representation of the decision tree.
		"""
		return self.__str__()


	def __eq__(self, other: any) -> bool:
		"""
		Compare two decision trees.

		Parameters:
		----------------
		other (any): The other decision tree to compare to.

		Returns:
		----------------
		bool: Whether the two decision trees are equal.
		"""
		return self.root == other.root

	def build_tree(self, data: pd.DataFrame, features: list, target_attribute: str, parent_node: any = None) -> Node | int:
		"""
		Build a decision tree using the ID3 algorithm.

		Parameters:
		----------------
			data (DataFrame): The dataset used for building the decision tree.
			features (list): List of feature names.
			target_attribute (str): The name of the target attribute.
			parent_node (Any): The class value of the parent node for the current branch.

		Returns:
		----------------
			Node: The root node of the decision tree.
		"""
		# If all target values are the same, return this value
		if len(np.unique(data[target_attribute])) <= 1:
			return int(np.unique(data[target_attribute])[0])

		# If the dataset is empty, return the mode target feature value in the original dataset
		if len(data) == 0:
			return int(np.unique(data[target_attribute])[np.argmax(np.unique(data[target_attribute], return_counts=True)[1])])

		# If the feature space is empty, return the mode target feature value of the direct parent node
		if len(features) == 0:
			return parent_node

		parent_node = int(np.unique(data[target_attribute])[np.argmax(np.unique(data[target_attribute], return_counts=True)[1])])
		best_feature = self._find_best_feature(data, features, target_attribute, use_gini=self.use_gini)

		# Create tree
		tree = Node(best_feature)
		features = [i for i in features if i != best_feature]

		# Grow branches under the root node for each value of the best feature
		for value in np.unique(data[best_feature]):
			sub_data = data.where(data[best_feature] == value).dropna()
			subtree = self.build_tree(sub_data, features, target_attribute, parent_node)
			tree.children[int(value)] = subtree

		self.root = tree # is this necessary?
  
		return tree

	def _find_best_feature(self, data: pd.DataFrame, features: list[str], target_attribute: str, use_gini: bool = False) -> str:
		"""
		Find the best feature for splitting the dataset.

		This method can use either Information Gain or Gini Index for selecting the best feature.

		Parameters:
		----------------
		data (DataFrame): The dataset.
		features (list): List of feature names.
		target_attribute (str): The name of the target attribute.
		use_gini (bool): Whether to use Gini Index instead of Information Gain. Default is False.

		Returns:
  		----------
		str: The best feature for splitting the dataset.
		"""
		gini_indices = {feature: gini_index(data, feature, target_attribute) for feature in features}
		information_gains = {feature: information_gain(data, feature, target_attribute) for feature in features}
  
		if use_gini:
			return min(gini_indices, key=gini_indices.get)

		return max(information_gains, key=information_gains.get)

	def _traverse(self, node: Node | int, current_data: dict) -> dict:
		"""
		Recursively traverse the tree to generate a data point.
  
		Parameters:
		-----------
		node (Node): The current node in the decision tree.
		current_data (dict): The current state of the data point being generated.
  
		Returns:
		--------
		dict: A complete data point when a leaf node is reached.
		"""
		if not isinstance(node, Node) or not node.children:
			return node

		branch_value = current_data[node.attribute]
		if branch_value not in node.children:
			branch_value = random.choice(list(node.children.keys()))
  
		return self._traverse(node.children[branch_value], current_data) # next node

	def predict(self, data: pd.DataFrame) -> pd.Series:
		"""
		Predict the class labels for a given dataset.

		Parameters:
		------------
		num_samples (int): The number of data points to generate.

		Returns:
		---------
		Series: A Series containing the generated data points.
		"""
		predictions = []
		for _, row in data.iterrows():
			data_point = self._traverse(self.root, row.to_dict())
			predictions.append(data_point)
   
		return pd.Series(predictions, name="c")

	def render_tree(self):
		"""
		Render the decision tree using RenderTree for visual representation.
		"""
		def convert_to_anytree(node, parent=None, edge_value=None):
			"""
			Recursively convert a Node to an AnyNode.
			"""
			if parent is None:
				current_node = AnyNode(name=node.attribute, parent=parent)
			else:
				intermediate_node = AnyNode(name=f"Value: {edge_value}", parent=parent)
				current_node = AnyNode(name=node.attribute if isinstance(node, Node) else f"Leaf: {bool(node)}", parent=intermediate_node)

			# Recursively convert child nodes
			if isinstance(node, Node):
				for value, child in node.children.items():
					convert_to_anytree(child, parent=current_node, edge_value=value)

			return current_node

		# Convert the root of the ID3 tree
		anytree_root = convert_to_anytree(self.root)

		for pre, fill, node in RenderTree(anytree_root):
			print(f"{pre}{node.name}")

