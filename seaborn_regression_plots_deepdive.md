# Seaborn Regression Plots - Deep Dive & Complete Guide

---

## **What are Regression Plots?**

**Regression plots** visualize **linear and non-linear relationships** between two variables by fitting a model and showing:
- **Scatter points** (actual data)
- **Fitted line** (trend)
- **Confidence interval** (uncertainty band)

---

## **1. REGPLOT (Axes-Level Regression)**

### **What is it?**
`regplot` creates a **scatter plot with a regression line** and confidence band on a matplotlib axes.

Used for **single plot focused on one relationship**.

### **When to use it?**
- Examine relationship between 2 variables
- Fit and visualize trends
- Customize single plot
- Manual subplot control

### **Basic Syntax:**

```python
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

# Simple scatter + regression line
sns.regplot(data=df, x='total_bill', y='tip')
plt.show()
```

### **Parameters Explained:**

```python
sns.regplot(
    data=df,                       # DataFrame
    x='total_bill',               # X variable
    y='tip',                      # Y variable
    scatter=True,                 # Show scatter points
    fit_reg=True,                 # Show regression line
    ci=95,                        # Confidence interval (0-100)
    order=1,                      # Polynomial order (1=linear, 2=quadratic)
    robust=False,                 # Robust regression (ignore outliers)
    logistic=False,               # Logistic regression (binary outcomes)
    lowess=False,                 # LOWESS smooth fit
    x_estimator=None,             # Function to estimate y for each x value
    x_ci=95,                      # CI for x_estimator
    scatter_kws={},               # Scatter point arguments
    line_kws={},                  # Line arguments
    ax=None                       # Matplotlib axes
)
```

### **Parameter Details:**

#### **`fit_reg` Parameter**
Show or hide regression line:

```python
# With regression line (default)
sns.regplot(data=df, x='total_bill', y='tip', fit_reg=True)

# Just scatter points
sns.regplot(data=df, x='total_bill', y='tip', fit_reg=False)
```

#### **`ci` Parameter**
Confidence interval (uncertainty band):

```python
# 95% confidence interval (default) - wider band
sns.regplot(data=df, x='total_bill', y='tip', ci=95)

# 99% confidence interval - even wider
sns.regplot(data=df, x='total_bill', y='tip', ci=99)

# 68% confidence interval - narrower
sns.regplot(data=df, x='total_bill', y='tip', ci=68)

# No confidence interval
sns.regplot(data=df, x='total_bill', y='tip', ci=None)
```

**What the band shows:**
- Band gets **wider** at the edges (more uncertainty)
- Band gets **narrower** in the middle (more certainty)
- Wider CI = less certainty, Narrower CI = more certainty

#### **`order` Parameter**
Polynomial order (degree of fit):

```python
# Linear (straight line) - order=1 (default)
sns.regplot(data=df, x='total_bill', y='tip', order=1)
# y = a + b*x

# Quadratic (curved) - order=2
sns.regplot(data=df, x='total_bill', y='tip', order=2)
# y = a + b*x + c*x²

# Cubic - order=3
sns.regplot(data=df, x='total_bill', y='tip', order=3)
# y = a + b*x + c*x² + d*x³

# Higher orders = more complex curves
sns.regplot(data=df, x='total_bill', y='tip', order=5)
```

**Visual Difference:**
```
order=1 (Linear)      order=2 (Quadratic)    order=3 (Cubic)
    /                  /‾‾\                  /‾\  
   /                  /     \                /   \
  /                  /       \              /     \
```

#### **`robust` Parameter**
Robust regression (ignore outliers):

```python
# Standard regression (affected by outliers)
sns.regplot(data=df, x='total_bill', y='tip', robust=False)

# Robust regression (uses median, ignores extreme outliers)
sns.regplot(data=df, x='total_bill', y='tip', robust=True)
```

**When to use:**
- `robust=False`: Normal data without extreme outliers
- `robust=True`: Data with outliers that distort the line

#### **`logistic` Parameter**
Logistic regression (for binary outcome):

```python
# Create binary variable
df['high_tip'] = (df['tip'] > df['tip'].median()).astype(int)

# Standard linear regression
sns.regplot(data=df, x='total_bill', y='high_tip', logistic=False)

# Logistic regression (S-curve)
sns.regplot(data=df, x='total_bill', y='high_tip', logistic=True)
```

**Output:** S-shaped curve showing probability (0 to 1)

