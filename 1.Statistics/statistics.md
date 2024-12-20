## Topics to Cover

**Descriptive Statistics vs. Inferential Statistics**
**Descriptive statistics**: Summarizing data (e.g., measures of central tendency, measures of dispersion, histograms, box plots).

**Inferential statistics**: Making predictions or inferences about a population based on a sample (e.g., z-test, t-test, ANOVA, chi-square test).

1. **Descriptive Statistics**

   - Measures of Central Tendency
     - Mean
     - Median
     - Mode
   - Measures of Dispersion
     - Variance
     - Standard Deviation
     - Range
   - Data Summarization Tools
     - Histograms
     - Box Plots
     - Whisker Plots
   - Probability Distributions
     - Probability Density Function (PDF)
     - Cumulative Distribution Function (CDF)
     - Gaussian Distribution
     - Log Normal Distribution
     - Binomial Distribution
     - Bernoulli Distribution
     - Pareto Distribution (Power Law Distribution)
     - Standard Normal Distribution
   - Statistical Transformation Techniques
     - Standardization
     - Q-Q Plot Analysis

- **Inferential Statistics**

  - Hypothesis Testing
    - Null Hypothesis
    - Alternative Hypothesis
  - Statistical Tests
    - Z-test
    - T-test
    - ANOVA (Analysis of Variance)
      - F-test
      - Factorial ANOVA
    - Chi-square test
  - P-values
  - Confidence Intervals
  - Statistical Tables
    - Z-tables
    - T-tables
    - Chi-square tables
- **Sampling Techniques**

  - Simple Random Sampling
  - Stratified Sampling
  - Systematic Sampling
  - Convenience Sampling
- **Applications and Examples**

  - Exit Poll Analysis
  - Household Surveys
  - Drug Testing Sampling Strategies

1. **Basic Definitions**
   - Statistics: The science of collecting, organizing, and analyzing data to make better decisions.
   - Data: Facts or pieces of information that can be measured.
   - Types of Statistics: Descriptive (organizing and summarizing data) and Inferential (using data to form conclusions).

## Key Concepts and Examples

### Descriptive Statistics

- Example: Calculating the average age of students in a class.
- Measures: Central tendency (mean, median, mode), dispersion (variance, standard deviation), data visualization (histograms, box plots).

### Inferential Statistics

- Example: Determining if the average marks of students in one classroom are similar to the average marks of students in the entire college.
- Techniques: Using sample data to make inferences about a population, hypothesis testing, confidence intervals.

### Population and Sample

- Population: The entire group being studied, denoted by$N$.
- Sample: A subset of the population, denoted by$n$.
- Example: Conducting an exit poll by surveying a sample of voters to infer the preferences of the entire population.

## Sampling Techniques

1. **Simple Random Sampling**

   - Definition: Every member of the population has an equal chance of being selected.
   - Example: Randomly selecting individuals for a survey.
2. **Stratified Sampling**

   - Definition: The population is divided into non-overlapping groups (strata) and samples are taken from each group.
   - Example: Sampling based on gender (male, female) or age groups.
3. **Systematic Sampling**

   - Definition: Selecting every nth individual from the population.
   - Example: Surveying every 8th person entering a mall.
4. **Convenient Sampling**

   - Definition: Sampling individuals who are conveniently available.
   - Example: Surveying individuals who have expertise in a specific topic like data science.

## Practical Applications

- **Election Polls**: Using random sampling to predict election results.
- **Household Surveys**: RBI using stratified or random sampling for surveys.
- **Drug Testing**: Using stratified sampling based on age groups for testing new drugs.

## Conclusion

Understanding both descriptive and inferential statistics is crucial for making informed decisions based on data. Using various sampling techniques ensures that the data collected is representative and reliable. Throughout this course, we will dive deep into these concepts and apply them using Python, enabling you to tackle real-world data science problems efficiently. Let's start our journey by understanding the fundamental concepts of statistics!

## Variables

### What is a Variable?

A variable is a property that can take on any value. For example, height and weight are variables. They can have values like 170 cm, 172 cm, 185 cm, 190 cm for height and values like 78 kg, 99 kg, 100 kg, 60 kg, 50 kg for weight.

### Types of Variables

There are two kinds of variables:

1. **Quantitative Variables**
2. **Qualitative (Categorical) Variables**

#### Quantitative Variables

Quantitative variables can be measured numerically. We can perform various operations like addition, subtraction, division, and multiplication on them. Examples include:

- Age
- Weight
- Height

Quantitative variables can be further divided into two types:

1. **Discrete Variables:** These can only take whole numbers.

   - Examples: Number of bank accounts, number of children in a family.
2. **Continuous Variables:** These can take any numerical value.

   - Examples: Height, weight, amount of rainfall.

#### Qualitative (Categorical) Variables

Qualitative variables are based on characteristics and cannot be measured numerically. We cannot perform mathematical operations on them. Examples include:

- Gender (male, female)
- IQ categories (0-10: less IQ, 10-50: medium IQ, 50-100: good IQ)
- Blood group (A positive, A negative)
- T-shirt size (large, XL, medium, small)

### Examples of Variable Types

- **Gender:** Qualitative or categorical
- **Marital Status:** Qualitative or categorical
- **River Length:** Quantitative (continuous)
- **Population of a State:** Quantitative (discrete)
- **Song Length:** Quantitative (continuous)
- **Blood Pressure:** Quantitative (continuous)
- **Pin Code:** Discrete or categorical

Understanding the types of variables is crucial for handling them appropriately in data science problems.

### Variable Measurement

We have four different types of measured variables:

1. **Nominal**
2. **Ordinal**
3. **Interval**
4. **Ratio**

Understanding these types is crucial because your dataset will contain these variables, enabling you to perform effective data analysis. Let’s explore each type:

#### Nominal

Nominal data, also known as categorical or qualitative data, is divided into different classes. Examples include:

- Colors
- Gender
- Types of flowers

This type of data is used to label variables without providing any quantitative value.

#### Ordinal

In ordinal data, the order of values matters, but the specific value does not. For instance:

- Students' marks: 100, 96, 57, 85, 44
  - Ranks: 1st, 2nd, 3rd, 4th, 5th

Here, the focus is on the order (ranks) rather than the actual values (marks).

#### Interval

Interval data has meaningful order and values, but lacks a true zero. For example:

- Temperature in Fahrenheit: 70-80°F, 80-90°F
- Distance ranges: 10-20 miles, 20-30 miles

Zero Fahrenheit does not signify the absence of temperature.

#### Ratio

Ratio data has all the properties of interval data, but with a meaningful zero point, indicating the absence of the variable being measured. This means you can make meaningful statements about how many times greater one object is compared to another. Examples include:

- **Height:** Zero height means the absence of height.
- **Weight:** Zero weight means the absence of weight.
- **Income:** Zero income means no income.
- **Distance:** Zero distance means no distance traveled.

### Examples and Analysis

#### Height

- **Data:** 150 cm, 160 cm, 170 cm, 180 cm, 190 cm
- **Properties:**
  - Order matters: 150 cm < 160 cm < 170 cm < 180 cm < 190 cm
  - Value matters: The difference between 150 cm and 160 cm is the same as between 180 cm and 190 cm.
  - True zero: A height of 0 cm indicates no height.

#### Weight

- **Data:** 50 kg, 60 kg, 70 kg, 80 kg, 90 kg
- **Properties:**
  - Order matters: 50 kg < 60 kg < 70 kg < 80 kg < 90 kg
  - Value matters: The difference between 50 kg and 60 kg is the same as between 80 kg and 90 kg.
  - True zero: A weight of 0 kg indicates no weight.

#### Income

- **Data:** $30,000, $40,000, $50,000, $60,000, $70,000
- **Properties:**
  - Order matters: $30,000 < $40,000 < $50,000 < $60,000 < $70,000
  - Value matters: The difference between $30,000 and $40,000 is the same as between $60,000 and $70,000.
  - True zero: An income of $0 indicates no income.

#### Distance

- **Data:** 10 km, 20 km, 30 km, 40 km, 50 km
- **Properties:**
  - Order matters: 10 km < 20 km < 30 km < 40 km < 50 km
  - Value matters: The difference between 10 km and 20 km is the same as between 40 km and 50 km.
  - True zero: A distance of 0 km indicates no distance traveled.

### Key Points

- **Order Matters:** Like ordinal and interval data, the order of values in ratio data is meaningful.
- **Value Matters:** The difference between values is consistent and meaningful.
- **True Zero:** Unlike interval data, ratio data has a true zero, making statements like "twice as much" meaningful.

Understanding the type of data you're working with is crucial for selecting appropriate statistical methods and analyses. Ratio data allows for a wide range of statistical techniques, including all those applicable to interval data, plus additional operations such as meaningful ratios and percentages.

### Frequency Distribution

Understanding frequency distribution is essential for visualizing datasets. Let’s consider a dataset with three types of flowers: Rose, Lily, and Sunflower.

```
Rose, Lily, Sunflower, Rose, Lily, Lily, Lily
```

Creating a frequency distribution table:

| Flower    | Frequency |
| ----------- | ----------- |
| Rose      | 3         |
| Lily      | 4         |
| Sunflower | 2         |

#### Cumulative Frequency

Cumulative frequency sums the frequencies sequentially:

- Rose: 3
- Rose + Lily: 3 + 4 = 7
- Rose + Lily + Sunflower: 3 + 4 + 2 = 9

### Visualizing Data

Using frequency distribution, we can derive bar charts, pie charts, etc.

#### Bar Graph

For discrete variables, we use bar graphs. Example:

- **X-axis:** Flower types (Rose, Lily, Sunflower)
- **Y-axis:** Frequency

```plaintext
Rose:      ###
Lily:      ####
Sunflower: ##
```

#### Histogram

For continuous variables, we use histograms. Example with ages:

- Ages: 10, 12, 14, 18, 24, 26, 30, 35, 36, 37, 40, 41, 42, 43, 50, 51

Bins (default size 10):

- 0-10: 0
- 10-20: 4 (10, 12, 14, 18)
- 20-30: 3 (24, 26, 30)
- 30-40: 4 (35, 36, 37, 40)
- 40-50: 4 (41, 42, 43, 50)
- 50-60: 1 (51)

```plaintext
10-20: ####
20-30: ###
30-40: ####
40-50: ####
50-60: #
```

#### Probability Density Function (PDF)

PDF is the smoothening of a histogram using a Kernel Density Estimator (KDE). It’s an advanced topic we’ll cover later.

### Bar Graph vs Histogram

- **Bar Graph:** Used for discrete data
- **Histogram:** Used for continuous data

A probability density function (PDF) smoothens histograms for continuous data representation.

Sure, let's break down the topics covered in your session and prepare a more structured version.

---

# Statistics for Data Science: Intermediate Level

## Overview

In this session, we will cover intermediate statistical concepts crucial for data science. Specifically, we will delve into:

1. Measure of Central Tendency
2. Measure of Dispersions
3. Gaussian Distribution
4. Z Score
5. Standard Normal Distribution

