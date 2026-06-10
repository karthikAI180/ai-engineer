import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# Set style
sns.set_style('whitegrid')
sns.set_palette('husl')

# ============================================================================
# CHART 1: SCATTER PLOT - Age vs Fare by Passenger Class
# ============================================================================
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Age', y='Fare', hue='Pclass', palette='husl')
plt.title('Age vs Fare by Passenger Class')
plt.xlabel('Age')
plt.ylabel('Fare ($)')
plt.tight_layout()
plt.savefig('1_scatter.png', dpi=300, bbox_inches='tight')


# ============================================================================
# CHART 2: BAR PLOT - Survival Rate by Passenger Class
# ============================================================================
plt.figure(figsize=(10, 6))
k = df.groupby('Pclass')['Survived'].mean().reset_index()
sns.barplot(data=k, x='Pclass', y='Survived', hue='Pclass', palette='husl')
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.tight_layout()
plt.savefig('2_bar.png', dpi=300, bbox_inches='tight')


# ============================================================================
# CHART 3: HISTOGRAM - Age Distribution by Survival
# ============================================================================
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Age', kde=True, hue='Survived', palette='husl')
plt.title('Age Distribution by Survival')
plt.xlabel('Age')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('3_histogram.png', dpi=300, bbox_inches='tight')


# ============================================================================
# CHART 4: BOX PLOT - Fare by Passenger Class and Survival
# ============================================================================
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Pclass', y='Fare', hue='Survived', palette='husl')
plt.title('Fare Distribution by Class and Survival')
plt.xlabel('Passenger Class')
plt.ylabel('Fare ($)')
plt.tight_layout()
plt.savefig('4_boxplot.png', dpi=300, bbox_inches='tight')


# ============================================================================
# CHART 5: HEATMAP - Correlation Matrix
# ============================================================================
plt.figure(figsize=(10, 8))
sns.heatmap(df[['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']].corr(),
            annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig('5_heatmap.png', dpi=300, bbox_inches='tight')


# ============================================================================
# CHART 6: VIOLIN PLOT - Age by Passenger Class and Survival
# ============================================================================
plt.figure(figsize=(10, 6))
sns.violinplot(data=df, x='Pclass', y='Age', hue='Survived', palette='husl')
plt.title('Age Distribution by Class and Survival')
plt.xlabel('Passenger Class')
plt.ylabel('Age')
plt.tight_layout()
plt.savefig('6_violin.png', dpi=300, bbox_inches='tight')


print("✅ All 6 charts created and saved!")
