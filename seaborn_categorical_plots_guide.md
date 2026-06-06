# Seaborn Categorical Plots - Complete Guide

---

## **What are Categorical Plots?**

**Categorical plots** show relationships between **categorical variables** (groups) and **numerical variables** (values).

Used for:
- Comparing values across groups
- Showing distributions within categories
- Identifying patterns by group

---

## **1. BARPLOT (Average Values per Category)**

### **What is it?**
A bar plot shows the **mean value** of a numerical variable for each category, with **confidence intervals** (error bars showing uncertainty).

### **When to use it?**
- Compare average values between groups
- Show uncertainty with error bars
- Simple group comparisons
- Highlight differences in means

### **Basic Syntax:**

```python
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

# Simple bar plot
sns.barplot(data=df, x='day', y='total_bill')
plt.show()
```

### **Parameters Explained:**

```python
sns.barplot(
    data=df,                   # DataFrame
    x='day',                   # X-axis category
    y='total_bill',           # Y-axis numerical value
    hue='sex',                # Color by second category
    order=['Thurs', 'Fri', 'Sat', 'Sun'],  # Custom order
    palette='Set2',           # Color scheme
    errbar='sd',              # Error bar type ('sd', 'se', 'pi', 'ci')
    ci=95,                    # Confidence interval (0-100)
    estimator=np.mean,        # Function to estimate (mean, median, sum, etc.)
    orient='v',               # 'v' vertical, 'h' horizontal
    ax=None                   # Matplotlib axes
)
```

### **Parameter Details:**

#### **`estimator` Parameter**
What value to show (not just mean):

```python
import numpy as np

# Show mean (default)
sns.barplot(data=df, x='day', y='total_bill', estimator=np.mean)

# Show median
sns.barplot(data=df, x='day', y='total_bill', estimator=np.median)

# Show sum
sns.barplot(data=df, x='day', y='total_bill', estimator=np.sum)

# Show count
sns.barplot(data=df, x='day', y='total_bill', estimator='count')
```

#### **`errbar` Parameter**
Type of error bars:

```python
# Standard deviation
sns.barplot(data=df, x='day', y='total_bill', errbar='sd')

# Standard error
sns.barplot(data=df, x='day', y='total_bill', errbar='se')

# 95% confidence interval (default)
sns.barplot(data=df, x='day', y='total_bill', errbar='ci')

# Percentile interval
sns.barplot(data=df, x='day', y='total_bill', errbar='pi')

# No error bars
sns.barplot(data=df, x='day', y='total_bill', errbar=None)
```

#### **`ci` Parameter**
Confidence interval percentage:

```python
# 95% confidence interval (default)
sns.barplot(data=df, x='day', y='total_bill', ci=95)

# 90% confidence interval
sns.barplot(data=df, x='day', y='total_bill', ci=90)

# No confidence interval
sns.barplot(data=df, x='day', y='total_bill', ci=None)
```

#### **`hue` Parameter**
Separate bars by second category:

```python
# Different colors for male/female
sns.barplot(data=df, x='day', y='total_bill', hue='sex')
plt.show()
```

#### **`order` Parameter**
Custom x-axis order:

```python
# Default: alphabetical
sns.barplot(data=df, x='day', y='total_bill')

# Custom order
custom_order = ['Thurs', 'Fri', 'Sat', 'Sun']
sns.barplot(data=df, x='day', y='total_bill', order=custom_order)
```

#### **`orient` Parameter**
Vertical or horizontal bars:

```python
# Vertical (default)
sns.barplot(data=df, x='day', y='total_bill', orient='v')

# Horizontal
sns.barplot(data=df, y='day', x='total_bill', orient='h')
```

### **Complete Examples:**

#### **Example 1: Simple Bar Plot**
```python
sns.barplot(data=df, x='day', y='total_bill', color='steelblue')
plt.title('Average Bill by Day')
plt.ylabel('Total Bill ($)')
plt.show()
```