#### **`lowess` Parameter**
LOWESS smooth fit (non-parametric):

```python
# Linear fit
sns.regplot(data=df, x='total_bill', y='tip', lowess=False)

# LOWESS fit (smooth, follows data more closely)
sns.regplot(data=df, x='total_bill', y='tip', lowess=True)
```

**LOWESS (Locally Weighted Scatterplot Smoothing):**
- No straight line assumption
- Follows data patterns more closely
- Great for exploring data without assumptions

#### **`scatter_kws` Parameter**
Customize scatter points:

```python
sns.regplot(
    data=df, x='total_bill', y='tip',
    scatter_kws={
        'alpha': 0.5,              # Transparency
        's': 100,                  # Size
        'color': 'red',            # Color
        'edgecolor': 'black',      # Border color
        'linewidth': 1             # Border width
    }
)
plt.show()
```

#### **`line_kws` Parameter**
Customize regression line:

```python
sns.regplot(
    data=df, x='total_bill', y='tip',
    line_kws={
        'color': 'red',            # Line color
        'linewidth': 3,            # Line thickness
        'linestyle': '--',         # Dashed line
        'alpha': 0.8               # Transparency
    }
)
plt.show()
```

### **Complete Examples:**

#### **Example 1: Basic Regression**
```python
sns.regplot(data=df, x='total_bill', y='tip')
plt.title('Relationship: Bill vs Tip')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.show()
```

#### **Example 2: Without Confidence Interval**
```python
sns.regplot(data=df, x='total_bill', y='tip', ci=None)
plt.title('Bill vs Tip (No CI)')
plt.show()
```

#### **Example 3: Polynomial Fit (Quadratic)**
```python
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Linear
sns.regplot(data=df, x='total_bill', y='tip', order=1, ax=axes[0])
axes[0].set_title('Linear (order=1)')

# Quadratic
sns.regplot(data=df, x='total_bill', y='tip', order=2, ax=axes[1])
axes[1].set_title('Quadratic (order=2)')

# Cubic
sns.regplot(data=df, x='total_bill', y='tip', order=3, ax=axes[2])
axes[2].set_title('Cubic (order=3)')

plt.tight_layout()
plt.show()
```

#### **Example 4: Robust Regression**
```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Standard (affected by outliers)
sns.regplot(data=df, x='total_bill', y='tip', robust=False, ax=axes[0])
axes[0].set_title('Standard Regression')

# Robust (ignores outliers)
sns.regplot(data=df, x='total_bill', y='tip', robust=True, ax=axes[1])
axes[1].set_title('Robust Regression')

plt.show()
```

#### **Example 5: LOWESS Smooth Fit**
```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Linear
sns.regplot(data=df, x='total_bill', y='tip', lowess=False, ax=axes[0])
axes[0].set_title('Linear Fit')

# LOWESS (smooth, non-parametric)
sns.regplot(data=df, x='total_bill', y='tip', lowess=True, ax=axes[1])
axes[1].set_title('LOWESS Smooth Fit')

plt.show()
```

#### **Example 6: Logistic Regression**
```python
# Create binary outcome
df['high_tip'] = (df['tip'] > 3).astype(int)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Linear (not appropriate for binary)
sns.regplot(data=df, x='total_bill', y='high_tip', ax=axes[0])
axes[0].set_title('Linear (Inappropriate)')

# Logistic (S-curve for probability)
sns.regplot(data=df, x='total_bill', y='high_tip', logistic=True, ax=axes[1])
axes[1].set_title('Logistic (Appropriate)')

plt.show()
```

#### **Example 7: Custom Styling**
```python
sns.regplot(
    data=df, x='total_bill', y='tip',
    scatter_kws={'alpha': 0.5, 's': 80, 'color': 'blue'},
    line_kws={'color': 'red', 'linewidth': 2}
)
plt.title('Customized Regression Plot')
plt.show()
```

---

## **2. LMPLOT (Figure-Level Regression)**

### **What is it?**
`lmplot` is the **figure-level version** of `regplot`. It creates its own figure and supports **faceting** (subplots).

Used for **multiple plots with automatic layout**.

### **When to use it?**
- Create multiple regression plots
- Facet by categories (col/row)
- Color by hue
- Don't need subplot control

### **Basic Syntax:**

