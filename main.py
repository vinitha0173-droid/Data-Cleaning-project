import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data.csv")

# Show first 5 rows
print("First 5 rows:")
print(df.head())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Fill missing values
df = df.ffill()

# Basic info
print("\nData Info:")
print(df.info())

# Statistics
print("\nSummary:")
print(df.describe())

# Average salary
print("\nAverage Salary:", df['Salary'].mean())

# Department wise salary
print("\nDepartment-wise Salary:")
print(df.groupby('Department')['Salary'].mean())

# Gender count
print("\nGender Count:")
print(df['Gender'].value_counts())

# Visualization
sns.histplot(df['Age'])
plt.title("Age Distribution")
plt.show()

df.groupby('Department')['Salary'].mean().plot(kind='bar')
plt.title("Avg Salary by Department")
plt.show()