#### **Example 2: Grouped Bar Plot**
```python
sns.barplot(data=df, x='day', y='total_bill', hue='sex', palette='Set2')
plt.title('Average Bill by Day and Gender')
plt.show()
```

#### **Example 3: Custom Order and Estimator**
```python
order = ['Fri', 'Sat', 'Sun', 'Thurs']
sns.barplot(data=df, x='day', y='total_bill', order=order, estimator=np.median, errbar='sd')
plt.title('Median Bill by Day (with SD)')
plt.show()
```

#### **Example 4: Horizontal Bar Plot**
```python
sns.barplot(data=df, y='day', x='total_bill', palette='husl')
plt.title('Average Bill by Day')
plt.show()
```

#### **Example 5: Without Error Bars**
```python
sns.barplot(data=df, x='day', y='total_bill', hue='sex', errbar=None)
plt.title('Average Bill by Day and Gender')
plt.show()
```

---

## **2. COUNTPLOT (Frequency Count)**

### **What is it?**
A count plot shows the **frequency** (count) of observations in each category. It's a histogram for categorical data.

### **When to use it?**
- Count occurrences in categories
- See sample size per group
- Compare frequencies
- Identify imbalanced categories

### **Basic Syntax:**

```python
# Count observations in each day
sns.countplot(data=df, x='day')
plt.show()
```

### **Parameters Explained:**

```python
sns.countplot(
    data=df,                   # DataFrame
    x='day',                   # Category column
    y=None,                    # Alternative to x
    hue='sex',                # Separate colors by category
    order=['Fri', 'Sat', 'Sun', 'Thurs'],  # Custom order
    hue_order=['Male', 'Female'],  # Custom hue order
    palette='Set2',           # Color scheme
    orient='v',               # 'v' vertical, 'h' horizontal
    ax=None                   # Matplotlib axes
)
```

### **Parameter Details:**

#### **`hue` Parameter**
Stacked or grouped counts:

```python
# Stacked by sex
sns.countplot(data=df, x='day', hue='sex')
plt.show()
```

#### **`order` Parameter**
Custom category order:

```python
order = ['Fri', 'Sat', 'Sun', 'Thurs']
sns.countplot(data=df, x='day', order=order)
plt.show()
```

#### **`orient` Parameter**
Horizontal or vertical:

```python
# Vertical (default)
sns.countplot(data=df, x='day')

# Horizontal
sns.countplot(data=df, y='day')
```

### **Complete Examples:**

#### **Example 1: Simple Count Plot**
```python
sns.countplot(data=df, x='day', color='steelblue')
plt.title('Number of Records per Day')
plt.ylabel('Count')
plt.show()
```

#### **Example 2: Count Plot with Hue**
```python
sns.countplot(data=df, x='day', hue='sex', palette='Set2')
plt.title('Count by Day and Gender')
plt.show()
```

#### **Example 3: Custom Order**
```python
order = ['Fri', 'Sat', 'Sun', 'Thurs']
sns.countplot(data=df, x='day', order=order, hue='sex')
plt.title('Count by Day and Gender (Custom Order)')
plt.show()
```

#### **Example 4: Horizontal Count Plot**
```python
sns.countplot(data=df, y='day', hue='sex')
plt.title('Count by Day (Horizontal)')
plt.show()
```

---

## **3. BOXPLOT (Distribution by Category)**

### **What is it?**
A box plot shows the **distribution** of a numerical variable for each category:
- Box = 25th to 75th percentile (middle 50%)
- Line inside box = median
- Whiskers = extend to outliers
- Points = individual outliers

### **When to use it?**
- See distribution shape per group
- Compare medians between groups
- Identify outliers
- Show spread/variability

### **Basic Syntax:**

```python
sns.boxplot(data=df, x='day', y='total_bill')
plt.show()
```

### **Understanding Box Plot:**

```
        Outlier (point)
           ↑
    ___    |    ___
   |   |   |   |   |
   | 75%--+---+---|--- Upper whisker
   |   |   |   |   |
   |---|---+---|----  Median (50th percentile)
   | 25%  |   |   |
   |___| ↓ |___|
        Outlier (point)
```

