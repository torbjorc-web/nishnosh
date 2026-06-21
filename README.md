# Familiar: A Study In Data Analysis

This project is part of Machine Learning Foundations and explores data from a fictional blood transfusion startup called **Familiar**. The goal is to analyze subscriber lifespan data and iron level survey data in order to answer business questions about product effectiveness and side effects.

## Project Goals

The analysis focuses on three main questions:

1. Does the **Vein Pack** improve subscriber lifespan compared with the general population average?
2. Is the **Artery Pack** different from the Vein Pack in terms of lifespan?
3. Is there an association between pack type and iron level?

## Datasets

The project uses two CSV files:

- `familiar_lifespan.csv`
- `familiar_iron.csv`

These are loaded into pandas DataFrames:

```python
import pandas as pd
import numpy as np

lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')
```

## Analysis Steps

### 1. Vein Pack Lifespan
- Filtered the `lifespans` dataset to extract Vein Pack subscribers.
- Calculated the average lifespan.
- Performed a one-sample t-test against the population mean of 73 years.

### 2. Artery Pack Lifespan
- Filtered the `lifespans` dataset to extract Artery Pack subscribers.
- Calculated the average lifespan.
- Performed an independent two-sample t-test comparing Vein Pack and Artery Pack lifespans.

### 3. Iron Level Association
- Used the `iron` dataset to study side effects.
- Built a contingency table with `pd.crosstab()`.
- Performed a chi-square test to check whether pack type and iron level are associated.

## Statistical Tests Used

- `ttest_1samp()` for comparing a sample mean to a known value.
- `ttest_ind()` for comparing two independent samples.
- `chi2_contingency()` for testing association between categorical variables.

## How to Run

1. Make sure the CSV files are in the same directory as your Python script.
2. Run the script in a Python environment with these packages installed:
   - pandas
   - numpy
   - scipy
3. Execute the analysis script to print the results.

## Expected Output

The script prints:

- The first few rows of each dataset.
- Mean lifespan for Vein Pack subscribers.
- Mean lifespan for Artery Pack subscribers.
- P-values for all statistical tests.
- A contingency table for pack type vs iron level.

## Conclusion

This project helps Familiar evaluate whether its products have meaningful effects on lifespan and iron levels. The results can support product decisions, marketing claims, and customer guidance.