## Measure of central tendency

### 1. **Mean (Arithmetic Average)**

#### **Definition**

The mean is the sum of all values divided by the number of values.

#### **Formula**

- For a population:
     $$ \mu = \frac{\sum x_i}{N} $$

- For a sample:  
 $$ \bar{x} = \frac {\sum x_i}{n}  $$

#### **Application**

- **General Use**: Provides a central value for symmetric distributions without extreme outliers.
- **Economics**: Average income, average spending.
- **Education**: Average test scores, average grades.

#### **Impact with Increasing/Decreasing Values**

- **Increasing Values**: As values increase, the mean will increase. For example, if you add higher values to the dataset, the mean rises.
- **Decreasing Values**: As values decrease, the mean will decrease. Adding lower values pulls the mean down.

#### **Example**

For dataset {5, 10, 15}, the mean is 10. Adding a large value like 50 changes the mean to
$$ \frac{5 + 10 + 15 + 50}{4} = 20 $$

### 2. **Median**

#### **Definition**

The median is the middle value when data is ordered. If the dataset has an even number of observations, it's the average of the two middle values.

#### **Application**

- **Income**: Median income provides a better representation of typical income, especially in skewed distributions.
- **Housing**: Median house prices are less affected by extreme values compared to the mean.
- **Education**: Median scores reflect the typical performance better in skewed distributions.

#### **Impact with Increasing/Decreasing Values**

- **Increasing Values**: The median remains stable unless the values added change the middle position. For instance, adding values to the dataset might not affect the median if the added values do not change the order.
- **Decreasing Values**: Similarly, decreasing values might not impact the median if they do not shift the middle value or the middle position of the ordered data.

#### **Example**

For dataset {1, 3, 5}, the median is 3. Adding values 2 and 4, the median becomes
$$ \frac{3+4}{2} = 3.5 $$
(since now the dataset is {1, 2, 3, 4, 5}).

### 3. **Mode**

#### **Definition**

The mode is the value that appears most frequently in a dataset. There can be one mode (unimodal), more than one mode (bimodal or multimodal), or no mode if no value repeats.

#### **Application**

- **Retail**: Identifying the most popular product.
- **Marketing**: Understanding the most common customer preference.
- **Health**: Most common diagnosis or symptom in a population.

#### **Impact with Increasing/Decreasing Values**

- **Increasing Values**: If new values that are different from the existing values are added, the mode might remain unchanged or become a new value if it appears frequently.
- **Decreasing Values**: Removing values can affect the mode, especially if the removed values were the most frequent ones.

#### **Example**

For dataset {1, 2, 2, 3, 4}, the mode is 2. Adding more values like {2, 2, 5} makes 2 appear more frequently, reinforcing it as the mode.

### 4. **Geometric Mean**

#### **Definition**

The geometric mean is the nth root of the product of n values. It's used for rates of growth or percentages.

#### **Application**

- **Finance**: Average growth rates of investments.
- **Biology**: Average rates of biological processes.
- **Economics**: Average rates of inflation.

#### **Impact with Increasing/Decreasing Values**

- **Increasing Values**: Increasing values will affect the geometric mean, but it is less sensitive to extreme values compared to the arithmetic mean. The geometric mean will increase but not as rapidly as the arithmetic mean.
- **Decreasing Values**: If very small values are introduced, especially values close to zero, the geometric mean can be significantly reduced.

#### **Example**

For dataset {2, 8}, the geometric mean is 
$$ \sqrt{2 \times 8} = \sqrt{16} = 4 $$
 Adding larger values will generally increase the geometric mean.

### 5. **Harmonic Mean**

#### **Definition**

The harmonic mean is the reciprocal of the arithmetic mean of the reciprocals of the values. It's used for rates or ratios.

#### **Application**

- **Finance**: Average rates of return on investments.
- **Physics**: Average speed or velocity calculations.

#### **Impact with Increasing/Decreasing Values**

- **Increasing Values**: As the values increase, the harmonic mean increases, but it is influenced more by smaller values, so it increases more slowly compared to the arithmetic mean.
- **Decreasing Values**: Very small values will decrease the harmonic mean significantly. Adding values close to zero can drastically lower the harmonic mean.

#### **Example**

For dataset {1, 2, 4}, the harmonic mean is 
$$ \frac{3}{\frac{1}{1} + \frac{1}{2} + \frac{1}{4}} = \frac{3}{1.75} \approx 1.71 $$
 Adding very small values will reduce this mean significantly.

### Summary of Impact

- **Mean**: Sensitive to extreme values; increases/decreases with values.
- **Median**: Less sensitive to extreme values; stable unless values shift the middle.
- **Mode**: Dependent on frequency; changes if the most frequent values change.
- **Geometric Mean**: Sensitive to extreme values but less so than the arithmetic mean; useful for growth rates.
- **Harmonic Mean**: Sensitive to small values; useful for rates and ratios.
-

### Example

Given the dataset: $\{ 1, 2, 2, 3, 4, 5, 6\}$

- Range:$6 - 1 = 5$
- Variance and standard deviation calculations can be performed using appropriate formulas or software tools.

## Measure of Dispersion

Measures of dispersion quantify the spread or variability of a dataset. Understanding these measures helps in analyzing the consistency and variability within the data. Here are the main measures of dispersion, their applications, and how changes in the data impact them:

### 1. **Range**
   - **Definition**: The difference between the maximum and minimum values in a dataset.
   - **Formula**: Range = Max value - Min value
   - **Application**:
     - **Weather Data**: Range of temperatures in a city over a month.
     - **Finance**: Range of stock prices over a period.
   - **Impact of Changes**:
     - **Increasing Data**: Adding higher values increases the range.
     - **Decreasing Data**: Adding lower values decreases the range.