### **Parameters Explained:**

```python
sns.boxplot(
    data=df,                   # DataFrame
    x='day',                   # Category
    y='total_bill',           # Numerical value
    hue='sex',                # Color by category
    order=['Fri', 'Sat', 'Sun', 'Thurs'],  # Custom order
    palette='Set2',           # Color scheme
    width=0.6,                # Width of boxes
    linewidth=1.5,            # Border line width
    fliersize=8,              # Size of outlier points
    whis=1.5,                 # Whisker length (1.5 * IQR default)
    orient='v',               # 'v' or 'h'
    ax=None
)
```

### **Parameter Details:**

#### **`hue` Parameter**
Compare distributions by sub-group:

```python
# Box for each day, colored by sex
sns.boxplot(data=df, x='day', y='total_bill', hue='sex')
plt.show()
```

#### **`whis` Parameter**
Controls whisker length:

```python
# Default: 1.5 × IQR (inter-quartile range)
sns.boxplot(data=df, x='day', y='total_bill', whis=1.5)

# Show all points within 2 × IQR
sns.boxplot(data=df, x='day', y='total_bill', whis=2.0)

# Show min/max
sns.boxplot(data=df, x='day', y='total_bill', whis=[0, 100])
```

#### **`width` Parameter**
Box width:

```python
sns.boxplot(data=df, x='day', y='total_bill', width=0.3)   # Narrow
sns.boxplot(data=df, x='day', y='total_bill', width=0.8)   # Wide
```

### **Complete Examples:**

#### **Example 1: Simple Box Plot**
```python
sns.boxplot(data=df, x='day', y='total_bill', palette='Set2')
plt.title('Bill Distribution by Day')
plt.show()
```

#### **Example 2: Box Plot with Hue**
```python
sns.boxplot(data=df, x='day', y='total_bill', hue='sex', palette='husl')
plt.title('Bill Distribution by Day and Gender')
plt.show()
```

#### **Example 3: Horizontal Box Plot**
```python
sns.boxplot(data=df, y='day', x='total_bill', hue='sex')
plt.title('Bill Distribution (Horizontal)')
plt.show()
```

#### **Example 4: Custom Whisker Length**
```python
sns.boxplot(data=df, x='day', y='total_bill', whis=[10, 90])
plt.title('Box Plot with 10-90 Percentile Whiskers')
plt.show()
```

---

## **4. VIOLINPLOT (Distribution Shape)**

### **What is it?**
A violin plot shows the **full distribution** of a numerical variable per category using kernel density estimation.

**Like a box plot + KDE mirrored on both sides.**

### **When to use it?**
- See distribution shape per group
- Identify multimodal distributions
- More detail than box plot
- Beautiful visualization

### **Basic Syntax:**

```python
sns.violinplot(data=df, x='day', y='total_bill')
plt.show()
```

### **Understanding Violin Plot:**

```
    Distribution shape (KDE)
            ↓
        /‾‾‾‾‾\
       /       \
      |    ●    |    ● = median (with small box plot inside)
      |    |    |
       \       /
        \___/

    Width shows probability density
    (wider = more data points)
```

### **Parameters Explained:**

```python
sns.violinplot(
    data=df,                   # DataFrame
    x='day',                   # Category
    y='total_bill',           # Numerical value
    hue='sex',                # Color by category
    order=['Fri', 'Sat', 'Sun', 'Thurs'],  # Custom order
    palette='Set2',           # Color scheme
    inner='box',              # 'box', 'quartile', 'point', 'stick', None
    cut=0,                    # Extend density to min/max
    linewidth=1.5,            # Line width
    scale='width',            # 'width', 'area', 'count'
    bw=0.2,                   # Kernel bandwidth (smoothness)
    orient='v',               # 'v' or 'h'
    ax=None
)
```

### **Parameter Details:**

#### **`inner` Parameter**
What to show inside violin:

