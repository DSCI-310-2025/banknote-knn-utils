"""
Banknote Utils
==============

A Python package for banknote classification and analysis utilities, providing tools for data processing,
visualization, and modeling focused on banknote authentication.

This package includes functions for:
- Checking and handling missing values in datasets
- Ensuring output directories exist
- K-Nearest Neighbors (KNN) modeling utilities
- Visualization utilities for exploratory data analysis
"""

__version__ = "0.1.6"

# Import functions from modules
from .check_missing_value import check_missing_value
from .ensure_output_directory import ensure_output_directory
from .modeling_utils import (
    evaluate_knn_cv,
    plot_knn_cv,
    train_knn_model,
    evaluate_model
)
from .visualization_utils import (
    create_count_table,
    create_histogram
)

__all__ = [
    "check_missing_value",
    "ensure_output_directory",
    "evaluate_knn_cv",
    "plot_knn_cv",
    "train_knn_model",
    "evaluate_model",
    "create_count_table",
    "create_histogram"
]