### 2. **Variance**
   - **Definition**: The average of the squared differences between each data point and the mean.
   - **Formula**:
     - Population variance: $$ \sigma^2 = \frac{\sum (x_i - \mu)^2}{N} $$
     - Sample variance: $$ s^2 = \frac{\sum (x_i - \bar{x})^2}{n-1} $$
   - **Application**:
     - **Finance**: Measure of investment risk (volatility).
     - **Quality Control**: Variance in product measurements.
   - **Impact of Changes**:
     - **Increasing Data**: Variance increases if the new data points are far from the mean.
     - **Decreasing Data**: Variance decreases if new data points are closer to the mean or less dispersed.

### 3. **Standard Deviation**
   - **Definition**: The square root of the variance, providing a measure of spread in the same units as the data.
   - **Formula**:
     - Population standard deviation: $$ \sigma = \sqrt{\frac{\sum (x_i - \mu)^2}{N}} $$
     - Sample standard deviation: $$ s = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n-1}} $$
   - **Application**:
     - **Education**: Standard deviation of test scores to understand performance variation.
     - **Finance**: Volatility of asset returns.
   - **Impact of Changes**:
     - **Increasing Data**: Standard deviation increases if new data points are more spread out from the mean.
     - **Decreasing Data**: Standard deviation decreases if data points are more closely clustered around the mean.

### 4. **Interquartile Range (IQR)**
   - **Definition**: The difference between the third quartile (Q3) and the first quartile (Q1), representing the range within which the middle 50% of the data lies.
   - **Formula**: IQR = Q3 - Q1
   - **Application**:
     - **Outlier Detection**: Identifying outliers using IQR-based methods.
     - **Data Distribution**: Understanding the spread of the central portion of the data.
   - **Impact of Changes**:
     - **Increasing Data**: IQR increases if the new data points affect Q1 or Q3 significantly.
     - **Decreasing Data**: IQR decreases if the central 50% of the data becomes narrower.

### 5. **Mean Absolute Deviation (MAD)**
   - **Definition**: The average of the absolute differences between each data point and the mean.
   - **Formula**: $$ MAD = \frac{\sum |x_i - \bar{x}|}{n} $$
   - **Application**:
     - **Finance**: Assessing the average deviation in financial data.
     - **Operations**: Evaluating consistency in production processes.
   - **Impact of Changes**:
     - **Increasing Data**: MAD increases if new data points are further from the mean.
     - **Decreasing Data**: MAD decreases if data points are closer to the mean.

### 6. **Coefficient of Variation (CV)**
   - **Definition**: A standardized measure of dispersion relative to the mean, expressed as a percentage.
   - **Formula**: $$ CV = \frac{\sigma}{\bar{x}} \times 100 $$
   - **Application**:
     - **Comparing Variability**: Comparing variability between datasets with different units or means.
     - **Risk Assessment**: Assessing relative risk in finance.
   - **Impact of Changes**:
     - **Increasing Data**: CV increases if the standard deviation increases relative to the mean.
     - **Decreasing Data**: CV decreases if the mean increases relative to the standard deviation.

### Summary of Impacts:
- **Range**: Directly affected by extreme values at the ends of the dataset.
- **Variance and Standard Deviation**: Affected by the overall spread of the data points around the mean; more spread increases these values.
- **Interquartile Range (IQR)**: Less sensitive to extreme values and focuses on the middle spread of data.
- **Mean Absolute Deviation (MAD)**: Provides a simple average of absolute deviations and is less influenced by extreme values compared to variance and standard deviation.
- **Coefficient of Variation (CV)**: Useful for comparing relative variability, especially when means differ significantly.

Each measure of dispersion provides a different perspective on the variability in a dataset, and their changes can reflect different aspects of data distribution and spread.

## 3. Gaussian Distribution (Normal Distribution)

### Definition

A continuous probability distribution characterized by a bell-shaped curve, symmetric about the mean.

### Properties

- Mean $\mu$
- Standard deviation $\sigma$

## 4. Z Score

### Definition

A measure of how many standard deviations an element is from the mean.

### Formula

<!-- $\frac123$ -->

$$
Z = \frac{(X - \mu)}{\sigma}
$$

## 5. Standard Normal Distribution

### Definition

A normal distribution with a mean of 0 and a standard deviation of 1.

### Conversion

Any normal distribution can be converted to a standard normal distribution using the Z-score formula.

---

These are the core topics for today's session. We will dive deeper into each concept, solve problems, and understand their applications in data science. Feel free to ask questions as we progress through each section.

### Population Mean

**Formula**:
$$
\mu = \frac{\sum_{i=1}^{N} x_i}{N}
$$
Where:

- $\mu$ is the population mean.
- $x_i$ represents each value in the population.
- N is the total number of values in the population.

### Sample Mean

**Formula**:

$$ \bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}
$$
Where:

- \(\bar{x}\) is the sample mean.
- \(x_i\) represents each value in the sample.
- \(n\) is the number of values in the sample.

These formulas allow you to calculate the average value of a dataset, whether you are dealing with the entire population or just a sample from that population.

### Measures of Dispersion: Variance and Standard Deviation

Measures of dispersion help us understand the spread or variability of a dataset. The two primary measures we will discuss are **variance** and **standard deviation**.

#### Variance

Variance measures the average degree to which each point differs from the mean. It gives us an idea of how spread out the data points are. There are two types of variance: population variance and sample variance.

