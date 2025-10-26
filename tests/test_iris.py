import pytest
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Import the functions we want to test
from part2_practical.task1_iris_sklearn.iris_pipeline import (
    load_data,
    split_features_target,
    train_model,
    evaluate_model
)

# A pytest fixture is a reusable setup function for your tests.
# This fixture loads the data once and can be used by multiple tests.
@pytest.fixture(scope="module")
def iris_data():
    """Fixture to load the iris dataset."""
    return load_data()

def test_load_data(iris_data):
    """Tests the data loading function."""
    assert isinstance(iris_data, pd.DataFrame)
    assert not iris_data.empty
    assert "species_name" in iris_data.columns
    assert len(iris_data) == 150

def test_split_features_target(iris_data):
    """Tests the feature/target splitting function."""
    X, y = split_features_target(iris_data)
    
    assert isinstance(X, pd.DataFrame)
    assert isinstance(y, pd.Series)
    assert X.shape[0] == len(y)
    assert 'species' not in X.columns
    assert 'species_name' not in X.columns

def test_train_model(iris_data):
    """Tests the model training function."""
    X, y = split_features_target(iris_data)
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = train_model(X_train, y_train)
    
    assert isinstance(model, DecisionTreeClassifier)
    # A simple check to see if the model has been fitted
    assert hasattr(model, 'tree_')

def test_evaluate_model(iris_data):
    """Tests the model evaluation function."""
    X, y = split_features_target(iris_data)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = train_model(X_train, y_train)
    metrics = evaluate_model(model, X_test, y_test)
    
    assert isinstance(metrics, dict)
    assert "accuracy" in metrics
    assert isinstance(metrics["accuracy"], float)
    assert 0.0 <= metrics["accuracy"] <= 1.0