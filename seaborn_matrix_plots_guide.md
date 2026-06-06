# Seaborn Matrix Plots - Complete Guide

---

## **What are Matrix Plots?**

**Matrix plots** are grid-based visualizations for:
- Displaying 2D data (heatmaps)
- Comparing multiple variables at once
- Creating multi-panel plots with shared properties
- Showing correlations and relationships

---

## **1. HEATMAP (2D Color Grid)**

### **What is it?**
A heatmap displays a **2D matrix** using **colors** to represent values. Rows and columns represent variables, colors show magnitude.

**Common uses:**
- Correlation matrices
- Time series heatmaps
- Comparing many variables

### **When to use it?**
- See correlations between variables
- Identify patterns in 2D data
- Compare values across multiple variables
- Show missing data

### **Basic Syntax:**

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset('tips')

# Simple heatmap
corr_matrix = df.corr(numeric_only=True)
sns.heatmap(corr_matrix)
plt.show()
```

### **Parameters Explained:**

```python
sns.heatmap(
    data=corr_matrix,              # 2D array/DataFrame
    vmin=None,                     # Minimum value color
    vmax=None,                     # Maximum value color
    cmap='viridis',                # Color palette
    center=None,                   # Center value (for diverging)
    annot=True,                    # Show values in cells
    fmt='.2f',                     # Number format
    linewidths=0.5,                # Line between cells
    linecolor='gray',              # Line color
    cbar=True,                     # Show colorbar
    cbar_kws={},                   # Colorbar settings
    square=False,                  # Make cells square
    xticklabels=True,              # Show x labels
    yticklabels=True,              # Show y labels
    ax=None                        # Matplotlib axes
)
```

### **Parameter Details:**

#### **`cmap` Parameter**
Color palette for values:

```python
# Viridis (purple to yellow)
sns.heatmap(corr_matrix, cmap='viridis')

# Coolwarm (blue to red)
sns.heatmap(corr_matrix, cmap='coolwarm')

# RdBu (red-blue diverging)
sns.heatmap(corr_matrix, cmap='RdBu_r', center=0)

# Sequential (white to dark)
sns.heatmap(corr_matrix, cmap='Blues')
```

#### **`annot` Parameter**
Show values in cells:

```python
# No annotations
sns.heatmap(corr_matrix, annot=False)

# Show values
sns.heatmap(corr_matrix, annot=True)

# Custom format
sns.heatmap(corr_matrix, annot=True, fmt='.2f')  # 2 decimals
```

#### **`center` Parameter**
Center diverging colormap:

```python
# Center at 0 (for diverging palettes like RdBu)
sns.heatmap(corr_matrix, cmap='RdBu', center=0)

# No center
sns.heatmap(corr_matrix, cmap='coolwarm')
```

#### **`vmin` and `vmax`**
Set color scale limits:

```python
# Default: auto min/max
sns.heatmap(corr_matrix, cmap='viridis')

# Custom range
sns.heatmap(corr_matrix, cmap='viridis', vmin=-1, vmax=1)
```

#### **`square` Parameter**
Make cells square (not rectangular):

```python
# Rectangular (default)
sns.heatmap(corr_matrix)

# Square
sns.heatmap(corr_matrix, square=True)
```

#### **`linewidths` Parameter**
Space between cells:

```python
sns.heatmap(corr_matrix, linewidths=0)      # No lines
sns.heatmap(corr_matrix, linewidths=1)      # 1px lines
sns.heatmap(corr_matrix, linewidths=2)      # 2px lines
```

#### **`cbar` Parameter**
Show/hide colorbar:

```python
# Show colorbar (default)
sns.heatmap(corr_matrix, cbar=True)

# Hide colorbar
sns.heatmap(corr_matrix, cbar=False)