```python
# Single plot (like regplot)
sns.lmplot(data=df, x='total_bill', y='tip')
plt.show()

# Multiple plots by category
sns.lmplot(data=df, x='total_bill', y='tip', col='day')
plt.show()
```

### **Parameters Explained:**

```python
sns.lmplot(
    data=df,                       # DataFrame
    x='total_bill',               # X variable
    y='tip',                      # Y variable
    hue='sex',                    # Color by category
    col='day',                    # Columns by category
    row='time',                   # Rows by category
    col_order=['Fri', 'Sat', 'Sun', 'Thurs'],  # Custom order
    row_order=['Lunch', 'Dinner'], # Custom order
    palette='Set2',               # Color palette
    fit_reg=True,                 # Show regression line
    ci=95,                        # Confidence interval
    order=1,                      # Polynomial order
    robust=False,                 # Robust regression
    logistic=False,               # Logistic regression
    lowess=False,                 # LOWESS smooth
    height=5,                     # Subplot height
    aspect=1.0,                   # Aspect ratio
    scatter_kws={},               # Scatter arguments
    line_kws={},                  # Line arguments
    hue_order=['Male', 'Female'], # Hue order
    legend=True                   # Show legend
)
```

### **Parameter Details:**

#### **`col` Parameter**
Separate plots by column:

```python
# One row, 4 columns (one for each day)
sns.lmplot(data=df, x='total_bill', y='tip', col='day')
plt.show()
```

#### **`row` Parameter**
Separate plots by row:

```python
# 2 rows (lunch/dinner), 1 column
sns.lmplot(data=df, x='total_bill', y='tip', row='time')
plt.show()
```

#### **`col` + `row`**
Matrix of plots:

```python
# 2x4 grid: rows=time, cols=day
sns.lmplot(data=df, x='total_bill', y='tip', row='time', col='day')
plt.show()
```

#### **`hue` Parameter**
Color by category (within same plot):

```python
# Lines for male/female, columns for day
sns.lmplot(data=df, x='total_bill', y='tip', col='day', hue='sex', palette='Set2')
plt.show()
```

#### **`height` and `aspect`**
Figure size:

```python
# Tall plots
sns.lmplot(data=df, x='total_bill', y='tip', col='day', height=6)

# Wide plots
sns.lmplot(data=df, x='total_bill', y='tip', col='day', height=5, aspect=2)
```

### **Complete Examples:**

#### **Example 1: Simple LMPlot**
```python
sns.lmplot(data=df, x='total_bill', y='tip', height=5)
plt.show()
```

#### **Example 2: Facet by Column**
```python
sns.lmplot(data=df, x='total_bill', y='tip', col='day', height=4)
plt.show()
```

#### **Example 3: Facet by Row**
```python
sns.lmplot(data=df, x='total_bill', y='tip', row='time', height=4)
plt.show()
```

#### **Example 4: Matrix Faceting**
```python
# 2x4 grid
sns.lmplot(data=df, x='total_bill', y='tip', row='time', col='day', height=3, aspect=1.2)
plt.show()
```

#### **Example 5: With Hue**
```python
# Separate lines for male/female within each day
sns.lmplot(data=df, x='total_bill', y='tip', col='day', hue='sex', 
           palette='Set2', height=4)
plt.show()
```

#### **Example 6: Polynomial + Hue + Facet**
```python
sns.lmplot(data=df, x='total_bill', y='tip', col='day', hue='sex', 
           order=2, palette='husl', height=4)
plt.show()
```

#### **Example 7: Robust + Hue + Facet**
```python
sns.lmplot(data=df, x='total_bill', y='tip', col='day', hue='sex', 
           robust=True, palette='Set2', height=4)
plt.show()
```

#### **Example 8: Large Faceted Grid**
```python
sns.lmplot(data=df, x='total_bill', y='tip', row='time', col='day', 
           hue='sex', palette='husl', height=3, aspect=1.3)
plt.show()
```

---

## **3. RESIDPLOT (Regression Diagnostics)**

### **What is it?**
A residual plot shows **differences between actual and predicted values** (residuals).

Used for **checking if linear regression is appropriate**.

### **When to use it?**
- Check regression assumptions
- Detect non-linear patterns
- Identify outliers
- Verify homoscedasticity (equal variance)

### **Basic Syntax:**

```python
# Residuals vs fitted values
sns.residplot(data=df, x='total_bill', y='tip')
plt.show()
```

### **How to Interpret:**

