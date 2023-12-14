import numpy as np

class NaiveBayesClassifier:
    def __init__(self):
        self.params = {}

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        """ Fit the Naive Bayes model to the training data. 
        
        Parameters
        ----------
        X : np.ndarray
            Training data.
        y : np.ndarray
            Training labels.
        """
        self.classes = np.unique(y)
        self.features = X.shape[1]

        # Calculate parameters for each class
        for c in self.classes:
            X_c = X[y == c]
            self.params[c] = {
                'mean': X_c.mean(axis=0),
                'var': X_c.var(axis=0),
                'prior': X_c.shape[0] / X.shape[0]
            }

    def gaussian_density(self, class_idx: int, x: np.ndarray) -> np.ndarray:
        """ Calculate Gaussian density function for a given class and data point. 
        
        Parameters
        ----------
        class_idx : int
            Index of the class in the list of classes.
        x : np.ndarray
            Data point for which to calculate the Gaussian density function.

        Returns
        -------
        np.ndarray
            Gaussian density function for the given class and data point.
        """
        mean = self.params[class_idx]['mean']
        var = self.params[class_idx]['var']
        numerator = np.exp(- (x - mean) ** 2 / (2 * var))
        denominator = np.sqrt(2 * np.pi * var)
        return numerator / denominator

    def predict(self, X: np.ndarray) -> np.ndarray:
        """ Predict the class labels for the given data points. 
        
        Parameters
        ----------
        X : np.ndarray
            Data points for which to predict the class labels.
            
        Returns
        -------
        np.ndarray
            Predicted class labels for the given data points.
        """
        preds = []
        for x in X:
            posteriors = []

            # Calculate posterior probability for each class
            for c in self.classes:
                prior = np.log(self.params[c]['prior'])
                class_conditional = np.sum(np.log(self.gaussian_density(c, x)))
                posterior = prior + class_conditional
                posteriors.append(posterior)

            # Select the class with the highest posterior probability
            preds.append(np.argmax(posteriors))

        return np.array(preds)
    
    def __str__(self) -> str:
        """Return a string representation of the Naive Bayes classifier."""
        output = ["Naive Bayes Classifier Summary:"]
        output.append("-" * 60)
        output.append(f"{'Class':<10} | {'Prior':<10} | {'Mean':<20} | {'Variance'}")
        output.append("-" * 60)
        for c in self.classes:
            prior_val = f"{self.params[c]['prior']:.4f}"
            mean_vals = ', '.join(f"{m:.2f}" for m in self.params[c]['mean'])
            var_vals = ', '.join(f"{v:.2f}" for v in self.params[c]['var'])
            output.append(f"{c:<10} | {prior_val:<10} | {mean_vals:<20} | {var_vals}")
        return "\n".join(output)

    def __repr__(self) -> str:
        """Return a string representation of the Naive Bayes classifier."""
        return f"NaiveBayesClassifier(n_classes={len(self.classes)})"