# Customize colorbar
sns.heatmap(corr_matrix, cbar_kws={'label': 'Correlation'})
```

### **Complete Examples:**

#### **Example 1: Correlation Matrix**
```python
df = sns.load_dataset('tips')
corr = df.corr(numeric_only=True)

sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, square=True)
plt.title('Correlation Matrix')
plt.show()
```

#### **Example 2: Custom Range**
```python
sns.heatmap(corr, annot=True, cmap='RdBu_r', center=0, 
            vmin=-1, vmax=1, square=True, cbar_kws={'label': 'Correlation'})
plt.title('Correlation Heatmap')
plt.show()
```

#### **Example 3: No Annotations**
```python
sns.heatmap(corr, cmap='viridis', square=True, cbar=True)
plt.title('Correlation Heatmap (No Values)')
plt.show()
```

#### **Example 4: Custom Data (Not Correlation)**
```python
# Random 5x5 matrix
data = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    index=['A', 'B', 'C'],
    columns=['X', 'Y', 'Z']
)

sns.heatmap(data, annot=True, cmap='YlOrRd', linewidths=1, square=True)
plt.title('Custom Data Heatmap')
plt.show()
```

#### **Example 5: Large Dataset**
```python
# Create larger matrix
large_corr = pd.DataFrame(
    np.random.randn(10, 10),
    columns=[f'Var{i}' for i in range(10)],
    index=[f'Var{i}' for i in range(10)]
).corr()

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(large_corr, cmap='coolwarm', center=0, square=True, ax=ax)
plt.title('Large Correlation Matrix')
plt.show()
```

---

## **2. CLUSTERMAP (Hierarchical Clustering + Heatmap)**

### **What is it?**
A clustermap combines a **heatmap with hierarchical clustering**.

It reorders rows and columns using **dendrogram** (tree diagram) to group similar items together.

### **When to use it?**
- Find clusters in data
- Identify similar variables/samples
- Discover patterns through grouping
- Correlation with automatic ordering

### **Basic Syntax:**

```python
# Clustermap reorders based on similarity
g = sns.clustermap(corr_matrix)
plt.show()
```

### **Parameters Explained:**

```python
sns.clustermap(
    data=corr_matrix,              # 2D array/DataFrame
    cmap='viridis',                # Color palette
    center=None,                   # Center value
    annot=False,                   # Show values
    fmt='.2f',                     # Number format
    linewidths=0.5,                # Line between cells
    cbar_kws={},                   # Colorbar settings
    row_cluster=True,              # Cluster rows
    col_cluster=True,              # Cluster columns
    row_linkage=None,              # Custom row clustering
    col_linkage=None,              # Custom column clustering
    method='average',              # Linkage method
    metric='euclidean',            # Distance metric
    z_score=None,                  # Standardize rows/cols
    standard_scale=None,           # Scale rows/cols
    figsize=(10, 10),              # Figure size
    dendrogram_ratio=0.15          # Dendrogram size ratio
)
```

### **Parameter Details:**

#### **`row_cluster` and `col_cluster`**
Enable/disable clustering:

```python
# Cluster both (default)
sns.clustermap(corr_matrix, row_cluster=True, col_cluster=True)

# Only cluster rows
sns.clustermap(corr_matrix, row_cluster=True, col_cluster=False)

# No clustering (just heatmap)
sns.clustermap(corr_matrix, row_cluster=False, col_cluster=False)
```

#### **`method` Parameter**
Linkage method for clustering:

```python
# Average linkage (default)
sns.clustermap(corr_matrix, method='average')

# Single linkage (minimum distance)
sns.clustermap(corr_matrix, method='single')

# Complete linkage (maximum distance)
sns.clustermap(corr_matrix, method='complete')

# Ward linkage (minimize variance)
sns.clustermap(corr_matrix, method='ward')
```

#### **`metric` Parameter**
Distance metric:

```python
# Euclidean distance (default)
sns.clustermap(corr_matrix, metric='euclidean')

# Correlation distance
sns.clustermap(corr_matrix, metric='correlation')