```python
# Box plot inside (default)
sns.violinplot(data=df, x='day', y='total_bill', inner='box')

# Quartile lines
sns.violinplot(data=df, x='day', y='total_bill', inner='quartile')

# Individual points
sns.violinplot(data=df, x='day', y='total_bill', inner='point')

# Lines at each point
sns.violinplot(data=df, x='day', y='total_bill', inner='stick')

# No inner detail
sns.violinplot(data=df, x='day', y='total_bill', inner=None)
```

#### **`scale` Parameter**
How to scale violin width:

```python
# Width = group size (default)
sns.violinplot(data=df, x='day', y='total_bill', scale='width')

# Width based on density area
sns.violinplot(data=df, x='day', y='total_bill', scale='area')

# Width = count
sns.violinplot(data=df, x='day', y='total_bill', scale='count')
```

#### **`hue` Parameter**
Split violin by category:

```python
sns.violinplot(data=df, x='day', y='total_bill', hue='sex', split=False)
# Each day has multiple violins (one per sex)

sns.violinplot(data=df, x='day', y='total_bill', hue='sex', split=True)
# One violin split in half (male left, female right)
```

### **Complete Examples:**

#### **Example 1: Simple Violin Plot**
```python
sns.violinplot(data=df, x='day', y='total_bill', palette='Set2')
plt.title('Bill Distribution by Day')
plt.show()
```

#### **Example 2: With Hue**
```python
sns.violinplot(data=df, x='day', y='total_bill', hue='sex', split=True)
plt.title('Bill Distribution by Day (Split by Gender)')
plt.show()
```

#### **Example 3: Different Inner Style**
```python
sns.violinplot(data=df, x='day', y='total_bill', inner='quartile')
plt.title('Violin Plot with Quartile Lines')
plt.show()
```

#### **Example 4: Horizontal Violin Plot**
```python
sns.violinplot(data=df, y='day', x='total_bill', palette='husl')
plt.title('Bill Distribution (Horizontal)')
plt.show()
```

---

## **5. STRIPPLOT (Individual Points)**

### **What is it?**
A strip plot shows **individual data points** scattered along the categorical axis.

**Like a scatter plot for categorical data.**

### **When to use it?**
- See all individual data points
- Show sample size
- Identify gaps and clusters
- Combine with other plots

### **Basic Syntax:**

```python
sns.stripplot(data=df, x='day', y='total_bill')
plt.show()
```

### **Parameters Explained:**

```python
sns.stripplot(
    data=df,                   # DataFrame
    x='day',                   # Category
    y='total_bill',           # Numerical value
    hue='sex',                # Color by category
    order=['Fri', 'Sat', 'Sun', 'Thurs'],  # Custom order
    palette='Set2',           # Color scheme
    size=6,                   # Point size
    jitter=True,              # Jitter points horizontally
    jitter_amount=0.1,        # Amount of jitter
    alpha=0.6,                # Transparency
    dodge=False,              # Dodge by hue
    orient='v',               # 'v' or 'h'
    ax=None
)
```

### **Parameter Details:**

#### **`jitter` Parameter**
Add random noise to prevent overlap:

```python
# No jitter (points overlap)
sns.stripplot(data=df, x='day', y='total_bill', jitter=False)

# With jitter (default, spread out)
sns.stripplot(data=df, x='day', y='total_bill', jitter=True)

# Control jitter amount
sns.stripplot(data=df, x='day', y='total_bill', jitter=0.2)
```

#### **`size` Parameter**
Point size:

```python
sns.stripplot(data=df, x='day', y='total_bill', size=4)   # Small
sns.stripplot(data=df, x='day', y='total_bill', size=12)  # Large
```

#### **`alpha` Parameter**
Transparency:

```python
sns.stripplot(data=df, x='day', y='total_bill', alpha=0.3)  # Transparent
sns.stripplot(data=df, x='day', y='total_bill', alpha=1.0)  # Opaque
```

#### **`dodge` Parameter**
Separate points by hue:

```python
# Overlapping points
sns.stripplot(data=df, x='day', y='total_bill', hue='sex', dodge=False)

# Separated by sex
sns.stripplot(data=df, x='day', y='total_bill', hue='sex', dodge=True)
```

