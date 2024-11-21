
## Introduction to Handling Missing Values

Welcome back, everyone! In this video, we'll dive into **handling missing values**—a crucial part of feature engineering in any data science, machine learning, or deep learning project.

### Why is Handling Missing Values Important?

Whenever you're solving real-world data science problems, you'll often encounter messy, raw data that isn't ready for modeling. Missing values are one of the most common issues you'll face. Whether you're working on a data science project or deploying a machine learning model, dealing with missing values is an essential step.

Let’s explore why missing values occur, the types of missing data, and different techniques to handle them.

---

### Why Do Missing Values Occur?

Imagine you’ve distributed a survey form to a sample of people. If someone isn't comfortable answering certain questions, they might leave those fields empty. As a result, the dataset will have missing values. This is just one scenario, but in general, missing values occur when information for a specific variable is not captured.

### Mechanisms of Missing Data

There are three main mechanisms through which missing data can occur:

1. **Missing Completely at Random (MCAR)**:
   - The missing values are completely random and have no relationship with any other data.
   - Example: A survey participant accidentally skips a question due to a form error or data entry mistake.
   - In this case, missing values are randomly distributed, and there’s no systematic reason for their absence.

2. **Missing at Random (MAR)**:
   - The probability of a value being missing is related to the observed data but not the missing data itself.
   - Example: In a survey, men may be less likely to disclose their income, while women may be reluctant to disclose their age. Here, the missingness is dependent on another variable (like gender).
   - So, the missing data in one column may depend on data in another column.

3. **Missing Not at Random (MNAR)**:
   - The missing data is not random and depends on the value of the missing data itself or other unmeasured factors.
   - Example: Employees dissatisfied with their job may choose not to disclose their income. Thus, missingness is tied to their job satisfaction level.
   - Here, missing values are related to hidden factors that may not be directly measured in the dataset.

---

### Handling Missing Values: Techniques and Examples

Now that we understand why missing values occur, let's explore techniques to handle them. We’ll use Python to demonstrate these techniques with the popular **Titanic dataset**, which contains a lot of missing values.

Let’s start by loading the dataset and exploring the missing values.

```python
import seaborn as sns
import pandas as pd

# Load Titanic dataset
df = sns.load_dataset('titanic')

# Display the first few rows
print(df.head())

# Checking for missing values
print("\nMissing Values Count per Column:")
print(df.isnull().sum())
```

**Explanation**:  
Here, we use the Titanic dataset from Seaborn, which contains missing values in columns like `age`, `embarked`, and `deck`.

### Approach 1: Dropping Missing Values

#### **1. Dropping Rows with Missing Values**

```python
# Dropping rows with any missing values
df_dropped_rows = df.dropna()
print("\nShape after dropping rows with missing values:", df_dropped_rows.shape)
```

**Problem**:  
This method significantly reduces the size of your dataset. For example, in the Titanic dataset, we have 891 rows initially, but after dropping rows with missing values, we are left with only 182 rows. This drastic reduction can lead to loss of valuable information.

#### **2. Dropping Columns with Missing Values**

```python
# Dropping columns with missing values
df_dropped_cols = df.dropna(axis=1)
print("\nColumns after dropping ones with missing values:", df_dropped_cols.columns)
```

**Explanation**:  
If a column has a large number of missing values (e.g., `deck` with 688 missing entries out of 891), it might be reasonable to drop it. However, you shouldn’t drop columns with a few missing values like `age`, which is an important feature for analysis.

### Approach 2: Imputation Techniques

Instead of dropping data, let’s explore **imputation techniques** to fill in missing values:

#### **1. Mean Imputation**

This is useful for numerical columns, especially if the data is approximately normally distributed.

```python
# Plotting Age distribution
import matplotlib.pyplot as plt

sns.histplot(df['age'], kde=True)
plt.title('Age Distribution')
plt.show()

# Filling missing values in 'age' with the mean value
df['age'] = df['age'].fillna(df['age'].mean())
print("\nMissing values in 'age' column after mean imputation:", df['age'].isnull().sum())
```

**Explanation**:  
We replace missing values in the `age` column with the column’s mean. This is effective if the missing values are MCAR or MAR and the data is normally distributed.

#### **2. Median Imputation**

For skewed distributions, the **median** is more robust than the mean.

```python
# Filling missing values in 'age' with the median value
df['age'] = df['age'].fillna(df['age'].median())
```

#### **3. Mode Imputation (for Categorical Columns)**

```python
# Filling missing values in 'embarked' column with mode
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
```

#### **4. Forward Fill & Backward Fill**

These are useful for time-series data.

```python
# Forward fill
df['age'] = df['age'].fillna(method='ffill')

# Backward fill
df['age'] = df['age'].fillna(method='bfill')
```

### Conclusion

We've covered multiple ways to handle missing data, ranging from dropping rows/columns to various imputation techniques like mean, median, mode, and filling methods. Choosing the right method depends on the nature of your dataset and the type of analysis you're planning to perform.