- **Population Variance $\sigma^2$)**:
  $$
  \sigma^2 = \frac{\sum_{i=1}^N (x_i - \mu)^2}{N}
  $$
  Where N is the total number of observations, $x_i$ are the individual data points, and $\mu$ is the population mean.
- **Sample Variance $s^2$**:
  $$
  s^2 = \frac{\sum_{i=1}^n (x_i - \bar{x})^2}{n - 1}
  $$
  Where n is the number of sample observations, $x_i$ are the individual data points, and
  $\bar{x}$ is the sample mean.

  The use of n-1 instead of n is known as Bessel's correction, which corrects the bias in the estimation of the population variance from a sample.

#### Standard Deviation

Standard deviation is the square root of the variance, providing a measure of dispersion in the same units as the original data, which makes it more interpretable.

- **Population Standard Deviation ($\sigma$)**:
  $$
  \sigma = \sqrt{\sigma^2} = \sqrt{\frac{\sum_{i=1}^N (x_i - \mu)^2}{N}}
  $$
- **Sample Standard Deviation $s$**:
  
  $$
  s = \sqrt{s^2} = \sqrt{\frac{\sum_{i=1}^n (x_i - \bar{x})^2}{n - 1}}
  $$

### Example Calculation

Let's consider a dataset: 1, 2, 2, 3, 4, 5

1. **Calculate the Mean ($\bar{x}$)**:
   $$
   \bar{x} = \frac{1 + 2 + 2 + 3 + 4 + 5}{6} = 2.83
   $$
2. **Calculate $x_i - \bar{x}$ for each data point**:
   $$
   \begin{align*}
   1 - 2.83 &= -1.83 \\
   2 - 2.83 &= -0.83 \\
   2 - 2.83 &= -0.83 \\
   3 - 2.83 &= 0.17 \\
   4 - 2.83 &= 1.17 \\
   5 - 2.83 &= 2.17 \\
   \end{align*}
   $$
3. **Square each result**:
   $$
   \begin{align*}
   (-1.83)^2 &= 3.35 \\
   (-0.83)^2 &= 0.69 \\
   (-0.83)^2 &= 0.69 \\
   0.17^2 &= 0.03 \\
   1.17^2 &= 1.37 \\
   2.17^2 &= 4.71 \\
   \end{align*}
   $$
4. **Sum of squared differences**:
   $$
   3.35 + 0.69 + 0.69 + 0.03 + 1.37 + 4.71 = 10.84
   $$
5. **Calculate the Sample Variance**:
   $$
   s^2 = \frac{10.84}{6 - 1} = \frac{10.84}{5} = 2.168
   $$
6. **Calculate the Sample Standard Deviation**:
   $$
   s = \sqrt{2.168} \approx 1.47
   $$

### Interpretation

- **Variance**: A higher variance indicates that the data points are more spread out from the mean, while a lower variance indicates that they are closer to the mean.
- **Standard Deviation**: This gives a more intuitive sense of dispersion. For example, in the above dataset, the standard deviation of approximately 1.47 suggests that most data points lie within 1.47 units of the mean (2.83).

By understanding and calculating these measures of dispersion, we can better interpret the variability and spread of data in various contexts.

## Understanding Percentiles and Quartiles to Identify Outliers

### Basics of Percentiles

To begin, let’s first understand the concept of percentiles. Before diving into percentiles, it's essential to grasp the idea of percentages. Suppose we have a small dataset: `[1, 2, 3, 4, 5]`. If we want to find the percentage of numbers that are odd, we can use the formula:

$$ \text{Percentage} = \left(\frac{\text{Number of odd numbers}}{\text{Total number of numbers}}\right) \times 100 $$

In this case, there are 3 odd numbers (1, 3, 5) out of 5. So,

$$ \text{Percentage} = \left(\frac{3}{5}\right) \times 100 = 60\% $$

### Defining Percentiles

Percentiles, on the other hand, are a bit more specific. A percentile is a value below which a certain percentage of observations fall. For example, if we say a value is at the 25th percentile, it means 25% of the data is below that value.

#### Formula for Percentile Rank

To find the perce ntile rank of a given value `X` in a dataset, we use:

$$ \text{Percentile rank} = \left(\frac{\text{Number of values below } X}{\text{Total number of values}}\right) \times 100 $$

Consider the dataset `[2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 9, 10, 11, 11, 12]`. To find the percentile rank of 10:

1. Count the number of values below 10: 13
2. Total number of values: 16
3. Apply the formula:

$$ \text{Percentile rank of 10} = \left(\frac{13}{16}\right) \times 100 = 81.25 $$

Thus, 10 is at the 81.25th percentile, meaning 81.25% of the values are less than 10.

### Finding the Value at a Given Percentile

To find the value at a given percentile (e.g., 25th percentile):

$$ \text{Index} = \left(\frac{\text{Percentile}}{100}\right) \times (N + 1) $$

For the 25th percentile in our dataset:

1. Percentile = 25
2. N = 16
3. Apply the formula:

$$ \text{Index} = \left(\frac{25}{100}\right) \times (16 + 1) = 4.25 $$

The 4.25th index value falls between the 4th and 5th values in the sorted dataset (which are 4 and 5). So, we average them:

$$ \text{Value} = \frac{4 + 5}{2} = 4.5 $$

### Five-Number Summary and IQR for Outliers

A five-number summary includes:

1. Minimum value
2. First Quartile (Q1, or 25th percentile)
3. Median (Q2, or 50th percentile)
4. Third Quartile (Q3, or 75th percentile)
5. Maximum value

