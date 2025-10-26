import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

def load_data():
    """Loads the Iris dataset and returns it as a pandas DataFrame."""
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species_name'] = df['species'].map(dict(enumerate(iris.target_names)))
    return df

def split_features_target(df):
    """Separates the features (X) and target (y) from the DataFrame."""
    X = df.drop(['species', 'species_name'], axis=1)
    y = df['species']
    return X, y

def train_model(X_train, y_train, random_state=42):
    """Initializes and trains a Decision Tree Classifier."""
    model = DecisionTreeClassifier(random_state=random_state)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Makes predictions and evaluates the model, returning a dictionary of metrics."""
    y_pred = model.predict(X_test)
    
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, average='weighted'),
        "recall": recall_score(y_test, y_pred, average='weighted')
    }
    return metrics