In the next video, we'll dive deeper into **advanced imputation techniques**, including **KNN Imputer** and **Iterative Imputer** from Scikit-Learn. These techniques can handle missing values more effectively, especially when dealing with complex datasets.

---



### Handling Imbalanced Datasets - Feature Engineering Series

Hey everyone! Welcome back to our feature engineering series. In today's session, we're going to focus on **handling imbalanced datasets**, a critical aspect of preparing data for machine learning and deep learning models. 

---

#### What is an Imbalanced Dataset?
Before diving into the techniques to handle imbalanced datasets, let's first understand what we mean by **imbalanced data**.

When working on machine learning projects, especially **classification problems**, the dataset is often divided into different categories or classes. For example:
- **Binary Classification**: Predicting outcomes like Yes/No, True/False, or Spam/Not Spam.

Let's say we have a dataset with **1000 samples**, where our target variable has two categories:
- **Class 1 (Yes)**: 900 samples
- **Class 0 (No)**: 100 samples

This results in a **9:1 ratio** between the two classes. Such a scenario is called an **imbalanced dataset** because one class significantly outnumbers the other.

---

#### Why Should We Address Imbalanced Datasets?
If your model is trained on imbalanced data, it will become biased towards the majority class. For instance, in our previous example, the model might always predict "Yes" because it appears in 90% of the samples. This leads to poor performance on the minority class ("No"), which is often the class of greater interest, especially in real-world applications like fraud detection, medical diagnosis, or rare event prediction.

---

#### Techniques to Handle Imbalanced Datasets
To balance the dataset, we have two main strategies:
1. **Upsampling (Oversampling)**
2. **Downsampling (Undersampling)**

Let's go through each technique with practical examples.

---

### 1. Upsampling the Minority Class
**Upsampling** involves increasing the number of samples in the minority class to match the majority class. This is done by creating synthetic data points, effectively balancing the dataset.

##### Steps:
- Separate the dataset into **majority** and **minority** classes.
- Use the `resample` method from `sklearn.utils` to generate new samples for the minority class.
- Concatenate the original majority class with the newly upsampled minority class.

##### Code Example:

```python
import numpy as np
import pandas as pd
from sklearn.utils import resample

# Fixing random seed for reproducibility
np.random.seed(42)

# Creating a synthetic imbalanced dataset
n_samples = 1000
class_ratio = 0.9  # 90% Class 0, 10% Class 1
n_class_0 = int(n_samples * class_ratio)  # 900 samples
n_class_1 = n_samples - n_class_0  # 100 samples

# Creating dataframes for Class 0 and Class 1
class_0 = pd.DataFrame({
    'Feature1': np.random.normal(0, 1, n_class_0),
    'Feature2': np.random.normal(1, 2, n_class_0),
    'Target': [0] * n_class_0
})

class_1 = pd.DataFrame({
    'Feature1': np.random.normal(1, 1, n_class_1),
    'Feature2': np.random.normal(2, 2, n_class_1),
    'Target': [1] * n_class_1
})

# Concatenating to create the imbalanced dataset
df = pd.concat([class_0, class_1]).reset_index(drop=True)

# Upsampling the minority class
df_minority = df[df['Target'] == 1]
df_majority = df[df['Target'] == 0]

df_minority_upsampled = resample(df_minority,
                                 replace=True,     # sample with replacement
                                 n_samples=n_class_0,  # match number of majority class
                                 random_state=42)

# Creating the upsampled dataset
df_upsampled = pd.concat([df_majority, df_minority_upsampled]).reset_index(drop=True)

# Checking the class distribution after upsampling
print(df_upsampled['Target'].value_counts())
```

##### Output:
```
0    900
1    900
```

As you can see, after upsampling, we have **900 samples** for each class, making the dataset balanced.

---

### 2. Downsampling the Majority Class
**Downsampling** involves reducing the number of samples in the majority class to match the minority class.

##### Steps:
- Separate the dataset into **majority** and **minority** classes.
- Use the `resample` method to randomly select a subset of samples from the majority class.
- Concatenate the downsampled majority class with the original minority class.

##### Code Example:

```python
# Downsampling the majority class
df_majority_downsampled = resample(df_majority,
                                   replace=False,    # sample without replacement
                                   n_samples=n_class_1,  # match number of minority class
                                   random_state=42)

# Creating the downsampled dataset
df_downsampled = pd.concat([df_majority_downsampled, df_minority]).reset_index(drop=True)

# Checking the class distribution after downsampling
print(df_downsampled['Target'].value_counts())
```

##### Output:
```
0    100
1    100
```

Here, we've reduced the majority class samples to **100**, making both classes equal. However, downsampling can lead to **loss of valuable data**, especially if you have a small dataset to begin with.

---

### When to Use Upsampling vs. Downsampling?
- **Upsampling** is generally preferred when you want to preserve all your data and can afford to generate synthetic samples.
- **Downsampling** is useful when you have a large dataset and want to reduce training time and resource consumption.