The interquartile range (IQR) is:

$$ \text{IQR} = Q3 - Q1 $$

To detect outliers, we define:

- Lower fence:$Q1 - 1.5 \times \text{IQR}$
- Upper fence:$Q3 + 1.5 \times \text{IQR}$

Values outside this range are considered outliers.

#### Example

Using the dataset `[1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 7, 8, 8, 9, 27]`:

1. Calculate Q1 and Q3:
   - Q1 (25th percentile) = 3
   - Q3 (75th percentile) = 7
2. Calculate IQR:

$$ \text{IQR} = 7 - 3 = 4 $$

3. Calculate fences:
   - Lower fence =$3 - 1.5 \times 4 = -3$
   - Upper fence =$7 + 1.5 \times 4 = 13$

4. Identify outliers: Any value outside \([-3, 13]\). Thus, 27 is an outlier.

### Visualizing with a Box Plot

A box plot can visually represent this five-number summary and outliers:

1. Minimum (1)
2. Q1 (3)
3. Median (5)
4. Q3 (7)
5. Maximum (excluding outliers) (9)
6. Outlier (27, marked separately)

By understanding and using percentiles, quartiles, and the IQR, we can effectively identify and handle outliers in a dataset. This statistical method helps maintain data integrity and ensure accurate analysis.

### Gaussian or Normal Distribution

Normal distribution, also known as Gaussian distribution, is crucial in statistics. Key characteristics include:

1. Symmetry around the mean
2. Mean = Median = Mode
3. 68-95-99.7 Rule:
   - 68% of data within 1 standard deviation of the mean
   - 95% within 2 standard deviations
   - 99.7% within 3 standard deviations

This distribution helps in various analyses, such as determining probabilities and identifying unusual data points.

Sure, here's the explanation and steps you outlined in markdown format:

---

# Understanding Z-Scores and Standard Normal Distribution

## Bell Curve and Z-Scores

Given a bell curve with:

- Mean $\mu$ = 4
- Standard Deviation $\sigma$ = 1

Values on the curve:

- 1, 2, 3, 4, 5, 6

### Applying Z-Scores

The formula for the Z-score is:
$$ Z = \frac{(X_i - \mu)}{\sigma} $$

Using the given mean and standard deviation:

1. $Z(1) = \frac{1 - 4}{1} = -3$
2. $Z(2) = \frac{2 - 4}{1} = -2$
3. $Z(3) = \frac{3 - 4}{1} = -1$
4. $Z(4) = \frac{4 - 4}{1} = 0$
5. $Z(5) = \frac{5 - 4}{1} = 1$
6. $Z(6) = \frac{6 - 4}{1} = 2$

### Resulting Distribution

After applying Z-scores, the new distribution is:
$$ -3, -2, -1, 0, 1, 2 $$

### Understanding the Standard Normal Distribution

By converting the original values to Z-scores, the distribution becomes a **Standard Normal Distribution** with:

- Mean = 0
- Standard Deviation = 1

A random variable \(X\) can be denoted as belonging to a standard normal distribution, written as \(X \sim N(0, 1)\).

## Importance of Standard Normal Distribution

### Example in Machine Learning

Consider a dataset with features:

- Age (years)
- Salary (dollars)
- Weight (kgs)

### Applying Standardization

Standardization involves converting each feature to a standard normal distribution using Z-scores. This process is important for ensuring that all features contribute equally to the model's learning process.

### Normalization vs. Standardization

- **Standardization**: Converts the data to a distribution with mean = 0 and standard deviation = 1.
- **Normalization**: Scales data to a specific range, typically [0, 1] using a Min-Max Scaler.

#### Normalization Example

For image processing in deep learning (e.g., CNNs), pixel values (0-255) are normalized to [0, 1] by dividing by 255.

## Practical Example with Z-Scores

### Comparing Performance in Cricket Matches

#### Data for 2021 Series

- Mean Score $\mu$ = 250
- Standard Deviation $\sigma$ = 10
- Team's Final Score $X_i$ = 240

Calculate the Z-score:
$$ Z = \frac{(240 - 250)}{10} = -1 $$

#### Data for 2020 Series

- Mean Score $\mu$ = 260
- Standard Deviation $\sigma$ = 12
- Team's Final Score $X_i$ = 245

Calculate the Z-score:
$$ Z = \frac{(245 - 260)}{12} = -1.25 $$

### Interpretation

- In 2021, the Z-score is -1.
- In 2020, the Z-score is -1.25.

The Z-score tells us how many standard deviations an element is from the mean. A higher Z-score (less negative) indicates better performance relative to the series' mean score. Thus, the team performed better in 2021 as compared to 2020.

### Visualization

![alt text](image.png)

- **2021 Series**: Mean = 250, Standard Deviation = 10
  - 240 falls at -1 standard deviation
- **2020 Series**: Mean = 260, Standard Deviation = 12
  - 245 falls at -1.25 standard deviations

From this, we infer that the team performed relatively better in 2021 than in 2020 based on the Z-scores.

Alright, let's break down the practical example of calculating the percentage of scores that fall above a given value using the Z-score, with an explanation and Python code to illustrate the process.

### Problem Statement