### **Complete Examples:**

#### **Example 1: Simple Strip Plot**
```python
sns.stripplot(data=df, x='day', y='total_bill', jitter=True, size=6)
plt.title('Individual Bill Values by Day')
plt.show()
```

#### **Example 2: Colored by Category**
```python
sns.stripplot(data=df, x='day', y='total_bill', hue='sex', palette='Set2', jitter=True)
plt.title('Bills by Day (Colored by Gender)')
plt.show()
```

#### **Example 3: Dodged by Hue**
```python
sns.stripplot(data=df, x='day', y='total_bill', hue='sex', dodge=True, size=8)
plt.title('Bills by Day (Separated by Gender)')
plt.show()
```

#### **Example 4: Over Box Plot**
```python
# Box plot first
sns.boxplot(data=df, x='day', y='total_bill', color='lightgray')

# Strip plot on top
sns.stripplot(data=df, x='day', y='total_bill', color='red', jitter=True, size=5)
plt.title('Box Plot + Strip Plot')
plt.show()
```

---

## **6. SWARMPLOT (No Overlapping Points)**

### **What is it?**
A swarm plot shows **individual data points without overlapping**, using an algorithm to arrange them.

**Like a strip plot but points don't overlap.**

### **When to use it?**
- Small to medium datasets
- See every single point
- No overlapping needed
- Combine with other plots

### **Basic Syntax:**

```python
sns.swarmplot(data=df, x='day', y='total_bill')
plt.show()
```

### **Parameters Explained:**

```python
sns.swarmplot(
    data=df,                   # DataFrame
    x='day',                   # Category
    y='total_bill',           # Numerical value
    hue='sex',                # Color by category
    order=['Fri', 'Sat', 'Sun', 'Thurs'],  # Custom order
    palette='Set2',           # Color scheme
    size=6,                   # Point size
    dodge=False,              # Dodge by hue
    alpha=0.6,                # Transparency
    orient='v',               # 'v' or 'h'
    ax=None
)
```

### **Parameter Details:**

#### **`size` Parameter**
Point size:

```python
sns.swarmplot(data=df, x='day', y='total_bill', size=4)   # Small
sns.swarmplot(data=df, x='day', y='total_bill', size=10)  # Large
```

#### **`dodge` Parameter**
Separate points by hue:

```python
# All mixed together
sns.swarmplot(data=df, x='day', y='total_bill', hue='sex', dodge=False)

# Separated by sex
sns.swarmplot(data=df, x='day', y='total_bill', hue='sex', dodge=True)
```

#### **`alpha` Parameter**
Transparency:

```python
sns.swarmplot(data=df, x='day', y='total_bill', alpha=0.5)
```

### **Complete Examples:**

#### **Example 1: Simple Swarm Plot**
```python
sns.swarmplot(data=df, x='day', y='total_bill', size=6, color='steelblue')
plt.title('Individual Bills by Day (No Overlap)')
plt.show()
```

#### **Example 2: Colored by Category**
```python
sns.swarmplot(data=df, x='day', y='total_bill', hue='sex', palette='Set2')
plt.title('Bills by Day and Gender')
plt.show()
```

#### **Example 3: Over Violin Plot**
```python
# Violin plot first
sns.violinplot(data=df, x='day', y='total_bill', color='lightgray', inner=None)

# Swarm plot on top
sns.swarmplot(data=df, x='day', y='total_bill', color='black', size=5)
plt.title('Violin Plot + Swarm Plot')
plt.show()
```

#### **Example 4: Dodged by Hue**
```python
sns.swarmplot(data=df, x='day', y='total_bill', hue='sex', dodge=True, size=7)
plt.title('Bills by Day (Separated by Gender)')
plt.show()
```

---

## **COMPARISON TABLE: When to Use Each**

