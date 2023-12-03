"""
This file contains utility functions for the assignment.
"""

import pandas as pd
import numpy as np
from IPython.display import HTML, display

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

def accuracy(predictions: pd.Series, original_data: pd.DataFrame) -> float:
    """Calculate the accuracy of predictions against actual data.
    
    Parameters
    ----------
    predictions : pd.Series
        The predictions made by the model.
    original_data : pd.DataFrame
        The original dataframe with actual target values.
        
    Returns
    -------
    float
        The accuracy of the predictions.
    """
    correct = (predictions == original_data).sum()
    total = predictions.shape[0]
    return correct / total

def precision(predictions: pd.Series, original_data: pd.DataFrame) -> float:
    """Calculate the precision of predictions against actual data.
    
    Parameters
    ----------
    predictions : pd.Series
        The predictions made by the model.
    original_data : pd.DataFrame
        The original dataframe with actual target values.
        
    Returns
    -------
    float
        The precision of the predictions.
    """
    true_positives = ((predictions == 1) & (original_data == 1)).sum()
    predicted_positives = (predictions == 1).sum()
    return true_positives / predicted_positives if predicted_positives else 0

def recall(predictions: pd.Series, original_data: pd.DataFrame) -> float:
    """Calculate the recall of predictions against actual data.
    
    Parameters
    ----------
    predictions : pd.Series
        The predictions made by the model.
    original_data : pd.DataFrame
        The original dataframe with actual target values.
        
    Returns
    -------
    float
        The recall of the predictions.
    """
    true_positives = ((predictions == 1) & (original_data == 1)).sum()
    actual_positives = (original_data == 1).sum()
    return true_positives / actual_positives if actual_positives else 0

def f1(predictions: pd.Series, original_data: pd.DataFrame) -> float:
    """Calculate the F1 score of predictions against actual data.
    
    Parameters
    ----------
    predictions : pd.Series
        The predictions made by the model.
    original_data : pd.DataFrame
        The original dataframe with actual target values.
        
    Returns
    -------
    float
        The F1 score of the predictions.
    """
    prec = precision(predictions, original_data)
    rec = recall(predictions, original_data)
    return 2 * (prec * rec) / (prec + rec) if (prec + rec) else 0

def render_scores(tree_scores: dict, forest_scores: dict):
    """Displays the performance scores of the decision tree and random forest models.

    Parameters
    ----------
    tree_scores : dict
        A dictionary containing the scores of the decision tree model.
        Should have keys: 'Accuracy', 'Precision', 'Recall', 'F1'.
    forest_scores : dict
        A dictionary containing the scores of the random forest model.
        Should have keys: 'Accuracy', 'Precision', 'Recall', 'F1'.
    """
    html = """
    <style>
        .score-table {
            width: 60%;
            margin-left: auto;
            margin-right: auto;
            border-collapse: collapse;
            text-align: center;
        }
        .score-table th, .score-table td {
            border: 1px solid #dddddd;
            padding: 8px;
        }
        .score-table th {
            background-color: #16537e;
        }
    </style>
    <table class="score-table">
        <tr>
            <th>Metric</th>
            <th>Decision Tree</th>
            <th>Random Forest</th>
        </tr>
    """
    
    for metric in ['Accuracy', 'Precision', 'Recall', 'F1']:
        html += f"<tr><td>{metric}</td><td>{tree_scores.get(metric, 'N/A'):.3f}</td><td>{forest_scores.get(metric, 'N/A'):.3f}</td></tr>"

    html += "</table>"
    display(HTML(html))