**Good residuals (linear regression is appropriate):**
- Points scattered randomly around y=0
- No clear pattern
- Equal spread across x-axis

**Bad residuals (linear regression NOT appropriate):**
- U-shape or other pattern
- Residuals increase/decrease systematically
- Unequal spread (wider at one end)

### **Parameters Explained:**

```python
sns.residplot(
    data=df,
    x='total_bill',               # X variable (or residual array)
    y='tip',                      # Y variable
    lowess=True,                  # Add LOWESS smoothed line
    robust=False,                 # Robust regression
    scatter_kws={},               # Scatter arguments
    line_kws={'color': 'red'},    # Line arguments
    ax=None
)
```

### **Complete Examples:**

#### **Example 1: Simple Residual Plot**
```python
sns.residplot(data=df, x='total_bill', y='tip', lowess=True)
plt.title('Residual Plot: Bill vs Tip')
plt.ylabel('Residuals')
plt.axhline(y=0, color='r', linestyle='--', alpha=0.5)
plt.show()
```

#### **Example 2: Linear vs Quadratic**
```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Fit linear, plot residuals
from sklearn.linear_model import LinearRegression
model_linear = LinearRegression()
model_linear.fit(df[['total_bill']], df['tip'])
residuals_linear = df['tip'] - model_linear.predict(df[['total_bill']])

axes[0].scatter(df['total_bill'], residuals_linear, alpha=0.5)
axes[0].axhline(y=0, color='r', linestyle='--')
axes[0].set_title('Residuals (Linear Model)')
axes[0].set_ylabel('Residuals')

# Fit quadratic, plot residuals
from sklearn.preprocessing import PolynomialFeatures
poly_features = PolynomialFeatures(degree=2)
X_poly = poly_features.fit_transform(df[['total_bill']])
model_quad = LinearRegression()
model_quad.fit(X_poly, df['tip'])
residuals_quad = df['tip'] - model_quad.predict(X_poly)

axes[1].scatter(df['total_bill'], residuals_quad, alpha=0.5)
axes[1].axhline(y=0, color='r', linestyle='--')
axes[1].set_title('Residuals (Quadratic Model)')
axes[1].set_ylabel('Residuals')

plt.tight_layout()
plt.show()
```

---

## **4. STATISTICAL INTERPRETATION**

### **R² Score (Coefficient of Determination)**

Shows how well the model fits the data:
- **R² = 1.0:** Perfect fit (100% variance explained)
- **R² = 0.5:** Moderate fit (50% variance explained)
- **R² = 0.0:** No fit (model useless)

### **Confidence Interval Band**

- **Narrow band:** High confidence in prediction
- **Wide band:** Low confidence
- Band gets **wider** at extremes (fewer data points)

### **Robust vs Standard Regression**

**Standard Regression:**
- Minimizes sum of squared errors
- Outliers have large impact
- Use when data is "clean"

**Robust Regression:**
- Uses median instead of mean
- Outliers have less impact
- Use when data has extreme values

### **Linear vs Polynomial vs LOWESS**

**Linear (order=1):**
- Simple, interpretable
- Good for stable trends
- Fails if relationship is curved

**Polynomial (order=2, 3, ...):**
- Captures curved relationships
- Higher order = more complex
- Risk of overfitting

**LOWESS:**
- Non-parametric (no equation)
- Follows data closely
- Best for exploration without assumptions

### **Logistic Regression**

For **binary outcomes** (0/1, yes/no):
- Output = probability (0 to 1)
- S-shaped curve
- Used in classification

---

## **5. COMPLETE REGRESSION ANALYSIS WORKFLOW**

```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

df = sns.load_dataset('tips')

# 1. Explore relationship
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Simple scatter
axes[0, 0].scatter(df['total_bill'], df['tip'], alpha=0.5)
axes[0, 0].set_title('1. Scatter Plot')

# Linear regression
sns.regplot(data=df, x='total_bill', y='tip', ax=axes[0, 1])
axes[0, 1].set_title('2. Linear Regression')

# Polynomial regression
sns.regplot(data=df, x='total_bill', y='tip', order=2, ax=axes[1, 0])
axes[1, 0].set_title('3. Quadratic Regression')

# Residuals
sns.residplot(data=df, x='total_bill', y='tip', ax=axes[1, 1], lowess=True)
axes[1, 1].set_title('4. Residual Plot')
axes[1, 1].axhline(y=0, color='r', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()

# 2. Calculate correlation
correlation = df['total_bill'].corr(df['tip'])
print(f"Correlation: {correlation:.3f}")

# 3. Fit model and get R²
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(df[['total_bill']], df['tip'])
r2 = model.score(df[['total_bill']], df['tip'])
print(f"R² Score: {r2:.3f}")

# 4. Get regression equation
slope = model.coef_[0]
intercept = model.intercept_
print(f"Equation: tip = {intercept:.2f} + {slope:.3f} * bill")
```