# Manhattan distance
sns.clustermap(corr_matrix, metric='cityblock')
```

#### **`z_score` Parameter**
Standardize data before clustering:

```python
# No standardization (default)
sns.clustermap(corr_matrix)

# Standardize rows
sns.clustermap(corr_matrix, z_score=0)

# Standardize columns
sns.clustermap(corr_matrix, z_score=1)
```

### **Complete Examples:**

#### **Example 1: Simple Clustermap**
```python
g = sns.clustermap(corr, cmap='coolwarm', center=0)
plt.show()
```

#### **Example 2: With Annotations**
```python
g = sns.clustermap(corr, annot=True, cmap='RdBu_r', center=0, 
                   fmt='.2f', figsize=(10, 8))
plt.show()
```

#### **Example 3: No Row Clustering**
```python
g = sns.clustermap(corr, col_cluster=True, row_cluster=False)
plt.show()
```

#### **Example 4: Different Linkage Method**
```python
g = sns.clustermap(corr, method='ward', cmap='viridis', figsize=(10, 8))
plt.show()
```

#### **Example 5: With Z-Score Standardization**
```python
data = pd.DataFrame(np.random.randn(20, 10) + np.arange(10))
g = sns.clustermap(data, z_score=0, cmap='coolwarm', center=0)
plt.show()
```

---

## **3. PAIRGRID (Customizable Pair Plot)**

### **What is it?**
PairGrid creates a **grid of subplots** for every pair of variables. You manually specify what plot to use.

**Like pairplot but with full control.**

### **When to use it?**
- Customize pair plots beyond default
- Mix different plot types
- Add custom functions
- Fine-grained control

### **Basic Syntax:**

```python
# Create grid
g = sns.PairGrid(data=df)

# Map plots to grid
g.map_diag(sns.histplot)           # Diagonal: histogram
g.map_upper(sns.scatterplot)       # Upper triangle: scatter
g.map_lower(sns.kdeplot)           # Lower triangle: KDE

plt.show()
```

### **Parameters Explained:**

```python
sns.PairGrid(
    data=df,                       # DataFrame
    vars=['col1', 'col2'],        # Specific columns
    x_vars=['col1'],              # X-axis columns only
    y_vars=['col2'],              # Y-axis columns only
    hue='sex',                    # Color by category
    hue_order=['Male', 'Female'], # Hue order
    palette='Set2',               # Color palette
    diag_sharey=True,             # Share y-axis on diagonal
    height=2.5,                   # Subplot size
    aspect=1.0,                   # Aspect ratio
    corner=False                  # Show only lower triangle
)
```

### **Mapping Functions:**

```python
# Diagonal plots (single variable)
g.map_diag(sns.histplot)
g.map_diag(sns.kdeplot)

# Off-diagonal plots (two variables)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)
g.map_offdiag(sns.scatterplot)

# Add trendline
g.map_lower(sns.regplot)
```

### **Complete Examples:**

#### **Example 1: Histogram + Scatter**
```python
g = sns.PairGrid(df[['total_bill', 'tip', 'size']], height=2.5)
g.map_diag(sns.histplot)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)
plt.show()
```

#### **Example 2: With Hue**
```python
g = sns.PairGrid(df[['total_bill', 'tip', 'size', 'sex']], hue='sex', palette='Set2')
g.map_diag(sns.histplot)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)
plt.show()
```

#### **Example 3: With Regression**
```python
g = sns.PairGrid(df[['total_bill', 'tip', 'size']])
g.map_diag(sns.histplot)
g.map_upper(sns.scatterplot)
g.map_lower(sns.regplot)
plt.show()
```

#### **Example 4: Custom Plot Types**
```python
g = sns.PairGrid(df[['total_bill', 'tip', 'size']], diag_sharey=False)
g.map_diag(sns.kdeplot, fill=True)
g.map_upper(sns.scatterplot, alpha=0.5)
g.map_lower(sns.kdeplot, fill=True, cmap='Blues')
plt.show()
```

#### **Example 5: Corner Only (Lower Triangle)**
```python
g = sns.PairGrid(df[['total_bill', 'tip', 'size', 'sex']], 
                 hue='sex', corner=True)
