"""
Machine Learning Foundations - Familiar: A Study In Data Analysis
Complete solution for all 13 tasks
"""

# Import libraries
import pandas as pd
import numpy as np

# Load datasets
lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')

# Import statistical tests
from scipy.stats import ttest_1samp, ttest_ind, chi2_contingency

# ============================================================
# What Can Familiar Do For You? (Tasks 1-5)
# ============================================================

# Task 1: View first 5 rows of lifespans dataframe
print("=== Task 1: First 5 rows of lifespans ===")
print(lifespans.head())

# Task 2: Extract vein pack lifespans
vein_pack_lifespans = lifespans[lifespans['pack'] == 'vein']['lifespan']

# Task 3: Calculate and print average lifespan for Vein Pack
vein_mean = np.mean(vein_pack_lifespans)
print("\n=== Task 3: Average Vein Pack Lifespan ===")
print(f"Vein Pack average lifespan: {vein_mean} years")
print(f"Is it longer than 73 years? {vein_mean > 73}")

# Task 4 & 5: Run 1-sample t-test against population mean of 73
print("\n=== Task 4 & 5: 1-Sample T-Test (Vein Pack vs 73 years) ===")
t_stat, p_value_vein = ttest_1samp(vein_pack_lifespans, 73)
print(f"p-value: {p_value_vein}")
print(f"Significantly different from 73 years (threshold 0.05)? {p_value_vein < 0.05}")

# ============================================================
# Upselling Familiar: Pumping Life Into The Company (Tasks 6-9)
# ============================================================

# Task 6: Extract artery pack lifespans
artery_pack_lifespans = lifespans[lifespans['pack'] == 'artery']['lifespan']

# Task 7: Calculate and print average lifespan for Artery Pack
artery_mean = np.mean(artery_pack_lifespans)
print("\n=== Task 7: Average Artery Pack Lifespan ===")
print(f"Artery Pack average lifespan: {artery_mean} years")
print(f"Is it longer than Vein Pack ({vein_mean})? {artery_mean > vein_mean}")

# Task 8 & 9: Run 2-sample t-test between Vein and Artery packs
print("\n=== Task 8 & 9: 2-Sample T-Test (Vein vs Artery Pack) ===")
t_stat2, p_value_artery = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print(f"p-value: {p_value_artery}")
print(f"Significantly different (threshold 0.05)? {p_value_artery < 0.05}")

# ============================================================
# Side Effects: A Familiar Problem (Tasks 10-13)
# ============================================================

# Task 10: View first 5 rows of iron dataframe
print("\n=== Task 10: First 5 rows of iron ===")
print(iron.head())

# Task 11: Create contingency table of pack vs iron
Xtab = pd.crosstab(iron['pack'], iron['iron'])
print("\n=== Task 11: Contingency Table (Pack vs Iron Level) ===")
print(Xtab)

# Task 12 & 13: Run chi-square test for association
print("\n=== Task 12 & 13: Chi-Square Test (Pack vs Iron Association) ===")
chi2, p_value_chi, dof, expected = chi2_contingency(Xtab)
print(f"p-value: {p_value_chi}")
print(f"Significant association (threshold 0.05)? {p_value_chi < 0.05}")

# ============================================================
# SUMMARY OF ALL RESULTS
# ============================================================
print("\n" + "="*60)
print("SUMMARY OF ALL RESULTS")
print("="*60)
print(f"Vein Pack average lifespan: {vein_mean} years (vs 73 population mean)")
print(f"Artery Pack average lifespan: {artery_mean} years (vs Vein Pack {vein_mean})")
print(f"\n1-Sample T-Test p-value (Vein vs 73): {p_value_vein}")
print(f"2-Sample T-Test p-value (Vein vs Artery): {p_value_artery}")
print(f"Chi-Square Test p-value (Pack vs Iron): {p_value_chi}")