| Plot | Data | Best For | Pros | Cons |
|------|------|----------|------|------|
| **Bar** | Mean per group | Compare averages | Simple, shows CI | Hides distribution |
| **Count** | Frequency | See counts | Shows all groups clearly | Only for counts |
| **Box** | Distribution | Compare medians & spread | Shows quartiles & outliers | Less detail on shape |
| **Violin** | Distribution shape | See full distribution | Beautiful, smooth | Can mislead (smoothing) |
| **Strip** | Individual points | See all points | Shows sample size | Overlapping |
| **Swarm** | Individual points | See all points, no overlap | No overlapping | Slow for large data |

---

## **LAYERING PLOTS (Combine Multiple)**

### **Common Combinations:**

#### **Violin + Swarm**
```python
sns.violinplot(data=df, x='day', y='total_bill', inner=None, palette='Set2')
sns.swarmplot(data=df, x='day', y='total_bill', color='black', size=5)
plt.title('Distribution + Individual Points')
plt.show()
```

#### **Box + Strip**
```python
sns.boxplot(data=df, x='day', y='total_bill', palette='Set2')
sns.stripplot(data=df, x='day', y='total_bill', color='red', jitter=True, size=4)
plt.title('Distribution + Jittered Points')
plt.show()
```

#### **Violin + Box + Swarm**
```python
sns.violinplot(data=df, x='day', y='total_bill', inner=None, alpha=0.5)
sns.boxplot(data=df, x='day', y='total_bill', width=0.3, palette='Set2')
sns.swarmplot(data=df, x='day', y='total_bill', color='black', size=4)
plt.title('Complete Distribution View')
plt.show()
```

---

## **COMPLETE CATEGORICAL DASHBOARD**

```python
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
sns.set_theme(style='darkgrid', palette='Set2')

fig, axes = plt.subplots(2, 3, figsize=(16, 10))

# 1. Bar Plot
sns.barplot(data=df, x='day', y='total_bill', ax=axes[0, 0])
axes[0, 0].set_title('1. Bar Plot (Mean)')

# 2. Count Plot
sns.countplot(data=df, x='day', hue='sex', ax=axes[0, 1])
axes[0, 1].set_title('2. Count Plot (Frequency)')

# 3. Box Plot
sns.boxplot(data=df, x='day', y='total_bill', hue='sex', ax=axes[0, 2])
axes[0, 2].set_title('3. Box Plot (Distribution)')

# 4. Violin Plot
sns.violinplot(data=df, x='day', y='total_bill', ax=axes[1, 0])
axes[1, 0].set_title('4. Violin Plot (Shape)')

# 5. Strip Plot
sns.stripplot(data=df, x='day', y='total_bill', jitter=True, ax=axes[1, 1], size=6)
axes[1, 1].set_title('5. Strip Plot (Points)')

# 6. Violin + Swarm
sns.violinplot(data=df, x='day', y='total_bill', inner=None, ax=axes[1, 2])
sns.swarmplot(data=df, x='day', y='total_bill', color='black', size=4, ax=axes[1, 2])
axes[1, 2].set_title('6. Violin + Swarm')

plt.tight_layout()
plt.show()
```

---

## **FIGURE-LEVEL FUNCTIONS (Advanced)**

```python
# Automatically creates subplots and manages layout
sns.catplot(data=df, x='day', y='total_bill', kind='bar', height=5)

sns.catplot(data=df, x='day', y='total_bill', kind='box', hue='sex', height=5)

sns.catplot(data=df, x='day', y='total_bill', kind='violin', col='sex', height=5)

sns.catplot(data=df, x='day', y='total_bill', kind='strip', jitter=True, height=5)

# With faceting
sns.catplot(data=df, x='day', y='total_bill', hue='sex', col='time', height=5)
```

---

## **KEY TAKEAWAYS**

1. **Bar Plot:** Best for **comparing means**
2. **Count Plot:** Best for **showing frequencies**
3. **Box Plot:** Best for **quartiles + outliers**
4. **Violin Plot:** Best for **distribution shape**
5. **Strip Plot:** Best for **individual points** (small data)
6. **Swarm Plot:** Best for **individual points** (no overlap)

**Pro Tip:** Layer plots! Violin + Swarm is beautiful and informative! 🎨