g.map_diag(sns.histplot)
g.map_lower(sns.scatterplot)
plt.show()
```

---

## **4. FACETGRID (Multi-Panel Plots by Category)**

### **What is it?**
FacetGrid creates **separate subplots** for different groups/categories using `col` and `row` parameters.

**Great for conditional visualization (if-then style plots).**

### **When to use it?**
- Create plots for each group
- Compare same plot across categories
- Organize plots by multiple variables
- See patterns by subgroup

### **Basic Syntax:**

```python
# Create grid with separate plots per day
g = sns.FacetGrid(data=df, col='day')
g.map(sns.scatterplot, 'total_bill', 'tip')
plt.show()
```

### **Parameters Explained:**

```python
sns.FacetGrid(
    data=df,                       # DataFrame
    row='sex',                     # Rows by category
    col='day',                     # Columns by category
    hue='time',                    # Color by category
    col_order=['Fri', 'Sat', 'Sun', 'Thurs'],  # Custom order
    row_order=['Female', 'Male'],  # Custom order
    palette='Set2',                # Color palette
    height=5,                      # Subplot height
    aspect=1.0,                    # Aspect ratio
    margin_titles=False            # Show titles on margins
)
```

### **Mapping Functions:**

```python
# Single mapping
g.map(sns.scatterplot, 'total_bill', 'tip')

# Multiple mappings
g.map(sns.histplot, 'total_bill')

# With kwargs
g.map(sns.scatterplot, 'total_bill', 'tip', alpha=0.5, s=100)
```

### **Complete Examples:**

#### **Example 1: Column Faceting**
```python
g = sns.FacetGrid(df, col='day', height=4, aspect=1.2)
g.map(sns.scatterplot, 'total_bill', 'tip')
plt.show()
```

#### **Example 2: Row and Column Faceting**
```python
g = sns.FacetGrid(df, row='sex', col='day', height=4)
g.map(sns.scatterplot, 'total_bill', 'tip', alpha=0.6)
plt.show()
```

#### **Example 3: With Hue and Custom Order**
```python
g = sns.FacetGrid(df, col='day', hue='sex', palette='Set2', height=4)
g.map(sns.scatterplot, 'total_bill', 'tip', alpha=0.6, s=80)
g.add_legend()
plt.show()
```

#### **Example 4: Different Plot Type**
```python
g = sns.FacetGrid(df, col='day', height=4)
g.map(sns.histplot, 'total_bill', kde=True, bins=15)
plt.show()
```

#### **Example 5: Complex Faceting**
```python
g = sns.FacetGrid(df, row='time', col='day', height=3, aspect=1.2)
g.map(sns.scatterplot, 'total_bill', 'tip', hue='sex', palette='husl')
g.add_legend()
plt.show()
```

---

## **5. REGRESSION PLOTS (Linear Relationships)**

### **What is it?**
Regression plots show **linear relationships** with a **fitted line** and **confidence interval**.

### **When to use it?**
- Show trend lines
- Visualize linear relationships
- Compare correlation strength
- Show uncertainty in fit

### **Two Functions:**

#### **A. `regplot` (Axes-level)**

```python
# Simple scatter with regression line
sns.regplot(data=df, x='total_bill', y='tip')
plt.show()
```

**Parameters:**
```python
sns.regplot(
    data=df,
    x='total_bill',               # X variable
    y='tip',                      # Y variable
    scatter=True,                 # Show scatter points
    fit_reg=True,                 # Show regression line
    ci=95,                        # Confidence interval (0-100)
    order=1,                      # Polynomial order (1=linear, 2=quadratic)
    robust=False,                 # Robust regression (ignore outliers)
    logistic=False,               # Logistic regression
    ax=None
)
```

#### **B. `lmplot` (Figure-level)**

```python
# Creates own figure with faceting support
sns.lmplot(data=df, x='total_bill', y='tip', col='day')
plt.show()
```

**Parameters:**
```python
sns.lmplot(
    data=df,
    x='total_bill',               # X variable
    y='tip',                      # Y variable
    hue='sex',                    # Color by category
    col='day',                    # Facet by columns
    row='time',                   # Facet by rows
    fit_reg=True,                 # Show regression line
    ci=95,                        # Confidence interval
    order=1,                      # Polynomial order
    height=5,                     # Figure height
    aspect=1.0                    # Aspect ratio
)
```

### **Parameter Details:**

#### **`ci` Parameter**
Confidence interval:

```python
# 95% CI (default)
sns.regplot(data=df, x='total_bill', y='tip', ci=95)

