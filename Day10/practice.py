import pandas as pd

# ============================================
# TASK 1: Load & Inspect Titanic Dataset
# ============================================
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
print(df.head())
print(df.dtypes)
print(df.info())
print(df.isna().sum())


# ============================================
# TASK 2: Filtering
# ============================================

# Filter 1: Passengers over 30
filt = df['Age'] > 30
print(df[filt].head(2))
print(len(df[filt]))

# Filter 2: Female passengers
filt = df['Sex'] == 'female'
print(df[filt].head(3))
print(len(df[filt]))

# Filter 3: Survivors only
filt = df['Survived'] == 1
print(len(df[filt]))
print(df[filt].head(3))

# Filter 4: Combined conditions
filt1 = (df['Survived'] == 1) & (df['Sex'] == 'female')
filt2 = (df['Survived'] == 1) & (df['Sex'] == 'female') & (df['Age'] > 25)
print(len(df[filt1]))
print(len(df[filt2]))
print(df[filt1].head(3))
print(df[filt2].head(3))

# Filter 5: Names containing 'th'
filt1 = df['Name'].str.contains('th')
print(len(df[filt1]))
print(df[filt1].head(3))

# Filter 6: Combined conditions with AND and OR
filt2 = (df['Pclass'] == 3) & (df['Name'].str.contains('th'))
filt3 = (df['Pclass'] == 3) | (df['Name'].str.contains('th'))
print(len(df[filt2]))
print(df[filt2].head(3))
print(len(df[filt3]))
print(df[filt3].head(3))


# ============================================
# TASK 3: groupby() Part 1
# ============================================

# Survival rate by Sex
print(df.groupby(['Sex'])['Survived'].mean())

# Average age by Passenger Class
print(df.groupby(['Pclass'])['Age'].mean())

# Count passengers from each port
print(df.groupby(['Embarked']).size())

# Multiple stats by Sex using agg()
print(df.groupby(['Sex']).agg({
    'Survived': 'mean',
    'Age': 'mean',
    'Fare': 'sum'
}))

# Average fare by Passenger Class
print(df.groupby(['Pclass'])['Fare'].mean())

# Total survivors from each port
filt = df['Survived'] == 1
print(df[filt].groupby(['Embarked'])['Survived'].sum())


# ============================================
# TASK 4: groupby() Part 2 - Multi-level
# ============================================

# Survival rate by Class AND Sex
print(df.groupby(['Pclass', 'Sex'])['Survived'].mean())

# Count passengers by Sex AND Embarked port
print(df.groupby(['Embarked', 'Sex'])['PassengerId'].count())

# Average fare by Class AND Survival status
print(df.groupby(['Pclass', 'Survived'])['Fare'].mean())

# Average age by Embarked port AND Sex
print(df.groupby(['Embarked', 'Sex'])['Age'].mean())

# Total fare by Class AND Sex
print(df.groupby(['Pclass', 'Sex'])['Fare'].sum())


# ============================================
# TASK 5: Handle Null Values
# ============================================

# Sub-task 1: Drop all rows with any null
print(len(df))
print(len(df.dropna()))

# Sub-task 2: Drop only rows where Age is null
print(len(df.dropna(subset=['Age'])))

# Sub-task 3: Fill Age nulls with median and verify
df['Age'] = df['Age'].fillna(df['Age'].median())
print(df['Age'].isna().sum())

# Sub-task 4: Fill Embarked nulls with most common value
print(df['Embarked'].isna().sum())
value = df.groupby(['Embarked']).size().sort_values(ascending=False).head(1).index[0]
df['Embarked'] = df['Embarked'].fillna(value)
print(df['Embarked'].isna().sum())

# Sub-task 5: Fill Cabin nulls with most common value
value = df['Cabin'].mode()[0]
df['Cabin'] = df['Cabin'].fillna(value)
print(df['Cabin'].isna().sum())


# ============================================
# TASK 6: Merging
# ============================================

# Create summary table
summary = df.groupby(['Pclass'])['Fare'].mean().reset_index()
print(summary)

# Rename columns to avoid confusion
summary.columns = ['Pclass', 'Avg_Fare']

# Merge back to original dataframe
df_new = df.merge(summary, on='Pclass', how='inner')
print(df_new.head(3))


# ============================================
# TASK 7: apply() Function
# ============================================

# Sub-task 1: Create Age_Category column
def Age_Category(age):
    if pd.isnull(age):
        return 'Unknown'
    if age < 13:
        return 'Child'
    elif age >= 13 and age < 18:
        return 'Teen'
    elif age >= 18 and age < 65:
        return 'Adult'
    else:
        return 'Senior'

df['Age_Category'] = df['Age'].apply(Age_Category)
print(df.head(3))