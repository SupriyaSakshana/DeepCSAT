
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



# Dataset Info
# Get a concise summary of the dataset
print("🔹 Dataset Information:")
print(df.info())



# Check data types and non-null counts
print("\n🔹 Data Types and Non-Null Values:")
print(df.dtypes)


# Missing Values/Null Values Count


# Count total missing values per column
missing_values = df.isnull().sum()

print("🔹 Missing Values Count per Column:")
print(missing_values)

# Count total missing values in the dataset
total_missing = missing_values.sum()
print(f"\n🧾 Total Missing Values in the Dataset: {total_missing}")

# Check if any column has missing values
if total_missing == 0:
    print("✅ No missing values found in the dataset.")
else:
    print("⚠️ Missing values detected — consider handling them in preprocessing.")





    # Visualizing the missing values
import matplotlib.pyplot as plt

missing_counts = df.isnull().sum()

plt.figure(figsize=(5,3))
missing_counts.plot(kind='bar', color='blue')
plt.title('Missing Values Count per Column')
plt.xlabel('Columns')
plt.ylabel('Number of Missing Values')
plt.show()


# Check Unique Values for each variable.
print("🔹 Unique Value Count for Each Column:\n")

for column in df.columns:
    unique_count = df[column].nunique()
    print(f"{column}: {unique_count} unique values")



    # Optional: Display sample unique values for categorical columns
print("\n🔹 Sample Unique Values (for categorical columns):\n")
for column in df.select_dtypes(include='object').columns:
    print(f"{column}: {df[column].unique()[:5]}")  # Show first 5 unique values only



    # Write your code to make your dataset analysis ready.

# 1. Remove duplicate rows (if any)
df = df.drop_duplicates()
print("✅ Duplicates removed (if any).")





# 2. Handle missing values — fill or drop based on column type
# Example: Fill numeric with mean, categorical with mode
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].mean())
print("✅ Missing values handled.")




# 3. Convert date columns to datetime format
date_cols = ['order_date_time', 'Issue_reported at', 'issue_responded', 'Survey_response_Date']
for col in date_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')
print("✅ Date columns converted to datetime format.")



# 4. Remove irrelevant columns (if necessary)
# Example: Drop Unique ID or redundant identifiers
df.drop(columns=['Unique_id', 'Order_id'], inplace=True, errors='ignore')
print("✅ Irrelevant columns removed.")





# 5. Confirm data readiness
print("\n🔍 Dataset is now cleaned and ready for analysis!")
print(df.info())






#Verifying How many null values are present in each columns:
df_missing_values = df.isna().sum().sort_values(ascending=False).reset_index()

#Rename columns
df_missing_values.columns = ['Items', 'Missing_Value_Count']

print("Missing values per column after handling:")
print(df_missing_values)




# Chart - 1 visualization code


# ===============================
#  Chart - 1: CSAT Score Distribution
# ===============================

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8,5))
sns.countplot(data=df, x='CSAT Score', hue='CSAT Score', palette='viridis', legend=False)
plt.title('📊 Distribution of CSAT Scores', fontsize=14)
plt.xlabel('CSAT Score')
plt.ylabel('Count of Customers')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()




# Chart - 2 visualization code

# ===============================
#: Average CSAT Score by Channel Name
# ===============================

plt.figure(figsize=(10,6))
channel_avg = df.groupby('channel_name')['CSAT Score'].mean().sort_values(ascending=False)

sns.barplot(x=channel_avg.index, y=channel_avg.values, palette='coolwarm')
plt.title('Average CSAT Score by Channel Name', fontsize=14)
plt.xlabel('Channel Name')
plt.ylabel('Average CSAT Score')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()