# 99% CI (wider band)
sns.regplot(data=df, x='total_bill', y='tip', ci=99)

# No CI
sns.regplot(data=df, x='total_bill', y='tip', ci=None)
```

#### **`order` Parameter**
Polynomial order (degree of fit):

```python
# Linear fit (default)
sns.regplot(data=df, x='total_bill', y='tip', order=1)

# Quadratic fit (curved)
sns.regplot(data=df, x='total_bill', y='tip', order=2)

# Cubic fit
sns.regplot(data=df, x='total_bill', y='tip', order=3)
```

#### **`robust` Parameter**
Ignore outliers:

```python
# Standard regression (affected by outliers)
sns.regplot(data=df, x='total_bill', y='tip', robust=False)

# Robust regression (ignore outliers)
sns.regplot(data=df, x='total_bill', y='tip', robust=True)
```

#### **`scatter` Parameter**
Show/hide scatter points:

```python
# Show scatter points (default)
sns.regplot(data=df, x='total_bill', y='tip', scatter=True)

# Just the line
sns.regplot(data=df, x='total_bill', y='tip', scatter=False)
```

### **Complete Examples:**

#### **Example 1: Simple Regression**
```python
sns.regplot(data=df, x='total_bill', y='tip', scatter_kws={'alpha': 0.5})
plt.title('Bill vs Tip (Linear Regression)')
plt.show()
```

#### **Example 2: Quadratic Fit**
```python
sns.regplot(data=df, x='total_bill', y='tip', order=2, ci=90)
plt.title('Bill vs Tip (Quadratic Fit)')
plt.show()
```

#### **Example 3: Robust Regression**
```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Standard (affected by outliers)
sns.regplot(data=df, x='total_bill', y='tip', ax=axes[0])
axes[0].set_title('Standard Regression')

# Robust (ignores outliers)
sns.regplot(data=df, x='total_bill', y='tip', robust=True, ax=axes[1])
axes[1].set_title('Robust Regression')

plt.show()
```

#### **Example 4: LMPlot with Faceting**
```python
# Separate regression line per day
sns.lmplot(data=df, x='total_bill', y='tip', col='day', height=4)
plt.show()
```

#### **Example 5: Colored by Category**
```python
sns.lmplot(data=df, x='total_bill', y='tip', hue='sex', palette='Set2', height=6)
plt.show()
```

#### **Example 6: Row and Column Faceting**
```python
sns.lmplot(data=df, x='total_bill', y='tip', row='time', col='day', 
           hue='sex', height=4, aspect=1.2)
