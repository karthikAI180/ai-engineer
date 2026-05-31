import pandas as pd

# Load Titanic dataset from online (no download needed)
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# ==========================================
# Task 1: Load & Basic Exploration
# ==========================================

# Print first 5 rows of dataset
print(df.head())

# Print last 3 rows of dataset
print(df.tail(3))

# Print total rows and columns (rows, columns)
print(df.shape)

# Print all column names
print(df.columns)

# ==========================================
# Task 2: Data Types & Missing Values
# ==========================================

# Print column names, data types and non-null counts
# Shows which columns have missing values
print(df.info())

# Print statistical summary (mean, min, max, std, percentiles)
# Only shows numeric columns
print(df.describe())

# ==========================================
# Task 3: Value Counts
# ==========================================

# Count how many survived (1) vs didn't survive (0)
print(df['Survived'].value_counts())

# Count how many passengers in each class (1, 2, 3)
print(df['Pclass'].value_counts())

# Count how many male vs female passengers
print(df['Sex'].value_counts())

# ==========================================
# Task 4: Filtering (Single Condition)
# ==========================================

# Filter passengers older than 30, show their names
filt = df['Age'] > 30
print(df.loc[filt, 'Name'])

# Filter female passengers, show their names
filt2 = df['Sex'] == 'female'
print(df.loc[filt2, 'Name'])

# Filter passengers who survived (1=survived), show their names
filt3 = df['Survived'] == 1
print(df.loc[filt3, 'Name'])

# ==========================================
# Task 5: Multiple Conditions (&, |, ~)
# ==========================================

# Filter female passengers older than 30 (AND condition)
filt = (df['Age'] > 30) & (df['Sex'] == 'female')
print(df.loc[filt, 'Name'])

# Filter passengers older than 30 AND in class 1 (AND condition)
filt2 = (df['Age'] > 30) & (df['Pclass'] == 1)
print(df.loc[filt2, 'Name'])

# Filter passengers who are female OR survived (OR condition)
filt3 = (df['Sex'] == 'female') | (df['Survived'] == 1)
print(df.loc[filt3, 'Name'])

# ==========================================
# Task 6: loc and iloc
# ==========================================

# Get first row by position (integer location)
print(df.iloc[0])

# Get first 5 rows by position
print(df.iloc[0:5])

# Get row with index label 0 (by label)
print(df.loc[0])

# Get first 5 rows, Name (col 3) and Age (col 5) only
print(df.iloc[0:5, [3, 5]])

# ==========================================
# Task 7: Sorting Data
# ==========================================

# Sort passengers by Age youngest first (ascending)
print(df.sort_values('Age', ascending=True))

# Sort passengers by Age oldest first (descending)
print(df.sort_values('Age', ascending=False))

# Sort by Fare highest first, modify original DataFrame
df.sort_values('Fare', ascending=False, inplace=True)

# Print only Name and Fare columns after sorting
print(df[['Name', 'Fare']])

# ==========================================
# Task 8: set_index & Index Operations
# ==========================================

# Set PassengerId as index (row label)
df.set_index('PassengerId', inplace=True)

# Print the index (shows all PassengerIds)
print(df.index)

# Sort DataFrame by index (PassengerId) ascending
print(df.sort_index())

# Access specific passenger by PassengerId using loc
print(df.loc[1])

# ==========================================
# Task 9: Series Operations
# ==========================================

# Get Age column as a Series (single column)
age_series = df['Age']

# Print type to confirm it's a Series not DataFrame
print(type(age_series))

# Print all Age values
print(age_series)

# Print maximum age (oldest passenger)
print(df['Age'].max())

# Print average age of all passengers
print(df['Age'].mean())

# Print minimum age (youngest passenger)
print(df['Age'].min())

# Count passengers from each embarkation port
# S=Southampton, C=Cherbourg, Q=Queenstown
print(df['Embarked'].value_counts())

# Count number of unique values in Sex column (male, female = 2)
print(df['Sex'].nunique())

# ==========================================
# Task 10: Selecting Multiple Columns
# ==========================================

# Select only 4 columns and store in new variable
df_subset = df.loc[:, ['Name', 'Age', 'Sex', 'Survived']]

# Print first 5 rows of subset (only 4 columns)
print(df_subset.head())

# Print shape of subset (891 rows, 4 columns)
print(df_subset.shape)

# ==========================================
# Bonus Task 11: rename()
# ==========================================

# Rename columns - Sex to Gender, Pclass to PassengerClass
df.rename(columns={'Sex': 'Gender', 'Pclass': 'PassengerClass'}, inplace=True)

# Print columns to confirm rename worked
print(df.columns)

# ==========================================
# Bonus Task 12: drop()
# ==========================================

# Drop Ticket and Cabin columns (not useful for analysis)
df.drop(columns=['Ticket', 'Cabin'], inplace=True)

# Print columns to confirm drop worked
print(df.columns)