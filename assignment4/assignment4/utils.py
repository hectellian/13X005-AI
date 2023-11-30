"""
This file contains utility functions for the assignment.
"""

import pandas as pd
import numpy as np
from math import log2

def entropy(data: pd.DataFrame, column: str) -> float:
    """Calculate the entropy of a given column in a dataframe.
    
    Parameters
    ----------
    data : pd.DataFrame
        The dataframe containing the data.
    column : str
        The column name to calculate the entropy of.
        
    Returns
    -------
    float
        The entropy of the column.
    """
    value_counts = data[column].value_counts() # Counts the occurrence of each class
    probabilities = value_counts / sum(value_counts)
    entropy = sum(probabilities * -np.log2(probabilities))
    
    return entropy


def information_gain(data: pd.DataFrame, split_attribute: str, target_attribute: str) -> float:
    """Calculate the Information Gain of a dataset after splitting on an attribute.
    
    Parameters
    ----------
    data : pd.DataFrame
        The dataframe containing the data.
    split_attribute : str
        The name of the attribute to split on.
    target_attribute : str
        The name of the target attribute.
        
    Returns
    -------
    float
        The Information Gain of the dataset after the split.
    """
    total_entropy = entropy(data, target_attribute)
    vals, counts = np.unique(data[split_attribute], return_counts=True)
    
    weighted_entropy = sum([(counts[i] / sum(counts)) * entropy(data.where(data[split_attribute] == vals[i]).dropna(), target_attribute) 
                            for i in range(len(vals))])
    
    return total_entropy - weighted_entropy

def gini_index(data: pd.DataFrame, split_attribute: str, target_attribute: str) -> float:
    """Calculate the Gini Index of a dataset after splitting on an attribute.

    Parameters
    ----------
    data : pd.DataFrame
        The dataframe containing the data.
    split_attribute : str
        The name of the attribute to split on.
    target_attribute : str
        The name of the target attribute.
        
    Returns
    -------
    float
        The Gini Index of the dataset after the split.
    """
    vals, counts = np.unique(data[split_attribute], return_counts=True)

    # Calculate the weighted Gini index
    weighted_gini = sum([(counts[i] / sum(counts)) * (1 - sum([(len(data[(data[split_attribute] == vals[i]) & (data[target_attribute] == k)]) / counts[i])**2 
                                                              for k in np.unique(data[target_attribute])]))
                         for i in range(len(vals))])
    
    return weighted_gini