You have a dataset with the following values:
\[4, 5, 6, 7, 3, 2, 1$$
The mean of this dataset is 4, and the standard deviation is 1. You need to find the percentage of scores that are greater than 4.25.

### Step-by-Step Solution

1. **Calculate the Z-Score:**
   The Z-score formula is given by:
   $$
   Z = \frac{X - \mu}{\sigma}
   $$
   where$X$ is the value (4.25),$\mu$ is the mean (4), and$\sigma$ is the standard deviation (1).

   So,
   $$
   Z = \frac{4.25 - 4}{1} = 0.25
   $$

2. **Find the Area to the Right of the Z-Score:**
   We need to find the area under the standard normal curve to the right of the Z-score (0.25). This can be found using Z-tables or a standard normal distribution function in Python.

3. **Calculate the Percentage:**
   The area to the right of the Z-score gives us the percentage of scores that fall above 4.25.

### Implementation in Python

![alt text](image-1.png)
Let's implement this in Python to make it more concrete:

```python
import numpy as np
import scipy.stats as stats

# Given data
mean = 4
std_dev = 1
x_value = 4.25

# Calculate Z-score
z_score = (x_value - mean) / std_dev

# Find the area to the right of the Z-score using the cumulative distribution function (CDF)
area_to_right = 1 - stats.norm.cdf(z_score)

# Convert to percentage
percentage = area_to_right * 100

print(f"Percentage of scores above {x_value}: {percentage:.2f}%")
```

### Explanation of the Code

1. **Calculate the Z-Score:**
   $$
   z\_score = \frac{x\_value - mean}{std\_dev}
   $$

2. **Calculate the Cumulative Distribution Function (CDF):**
   The `stats.norm.cdf(z_score)` function gives the cumulative probability up to the Z-score. We subtract this value from 1 to get the area to the right of the Z-score.

3. **Convert to Percentage:**
   Multiply the area to the right by 100 to get the percentage.

### Understanding the Result

The percentage of scores above 4.25 in the given dataset is approximately 40%. This means that 40% of the scores in the dataset are greater than 4.25.

This method is widely used in statistics, especially in hypothesis testing and confidence interval estimation, making it an essential concept for both academic purposes and practical applications in data analysis.

# Probability

Probability is super important and widely used in machine learning, deep learning, and many other fields. In this session, we'll discuss major concepts and applications of probability.

## Definition

Probability is a measure of the likelihood of an event. To understand probability, consider the following examples:

### Example 1: Rolling a Die

When rolling a die, the possible outcomes are \(1, 2, 3, 4, 5, 6\). If we want to find the probability of getting a 6, we can use the formula:

$$P(\text{Event}) = \frac{\text{Number of ways an event can occur}}{\text{Number of possible outcomes}} $$

Here, the number of ways to get a 6 is 1, and the number of possible outcomes is 6. Therefore:

$$P(6) = \frac{1}{6} $$

### Example 2: Tossing a Coin

When tossing a coin, the possible outcomes are heads (H) and tails (T). The probability of getting heads is:

$$P(H) = \frac{1}{2} $$

## Addition Rule

The addition rule is used to find the probability of either of two events occurring. It comes in two forms:

1. **Mutually Exclusive Events**: Events that cannot occur at the same time.
2. **Non-Mutually Exclusive Events**: Events that can occur at the same time.

### Mutually Exclusive Events

If two events are mutually exclusive, the probability of either event occurring is the sum of their individual probabilities:

$$P(A \text{ or } B) = P(A) + P(B) $$

#### Example: Tossing a Coin

If we want to find the probability of getting heads or tails, we use:

$$P(H \text{ or } T) = P(H) + P(T) = \frac{1}{2} + \frac{1}{2} = 1 $$

### Non-Mutually Exclusive Events

For non-mutually exclusive events, we need to subtract the probability of both events occurring:

$$P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B) $$

#### Example: Drawing a Card

Consider a deck of cards. What is the probability of drawing a queen or a heart?

- $P(\text{Queen}) = \frac{4}{52}$
-$P(\text{Heart}) = \frac{13}{52}$
-$P(\text{Queen and Heart}) = \frac{1}{52}$

So,

$$ P(\text{Queen or Heart}) = \frac{4}{52} + \frac{13}{52} - \frac{1}{52} = \frac{16}{52} = \frac{4}{13} $$

## Multiplication Rule

The multiplication rule is used to find the probability of both of two events occurring. It comes in two forms:

1. **Independent Events**: The occurrence of one event does not affect the occurrence of the other.
2. **Dependent Events**: The occurrence of one event affects the occurrence of the other.

### Independent Events

For independent events, the probability of both events occurring is the product of their individual probabilities:

$P(A \text{ and } B) = P(A) \times P(B)$

#### Example: Rolling a Die

What is the probability of rolling a 5 and then a 4?

$P(5 \text{ and } 4) = P(5) \times P(4) = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36}$

### Dependent Events

For dependent events, the probability of both events occurring is:

$P(A \text{ and } B) = P(A) \times P(B|A)$

Where $P(B|A)$is the conditional probability of $B$ given $A$.

#### Example: Drawing Cards

What is the probability of drawing a queen and then an ace from a deck of cards?

- $P(\text{Queen}) = \frac{4}{52}$
- After drawing a queen, $P(\text{Ace}) = \frac{4}{51}$

So,

$$ P(\text{Queen and Ace}) = \frac{4}{52} \times \frac{4}{51} = \frac{16}{2652} = \frac{4}{663} $$

## Permutation and Combination

Permutation and combination are used to calculate the number of ways to arrange or select items.

### Permutation

Permutation is used when the order of items matters.

#### Example: Arranging Chocolates

If there are 6 different chocolates, and we want to know the number of ways to arrange the first 3:

$$ P(n, r) = \frac{n!}{(n-r)!} = \frac{6!}{(6-3)!} = 6 \times 5 \times 4 = 120 $$

### Combination

Combination is used when the order of items does not matter.

#### Example: Selecting Chocolates

