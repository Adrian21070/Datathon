# Utility Functions

These are template functions to perform common procedures in a Data Science project. The functions include:

- `impute_na.py`: removes null values from a pandas DataFrame using specified criteria --"median", "mean", "sample", or "drop"--. It can be used for numeric and non-numeric features, though non-numeric support is limited to "drop".
- `outliers.py`: helper function that removes outliers from the dataset. It takes a pandas DataFrame, Series, or NumPy array as an input, and returns their respective type (e.g, if the input is a Series, it will return a Series). **A word of warning for ordinal features, since that will likely return an empty dataset**.
- `perform_pca.py`: you guessed it, it performs standard PCA dimensionality reduction implementation by Scikit-learn. Takes in a pandas DataFrame, spits out the same but transformed. It automatically drops null values and performs the transformation on numerical values.
- `power_transform.py`: function that transforms the specified distributions with a power transformation, either logarithmic ("log") or Box-Cox ("boxcox"). It receives a pandas DataFrame as input and returns the same but transformed. If no column is specified for the DataFrame, it will perform the transformation for all numeric columns.