---

## **6. REAL-WORLD EXAMPLES**

### **Example 1: Sales vs Advertising**
```python
# Sample data
data = pd.DataFrame({
    'advertising': np.random.uniform(0, 100, 100),
    'sales': np.random.uniform(0, 500, 100)
})

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Regplot
sns.regplot(data=data, x='advertising', y='sales', ax=axes[0])
axes[0].set_title('Advertising vs Sales')

# Robust (if outliers suspected)
sns.regplot(data=data, x='advertising', y='sales', robust=True, ax=axes[1])
axes[1].set_title('Robust Regression')

plt.show()
```

### **Example 2: Temperature vs Ice Cream Sales**
```python
# Non-linear relationship likely
data = pd.DataFrame({
    'temperature': np.linspace(0, 40, 50),
    'ice_cream_sales': np.linspace(0, 40, 50) ** 1.5 + np.random.normal(0, 10, 50)
})

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Linear (poor fit)
sns.regplot(data=data, x='temperature', y='ice_cream_sales', order=1, ax=axes[0])
axes[0].set_title('Linear (order=1)')

# Quadratic (better)
sns.regplot(data=data, x='temperature', y='ice_cream_sales', order=2, ax=axes[1])
axes[1].set_title('Quadratic (order=2)')

# LOWESS (exploratory)
sns.regplot(data=data, x='temperature', y='ice_cream_sales', lowess=True, ax=axes[2])
axes[2].set_title('LOWESS Smooth')

plt.tight_layout()
plt.show()
```

### **Example 3: Student Hours vs Exam Score**
```python
data = pd.DataFrame({
    'study_hours': np.random.uniform(0, 10, 100),
    'exam_score': np.random.uniform(30, 100, 100)
})

sns.lmplot(data=data, x='study_hours', y='exam_score', height=6)
plt.title('Study Hours vs Exam Score')
plt.show()
```

### **Example 4: Probability by Group**
```python
# Binary outcome
df['high_tip'] = (df['tip'] > df['tip'].median()).astype(int)

sns.lmplot(data=df, x='total_bill', y='high_tip', col='sex', 
           logistic=True, height=5)
plt.show()
```

---

## **KEY TAKEAWAYS**

1. **Regplot:** Single scatter + line plot
2. **LMPlot:** Multiple plots with faceting
3. **ResidPlot:** Check regression assumptions
4. **order=1:** Linear (straight line)
5. **order>1:** Polynomial (curved)
6. **robust=True:** Ignore outliers
7. **logistic=True:** Probability curves
8. **lowess=True:** Smooth exploration

---

## **DECISION TREE**

```
Want to VISUALIZE relationship?
├─ Single plot? → regplot()
├─ Multiple plots? → lmplot() + col/row
└─ Check assumptions? → residplot()

Want LINEAR fit?
└─ order=1 (default)

Want CURVED fit?
├─ Slightly curved? → order=2
├─ Very curved? → order=3+
└─ Unknown pattern? → lowess=True

Have OUTLIERS?
└─ robust=True

Have BINARY outcome?
└─ logistic=True
```

---

## **CHEAT SHEET**

```python
# Simple linear
sns.regplot(data=df, x='x', y='y')

# Quadratic
sns.regplot(data=df, x='x', y='y', order=2)

# Robust (outliers)
sns.regplot(data=df, x='x', y='y', robust=True)

# No CI
sns.regplot(data=df, x='x', y='y', ci=None)

# Multiple by category
sns.lmplot(data=df, x='x', y='y', col='category')

# By rows and columns
sns.lmplot(data=df, x='x', y='y', row='row_cat', col='col_cat')

# With hue (colors)
sns.lmplot(data=df, x='x', y='y', col='col_cat', hue='hue_cat')

# Check fit quality
sns.residplot(data=df, x='x', y='y', lowess=True)

# Binary outcome
sns.regplot(data=df, x='x', y='binary', logistic=True)
```