plt.show()
```

---

## **COMPARISON TABLE: When to Use Each Matrix Plot**

| Plot | Best For | Data Type | Output |
|------|----------|-----------|--------|
| **Heatmap** | Correlation matrices | 2D numerical | Single heatmap |
| **Clustermap** | Finding clusters | 2D numerical | Heatmap + dendrogram |
| **PairGrid** | Custom pair plots | Multiple variables | Grid of subplots |
| **FacetGrid** | Conditional plots | Categorical + numerical | Multi-panel plots |
| **Regplot** | Single regression | 2 numerical variables | Scatter + line |
| **LMPlot** | Multiple regressions | 2+ numerical | Faceted regressions |

---

## **COMPLETE MATRIX PLOTS DASHBOARD**

```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = sns.load_dataset('tips')
corr = df.corr(numeric_only=True)

# Set style
sns.set_theme(style='darkgrid', palette='Set2')

# 1. Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, square=True)
plt.title('1. Heatmap (Correlation)')
plt.tight_layout()
plt.show()

# 2. Clustermap
g = sns.clustermap(corr, cmap='coolwarm', center=0, figsize=(8, 6))
g.fig.suptitle('2. Clustermap (With Clustering)', y=1.02)
plt.show()

# 3. PairGrid
g = sns.PairGrid(df[['total_bill', 'tip', 'size']], height=2.5)
g.map_diag(sns.histplot)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)
plt.suptitle('3. PairGrid (Custom Pair Plot)', y=1.00)
plt.show()

# 4. FacetGrid
g = sns.FacetGrid(df, col='day', height=3, aspect=1.2)
g.map(sns.scatterplot, 'total_bill', 'tip', alpha=0.6)
g.fig.suptitle('4. FacetGrid (By Category)', y=0.98)
plt.show()

# 5. Regplot
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
sns.regplot(data=df, x='total_bill', y='tip', scatter_kws={'alpha': 0.5})
plt.title('5a. Regplot (Linear)')

plt.subplot(1, 2, 2)
sns.regplot(data=df, x='total_bill', y='tip', order=2, scatter_kws={'alpha': 0.5})
plt.title('5b. Regplot (Quadratic)')
plt.tight_layout()
plt.show()

# 6. LMPlot with Faceting
sns.lmplot(data=df, x='total_bill', y='tip', col='day', height=4)
plt.suptitle('6. LMPlot (Regression Grid)', y=1.00)
plt.show()
```

---

## **ADVANCED COMBINATIONS**

### **Heatmap + Clustermap Side by Side**
```python
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Regular heatmap
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, ax=axes[0])
axes[0].set_title('Original Order')

# Note: Clustermap creates own figure, so this is conceptual
```

### **FacetGrid + PairGrid Combination**
```python
# Separate pair plots for each category
for group in df['day'].unique():
    g = sns.PairGrid(df[df['day'] == group][['total_bill', 'tip', 'size']], height=2)
    g.map_diag(sns.histplot)
    g.map_upper(sns.scatterplot)
    g.map_lower(sns.kdeplot)
    plt.suptitle(f'PairGrid for {group}')
    plt.show()
```

### **FacetGrid + Regression**
```python
g = sns.FacetGrid(df, col='day', hue='sex', palette='Set2', height=4)
g.map(sns.regplot, 'total_bill', 'tip')
g.add_legend()
plt.show()
```

---

## **KEY TAKEAWAYS**

1. **Heatmap:** Best for **correlation matrices**
2. **Clustermap:** Best for **finding clusters** in data
3. **PairGrid:** Best for **customizable pair plots**
4. **FacetGrid:** Best for **conditional/faceted plots**
5. **Regplot:** Best for **single regression** relationship
6. **LMPlot:** Best for **multiple regressions** with faceting

**Pro Tip:** Combine FacetGrid + Heatmap for multi-group correlations! 🎨

---

## **QUICK REFERENCE: Function Selection**

```
Want to show CORRELATIONS?        → Heatmap
Want to CLUSTER similar items?    → Clustermap
Want CUSTOM pair plot?            → PairGrid
Want SEPARATE plots by group?     → FacetGrid
Want SINGLE trend line?           → Regplot
Want MULTIPLE trend lines?        → LMPlot
```
