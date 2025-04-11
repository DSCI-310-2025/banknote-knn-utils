# Banknote KNN Utils

[![PyPI version](https://img.shields.io/badge/pypi-v0.1.5-blue.svg)](https://pypi.org/project/banknote-knn-utils/)
[![Python versions](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://pypi.org/project/banknote-knn-utils/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

A Python package for banknote classification and analysis utilities, providing tools for data processing, visualization, and modeling focused on banknote authentication.

## Overview

Banknote Utils is a specialized package designed to simplify the process of analyzing and classifying banknote data. It provides a collection of utility functions for common tasks in the banknote authentication workflow, including data preprocessing, visualization, and machine learning model evaluation with a focus on K-Nearest Neighbors (KNN) classification.

## Installation

```bash
pip install banknote-knn-utils
```

## Features

- **Data Handling**:
  - Check and handle missing values in datasets
  - Ensure output directories exist for saving results

- **Visualization Utilities**:
  - Create count tables for class distribution analysis
  - Generate histograms for feature visualization

- **KNN Modeling Tools**:
  - Train KNN models with customizable parameters
  - Evaluate models using cross-validation
  - Visualize cross-validation results
  - Generate comprehensive model evaluation reports

## Usage Examples

### Checking for Missing Values

```python
import pandas as pd
from banknote_utils import check_missing_value

# Load your banknote dataset
data = pd.read_csv('banknote_data.csv')

# Check and handle missing values
clean_data = check_missing_value(data)
```

### Creating Visualizations

```python
from banknote_utils import create_count_table, plot_histogram

# Create a count table of class distribution
create_count_table(data, 'class', output_prefix='results/class_distribution')

# Create histograms for each feature
plot_histogram(data, 'variance', 'class', labels=['Genuine', 'Counterfeit'], 
               output_prefix='results/histograms')
```

### Training and Evaluating a KNN Model

```python
from banknote_utils import evaluate_knn_cv, plot_knn_cv, train_knn_model, evaluate_model
from sklearn.model_selection import train_test_split

# Prepare your data
X = data.drop('class', axis=1)
y = data['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Find the optimal k value using cross-validation
neighbors, cv_scores, best_k = evaluate_knn_cv(X_train, y_train, k_range=range(1, 21))

# Visualize the cross-validation results
plot_knn_cv(neighbors, cv_scores, output_path='results/knn_cv_plot.png')

# Train the KNN model with the optimal k value
model = train_knn_model(X_train, y_train, best_k)

# Evaluate the model
results = evaluate_model(model, X_test, y_test, output_path='results/confusion_matrix.png')
print(f"Model accuracy: {results['accuracy']:.4f}")
print(results['classification_report'])
```

## API Reference

### Data Handling

- `check_missing_value(bill_data)`: Check and handle missing values in the dataset
- `ensure_output_directory(output_prefix)`: Ensure output directories exist for saving results

### Visualization

- `create_count_table(dataset, target_variable, output_prefix=None)`: Create a count table for class distribution
- `plot_histogram(dataset, feature, target_variable, labels=None, output_prefix=None, figsize=(8, 6))`: Generate histograms for features

### Modeling

- `evaluate_knn_cv(X_train, y_train, k_range=range(1, 26))`: Evaluate different k values using cross-validation
- `plot_knn_cv(neighbors, cv_scores, output_path=None, figsize=(10, 6))`: Plot cross-validation results
- `train_knn_model(X_train, y_train, k)`: Train a KNN classifier with the specified k
- `evaluate_model(model, X_test, y_test, output_path=None, figsize=(6, 5))`: Evaluate a trained model and visualize results

## Ecosystem Context

Banknote Utils fills a specialized niche in the Python machine learning ecosystem by focusing specifically on banknote authentication workflows. While there are many general-purpose machine learning libraries available in Python, this package provides domain-specific utilities that streamline the banknote classification process.

### Related Packages and Differences:

1. **Scikit-learn**: A general-purpose machine learning library that provides the core KNN implementation used by Banknote Utils. Banknote Utils builds upon scikit-learn by adding domain-specific wrappers and visualization tools tailored for banknote authentication.

2. **Pandas**: Provides the core data manipulation capabilities. Banknote Utils extends pandas with specialized functions for handling banknote datasets.

3. **Matplotlib/Seaborn**: General-purpose visualization libraries. Banknote Utils offers pre-configured visualization functions specifically designed for banknote feature analysis.

4. **EDA Packages** (like pandas-profiling): Provide general exploratory data analysis. Banknote Utils focuses specifically on the visualizations and analyses most relevant to banknote authentication.

Unlike these more general packages, Banknote Utils combines functionality from multiple libraries into a streamlined workflow specifically optimized for banknote authentication tasks, reducing the amount of boilerplate code needed for common operations in this domain.

## Requirements

- Python 3.6+
- pandas
- matplotlib
- seaborn
- scikit-learn
- click

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Contact

For questions and feedback, please open an issue on GitHub.
