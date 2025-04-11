Basic Usage Examples
==================

This guide demonstrates the basic usage of the ``banknote_utils`` package.

Data Processing Examples
-----------------------

Checking for Missing Values
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import pandas as pd
    from banknote_utils import check_missing_value

    # Create a sample dataframe with missing values
    df = pd.DataFrame({
        'feature1': [1, 2, None, 4],
        'feature2': [5, None, 7, 8]
    })

    # Check for missing values
    missing_count = check_missing_value(df)
    # Output: Found 2 missing values in the data.
    #         Column feature1: 1 missing values
    #         Column feature2: 1 missing values

Ensuring Output Directory Exists
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from banknote_utils import ensure_output_directory

    # Ensure a directory exists before saving files
    ensure_output_directory("results/figures/plot.png")
    # This will create the directories 'results' and 'results/figures' if they don't exist


Modeling Examples
---------------

KNN Cross-Validation
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import pandas as pd
    from sklearn.model_selection import train_test_split
    from banknote_utils import evaluate_knn_cv, plot_knn_cv, train_knn_model

    # Load your dataset
    df = pd.read_csv("banknote_data.csv")
    X = df.drop("class", axis=1)
    y = df["class"]

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    # Evaluate different k values using cross-validation
    neighbors, cv_scores, best_k = evaluate_knn_cv(X_train, y_train, k_range=range(1, 21))
    
    # Plot the cross-validation results
    plot_knn_cv(neighbors, cv_scores, output_path="knn_cv.png")
    
    # Train the final model with the best k
    model = train_knn_model(X_train, y_train, best_k)


Model Evaluation
~~~~~~~~~~~~~~

.. code-block:: python

    from banknote_utils import evaluate_model

    # Evaluate the model and generate visualizations
    results = evaluate_model(model, X_test, y_test, output_path="confusion_matrix.png")
    
    # Access the evaluation results
    print(f"Test accuracy: {results['accuracy']}")
    print("Confusion matrix:")
    print(results['confusion_matrix'])
    
    # Save the classification report
    results['classification_report'].to_csv("classification_report.csv")


Visualization Examples
--------------------

Creating a Count Table
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import pandas as pd
    from banknote_utils import create_count_table

    # Create a sample dataframe
    df = pd.DataFrame({
        'class': [0, 1, 0, 0, 1, 1, 0]
    })

    # Create a count table
    count_table = create_count_table(df, 'class', save_path="class_counts.csv")
    print(count_table)

Creating Histograms
~~~~~~~~~~~~~~~~~

.. code-block:: python

    import pandas as pd
    from banknote_utils import create_histogram

    # Create a sample dataframe
    df = pd.DataFrame({
        'feature': [1.2, 2.3, 1.8, 0.9, 2.2, 1.5, 1.9],
        'class': [0, 1, 0, 0, 1, 1, 0]
    })

    # Create a histogram with class distribution
    create_histogram(df, 'feature', 'class', output_path="feature_histogram.png")