If we want to select 3 chocolates out of 6:

$$ C(n, r) = \frac{n!}{r!(n-r)!} = \frac{6!}{3!(6-3)!} = \frac{6 \times 5 \times 4}{3 \times 2 \times 1} = 20
$$

Sure, let's break down and clarify the concepts of permutations, combinations, and then delve into p-values and hypothesis testing.

### Permutations and Combinations

#### Permutations

Permutations refer to the arrangement of objects in a specific order. The order of elements is significant. For example, if you have three elements A, B, and C, the permutations would include ABC, ACB, BAC, BCA, CAB, and CBA.

The formula to calculate permutations of $n$items taken $r$at a time is:
$$P(n, r) = \frac{n!}{(n-r)!}$$

#### Combinations

Combinations refer to the selection of objects where the order does not matter. For example, if you have three elements A, B, and C, the combinations would include AB, AC, and BC.

The formula to calculate combinations of $n$items taken $r$at a time is:
$$C(n, r) = \frac{n!}{r!(n-r)!}$$

**Example with repeated elements:**
If you have items: Dairy Milk, Gems, Gems, and Eclairs. Each combination must be unique and the order does not matter.

### P-Value and Hypothesis Testing

#### P-Value

The p-value is a measure of the probability that an observed difference could have occurred just by random chance. For example, if the p-value is 0.05, there's a 5% chance that the observed difference is due to randomness.

#### Hypothesis Testing

Hypothesis testing is a method used to decide whether there is enough evidence to reject a null hypothesis, based on sample data.

1. **Null Hypothesis ($H_0$):** The default assumption (e.g., "the coin is fair").
2. **Alternative Hypothesis ($H_a$):** The opposite of the null hypothesis (e.g., "the coin is not fair").

**Steps:**

1. **Define the null and alternative hypotheses.**
2. **Perform the experiment and collect data.**
3. **Calculate the p-value or test statistic.**
4. **Compare the p-value to a significance level ($\alpha$).**
   - If $p \leq \alpha$, reject the null hypothesis.
   - If $p > \alpha$, do not reject the null hypothesis.

**Example: Testing a Fair Coin**

- Null Hypothesis $H_0$: The coin is fair ($\text{heads}) = 0.5$).
- Alternative Hypothesis $H_a$: The coin is not fair ($\text{heads}$) $\neq 0.5$\)).

1. **Conduct 100 coin tosses.**
2. **Calculate the observed number of heads.**
3. **Determine the mean and standard deviation for a fair coin.**
4. **Compute the confidence interval.**
   - Typically, for a significance level $\alpha = 0.05$, the confidence interval is 95%.
5. **Compare the observed result to the confidence interval:**
   - If the observed number of heads falls within the confidence interval, do not reject $H_0$.
   - If the observed number falls outside, reject $H_0$.

**Significance Level ($\alpha$) and Confidence Interval:**

- $\alpha = 0.05$: 95% confidence interval.
- $\alpha = 0.20$: 80% confidence interval.

#### Practical Example

**Assume:**

- Mean (expected number of heads in 100 tosses): 50
- Standard deviation: 10

If the observed number of heads is 30:

- **Check against the 95% confidence interval (mean ± 1.96 * std dev).**
- **30 is outside the 95% confidence interval (20, 80).**
- Therefore, reject $H_0$.

If the observed number of heads is 70:

- **70 is inside the 95% confidence interval (20, 80).**
- Therefore, do not reject $H_0$.

**Adjusting Significance Level:**

- With $\alpha = 0.20$, the 80% confidence interval is narrower.
- Observations falling outside this interval (e.g., 10 or 90 heads) would lead to rejecting $H_0$.

This approach helps determine whether observed data supports the null hypothesis or suggests an alternative.

**Probability Density Function (PDF)**—an important concept in statistics. We'll explore how it is created, its uses, and how it helps us in data analysis.

## Understanding Histograms

 In a histogram, the y-axis indicates how many points are present within each range. For example, if the range is between 70 to 80 weight, there may be five values present. Similarly, between 80 to 90, there could be ten values, and so on.

## From Histogram to Probability Density Function

Now, let's consider how we can convert this histogram into a Probability Density Function (PDF). Essentially, we smooth the histogram to create a curve, often resembling a bell curve—especially when dealing with a Gaussian distribution.

In a PDF, the y-axis no longer represents the count of values. Instead, it represents the **percentage of the distribution** within a specific range. For example, if the y-axis value is 0.1 at a particular point, it indicates that 10% of the distribution is present in that region.

### Key Points about PDF

- The y-axis represents the percentage of the distribution.
- The y-axis values range between 0 and 1 (0% to 100%).
- A PDF curve can tell us what portion of the distribution is within a specific range.

## Cumulative Density Function (CDF)

Now, let's explore the **Cumulative Density Function (CDF)**. In a CDF, the y-axis value represents the cumulative percentage of the distribution up to a certain point. For instance, if you add the y-values at different points, you generate a CDF curve.

### Key Points about CDF

- The y-axis represents the cumulative percentage of the distribution.
- The CDF curve starts at 0 and gradually increases to 1 as you move along the x-axis.
- The slope of the CDF curve becomes flatter as it approaches 1.

### Example Interpretation

Suppose at a point where weight is 130 kgs, the CDF value is 0.9. This indicates that 90% of the distribution in this dataset is less than 130 kgs, meaning the remaining 10% is greater than 130 kgs.

## Conclusion

In this video, we covered the concepts of **Probability Density Function (PDF)** and **Cumulative Density Function (CDF)**, and how they are used in exploratory data analysis.
