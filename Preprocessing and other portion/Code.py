
# Import Libraries


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Load Dataset

# ===============================
# 2. Load the Dataset
# ===============================

# Replace 'dataset.csv' with your actual dataset file path
df = pd.read_csv('G:\Supriya\Practical\dataset\eCommerce_Customer_support_data.csv')

# Confirm successful load
print("✅ Dataset loaded successfully!")


# ===============================
# 3. First Look at the Dataset
# ===============================

# Display first 5 rows
print("🔹 First 5 rows of the dataset:")
print(df.head())

# Display basic info
print("\n🔹 Dataset Info:")
print(df.info())

# Display statistical summary
print("\n🔹 Statistical Summary:")
print(df.describe())

# Dataset Rows & Columns count


rows, cols = df.shape
print(f"📊 The dataset contains {rows} rows and {cols} columns.")