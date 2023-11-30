import numpy as np
import pandas as pd

from assignment4.utils import (calculate_entropy, calculate_information_gain, calculate_gini_index,)
from assignment4.data_structures.node import Node

class ID3DecisionTree:
	"""
	Implementation of the ID3 decision tree algorithm.

	This class creates a decision tree for classification based on the Information Gain metric.
	"""
	def __init__(self):
		self.root = None
  
	def __str__(self) -> str:
		"""
		Return a string representation of the decision tree.

		Returns:
		----------------
		str: A string representation of the decision tree.
		"""
		return str(self.root)

	def build_tree(self, data: pd.DataFrame, features: list, target_attribute: str, parent_node_class: any = None) -> any:
		"""
		Build a decision tree using the ID3 algorithm.

		Parameters:
		----------------
			data (DataFrame): The dataset used for building the decision tree.
			features (list): List of feature names.
			target_attribute (str): The name of the target attribute.
			parent_node_class (Any): The class value of the parent node for the current branch.

		Returns:
		----------------
			Node: The root node of the decision tree.
		"""
		# If all target values are the same, return this value
		if len(np.unique(data[target_attribute])) <= 1:
			return np.unique(data[target_attribute])[0]

		# If the dataset is empty, return the mode target feature value in the original dataset
		if len(data) == 0:
			return np.unique(data[target_attribute])[np.argmax(np.unique(data[target_attribute], return_counts=True)[1])]

		# If the feature space is empty, return the mode target feature value of the direct parent node
		if len(features) == 0:
			return parent_node_class

		# Default value for this node
		parent_node_class = np.unique(data[target_attribute])[np.argmax(np.unique(data[target_attribute], return_counts=True)[1])]

		# Select the feature that best splits the dataset
		best_feature = self._find_best_feature(data, features, target_attribute)

		# Create the tree structure
		tree = Node(best_feature)
		features = [i for i in features if i != best_feature]

		# Grow branches under the root node for each value of the best feature
		for value in np.unique(data[best_feature]):
			sub_data = data.where(data[best_feature] == value).dropna()
			subtree = self.build_tree(sub_data, features, target_attribute, parent_node_class)
			tree.children[value] = subtree

		self.root = tree # is this necessary?
  
		return tree

	def _find_best_feature(self, data, features, target_attribute, use_gini=False):
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
		best_feature = None
		best_value = -float('inf')

		for feature in features:
			if use_gini:
				value = calculate_gini_index(data, feature, target_attribute)
			else:
				value = calculate_information_gain(data, feature, target_attribute)

			if value > best_value:
				best_value = value
				best_feature = feature

		return best_feature

	def render_tree(self):
		"""Render the tree
		"""
		print(self.root.as_tree())
