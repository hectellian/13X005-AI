import numpy as np

class LogisticRegressionClassifier:
    def __init__(self):
        self.weights = None
        self.bias = None

    def sigmoid(self, z):
        """ Sigmoid function implementation. """
        return 1 / (1 + np.exp(-z))

    def train(self, X, y, num_iters, learning_rate):
        """ Train the Logistic Regression model using gradient descent. """
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        # Gradient descent
        for _ in range(num_iters):
            model = self.sigmoid(np.dot(X, self.weights) + self.bias)
            dw = (1 / n_samples) * np.dot(X.T, (model - y))
            db = (1 / n_samples) * np.sum(model - y)

            self.weights -= learning_rate * dw
            self.bias -= learning_rate * db

    def predict(self, X):
        """ Predict class labels for samples in X. """
        linear_model = np.dot(X, self.weights) + self.bias
        y_predicted = self.sigmoid(linear_model)
        y_predicted_cls = [1 if i > 0.5 else 0 for i in y_predicted]
        return np.array(y_predicted_cls)

    def __str__(self) -> str:
        """Return a string representation of the Logistic Regression Classifier."""
        output = ["Logistic Regression Classifier Summary:"]
        output.append("-" * 50)
        weights_str = ', '.join(f"{w:.4f}" for w in self.weights)
        output.append(f"Weights: [{weights_str}]")
        output.append(f"Bias: {self.bias:.4f}")
        return "\n".join(output)
    
    def __repr__(self) -> str:
        """Return a string representation of the Logistic Regression Classifier."""
        return (f"LogisticRegressionClassifier(weights={self.weights}, bias={self.bias})")