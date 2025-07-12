# Chipotle Data Analysis - Ex3: Getting and Knowing Your Data
import pandas as pd

# Step 2: Import the dataset from the given address
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'

# Step 3: Assign it to a variable called users and use 'user_id' as index
users = pd.read_csv(url, sep='|', index_col='user_id')

# Step 4: See the first 25 entries
print("Step 4: First 25 entries:\n", users.head(25))

# Step 5: See the last 10 entries
print("\nStep 5: Last 10 entries:\n", users.tail(10))

# Step 6: What is the number of observations in the dataset?
print("\nStep 6: Number of observations:", users.shape[0])

# Step 7: What is the number of columns in the dataset?
print("\nStep 7: Number of columns:", users.shape[1])

# Step 8: Print the name of all the columns.
print("\nStep 8: Column names:\n", users.columns.tolist())

# Step 9: How is the dataset indexed?
print("\nStep 9: Index info:\n", users.index)

# Step 10: What is the data type of each column?
print("\nStep 10: Data types:\n", users.dtypes)

# Step 11: Print only the occupation column
print("\nStep 11: Occupation column:\n", users['occupation'])

# Step 12: How many different occupations are in this dataset?
print("\nStep 12: Number of unique occupations:", users['occupation'].nunique())

# Step 13: What is the most frequent occupation?
print("\nStep 13: Most frequent occupation:", users['occupation'].value_counts().idxmax())

# Step 14: Summarize the DataFrame
print("\nStep 14: DataFrame summary:\n", users.describe(include='all'))

# Step 15: Summarize all the columns
print("\nStep 15: Summary of all columns:\n", users.describe(include='all'))

# Step 16: Summarize only the occupation column
print("\nStep 16: Occupation summary:\n", users['occupation'].describe())

# Step 17: What is the mean age of users?
print("\nStep 17: Mean age of users:", users['age'].mean())

# Step 18: What is the age with least occurrence?
age_counts = users['age'].value_counts()
least_common_age = age_counts[age_counts == age_counts.min()].index.tolist()
print("\nStep 18: Age(s) with least occurrence:", least_common_age)
