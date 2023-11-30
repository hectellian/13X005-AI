"""
This file contains utility functions for the assignment.
"""

import pandas as pd
from math import log2

def calculate_entropy(data: pd.DataFrame, column: str) -> float:
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
    entropy = 0
    for count in value_counts:
        probability = count / len(data)
        entropy -= probability * log2(probability)
    return entropy

import numpy as np

def calculate_information_gain(data: pd.DataFrame, split_attribute: str, target_attribute: str) -> float:
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
    total_entropy = calculate_entropy(data, target_attribute)
    vals, counts = np.unique(data[split_attribute], return_counts=True)
    
    weighted_entropy = sum([(counts[i] / sum(counts)) * calculate_entropy(data.where(data[split_attribute] == vals[i]).dropna(), target_attribute) 
                            for i in range(len(vals))])
    
    return total_entropy - weighted_entropy

def calculate_gini_index(data: pd.DataFrame, split_attribute: str, target_attribute: str) -> float:
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