This video script on **SMOTE (Synthetic Minority Oversampling Technique)** is detailed and educational, guiding viewers through the entire process of handling imbalanced datasets using SMOTE. Here's a refined breakdown and summary of the key concepts, to make it flow more smoothly for your audience:

---

### Video Script: Handling Imbalanced Datasets with SMOTE

---

**Introduction:**

Hello everyone!  
Welcome back to our feature engineering series. In the previous videos, we discussed various techniques to handle imbalanced datasets, specifically focusing on upsampling and downsampling methods. Today, we're diving into a popular upsampling technique called **SMOTE**, which stands for **Synthetic Minority Oversampling Technique**.

**What is SMOTE?**

So, what exactly is SMOTE?  
SMOTE is a technique used in machine learning to address imbalanced datasets where the minority class has significantly fewer instances than the majority class. Unlike traditional upsampling, which simply duplicates existing minority class examples, SMOTE generates **synthetic samples** by interpolating between existing minority class instances. 

This approach helps increase the **variance** of the minority class, making it more diverse and better represented in the dataset.

---

**Difference Between Regular Upsampling and SMOTE:**

To understand this better, let's quickly recap regular upsampling:  
In traditional upsampling, we increase the count of the minority class by duplicating the same data points, which doesn't add any new information. This can lead to **overfitting**, as the duplicated points don't contribute to the diversity of the dataset.

SMOTE, on the other hand, addresses this issue by creating **synthetic data points** between the existing ones, thereby adding variability. Let me visualize this for you.

**Visual Explanation:**

Imagine a 2D feature space with two classes:

- Majority class points are scattered densely on one side (let's mark them as blue).
- Minority class points are sparsely located on the other side (let's mark them as red).

In regular upsampling, we would simply add more red dots at the same existing positions. But in SMOTE, we take two close red points, draw a line between them, and create synthetic points along that line. This method effectively increases the dataset's diversity and reduces the likelihood of overfitting.

---

**Creating a Synthetic Dataset for Demonstration:**

To demonstrate SMOTE, we'll generate an imbalanced dataset using the **`make_classification`** function from `sklearn`. Let's go ahead and create a dataset:

```python
from sklearn.datasets import make_classification

# Generate a dataset
X, y = make_classification(
    n_samples=1000,        # Total 1000 data points
    n_features=2,          # 2 features for easy visualization
    n_clusters_per_class=1,
    weights=[0.9, 0.1],    # 90% majority class, 10% minority class
    n_redundant=0,         # No redundant features
    random_state=42
)
```

This dataset has two features (F1 and F2) and is highly imbalanced, with only 10% of the points belonging to the minority class.

**Visualizing the Dataset:**

Let's visualize this dataset using a scatter plot:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame for visualization
df = pd.DataFrame(X, columns=['F1', 'F2'])
df['target'] = y

# Plotting the dataset
plt.figure(figsize=(8, 5))
plt.scatter(df[df['target'] == 0]['F1'], df[df['target'] == 0]['F2'], label='Majority Class', alpha=0.6)
plt.scatter(df[df['target'] == 1]['F1'], df[df['target'] == 1]['F2'], label='Minority Class', alpha=0.6, color='red')
plt.title('Original Imbalanced Dataset')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid(True)
plt.show()
```

You can see that the minority class (red points) is heavily outnumbered by the majority class (blue points).

---

**Applying SMOTE to Balance the Dataset:**

To apply SMOTE, we will use the **`imbalanced-learn`** library, specifically the `SMOTE` class.

```python
# Install imbalanced-learn if not already installed
# !pip install imbalanced-learn

from imblearn.over_sampling import SMOTE

# Apply SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Check the new class distribution
from collections import Counter
print(f"Original dataset class distribution: {Counter(y)}")
print(f"Resampled dataset class distribution: {Counter(y_resampled)}")
```

---

**Visualizing the Balanced Dataset:**

Now let's visualize the dataset after applying SMOTE:

```python
# Convert resampled data to a DataFrame
df_resampled = pd.DataFrame(X_resampled, columns=['F1', 'F2'])
df_resampled['target'] = y_resampled

# Plot the resampled dataset
plt.figure(figsize=(8, 5))
plt.scatter(df_resampled[df_resampled['target'] == 0]['F1'], df_resampled[df_resampled['target'] == 0]['F2'], label='Majority Class', alpha=0.6)
plt.scatter(df_resampled[df_resampled['target'] == 1]['F1'], df_resampled[df_resampled['target'] == 1]['F2'], label='Minority Class', alpha=0.6, color='red')
plt.title('Balanced Dataset after Applying SMOTE')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid(True)
plt.show()
```

As you can see, SMOTE has created synthetic data points, effectively balancing the class distribution while also adding variability to the minority class.

---

**Conclusion:**

To summarize:
- **SMOTE** is a powerful technique to handle imbalanced datasets by generating synthetic samples.
- It helps prevent overfitting that can occur with traditional upsampling techniques.
- SMOTE increases the diversity of the minority class by interpolating between existing instances.


---

