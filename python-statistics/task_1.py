from ucimlrepo import fetch_ucirepo 
  
# # fetch dataset 
# student_performance = fetch_ucirepo(id=320) 
  
# # data (as pandas dataframes) 
# X = student_performance.data.features 
# y = student_performance.data.targets 
  
# # metadata 
# print(student_performance.metadata) 
  
# # variable information 
# print(student_performance.variables) 

import pandas as pd

# Load the dataset
df = pd.read_csv("data/generated_student_performance.csv", sep=",")

# Step 1: Calculate Mean
mean_G3 = df['G3'].mean()
print(f"Mean of G3 (Final Grades): {mean_G3}")

# Step 2: Calculate Median
median_G3 = df['G3'].median()
print(f"Median of G3 (Final Grades): {median_G3}")

# Step 3: Calculate Mode
mode_G3 = df['G3'].mode()
print(f"Mode of G3 (Final Grades): {mode_G3.values}")

# Step 4: Calculate Variance
variance_G3 = df['G3'].var()
print(f"Variance of G3 (Final Grades): {variance_G3}")

# Step 5: Calculate Standard Deviation
std_dev_G3 = df['G3'].std()
print(f"Standard Deviation of G3 (Final Grades): {std_dev_G3}")

