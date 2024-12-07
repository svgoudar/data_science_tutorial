In our previous video, we discussed the mathematical intuition behind **linear regression** and **multiple linear regression** models. Now, we will explore some of the **performance metrics** that help determine how well a model fits a given dataset. The two key metrics we'll focus on today are **R-squared** and **Adjusted R-squared**.

### Understanding R-squared (Coefficient of Determination)

Let's begin with **R-squared**, often denoted as $R^2$. This metric gives us an idea of how well our regression model explains the variability of the target variable (dependent variable).

#### Formula for R-squared

$R^2 = 1 - \frac{\text{SS}_{\text{residual}}}{\text{SS}_{\text{total}}}$

Where:

- **$SS_{\text{residual}}$** (Sum of Squares of Residuals): Measures the total squared difference between the actual values ($y_i$) and the predicted values ($\hat{y}_i$) from the model.
  
  $\text{SS}_{\text{residual}} = \sum (y_i - \hat{y}_i)^2$
- **$SS_{\text{total}}$** (Total Sum of Squares): Measures the total squared difference between the actual values ($y_i$) and the mean of the actual values ($\bar{y}$).
  
  $\text{SS}_{\text{total}} = \sum (y_i - \bar{y})^2$

#### Intuition Behind R-squared

- $R^2$ is a measure of how much of the total variation in the dependent variable can be explained by the independent variables in the model.
- The value of $R^2$ ranges between **0 and 1**:
  - An $R^2$ value of **1** indicates that the regression model perfectly fits the data, explaining 100% of the variability.
  - An $R^2$ value of **0** means the model does not explain any of the variability in the target variable.

##### Visual Example

- Imagine we have data points plotted on a graph with $x$ as the independent variable and $y$ as the dependent variable.
- We draw a **best-fit line** through the data points using linear regression.
- The difference between each actual data point ($y_i$) and its corresponding point on the best-fit line ($\hat{y}_i$) is the **residual**.
- $SS_{\text{residual}}$ captures how far off our predictions are from the actual values.
- $SS_{\text{total}}$ captures how spread out the actual data is from the mean ($\bar{y}$).

##### Interpreting R-squared

- If $R^2 = 0.85$, it means **85% of the variance** in the dependent variable is explained by the independent variables in your model.
- A higher $R^2$ indicates a better fit, but there is a catch: $R^2$ **always increases** as you add more variables to the model, which can sometimes lead to overfitting.

---

### Understanding Adjusted R-squared

To address the limitation of $R^2$ increasing with additional features, we use **Adjusted R-squared**. This metric adjusts the $R^2$ value based on the number of predictors in the model and the size of the dataset.

#### Formula for Adjusted R-squared

$\text{Adjusted } R^2 = 1 - \left( \frac{\text{SS}_{\text{residual}} / (n - p - 1)}{\text{SS}_{\text{total}} / (n - 1)} \right)$

Where:

- $n$ is the number of observations (data points).
- $p$ is the number of independent variables (features).

#### Intuition Behind Adjusted R-squared

- **Adjusted R-squared** penalizes the addition of variables that do not improve the model significantly.
- It accounts for the **complexity** of the model by considering the number of features relative to the number of observations.
- If you add a feature that does not contribute to explaining the variance, **Adjusted $R^2$** will decrease, unlike $R^2$, which would still increase.

##### Example Scenario

- Let's say we're building a model to predict **house prices** based on features like **size of the house**, **number of bedrooms**, and **location**.
  - **Size of the house** and **number of bedrooms** are positively correlated with the price, so adding them improves the model.
  - However, if we add a feature like **gender of the homeowner**, which has no correlation with the house price, the $R^2$ might still increase slightly due to the formula, but the **Adjusted $R^2$** will penalize this unnecessary complexity.
  
##### Key Differences Between R-squared and Adjusted R-squared

- **$R^2$**:
  - Increases with the addition of new features, regardless of their relevance.
  - Does not consider the number of predictors.
- **Adjusted $R^2$**:
  - Adjusts for the number of features, rewarding models that improve fit and penalizing those that add complexity without value.
  - Preferred when comparing models with different numbers of predictors.

---

### Conclusion

- Use **$R^2$** to understand the basic fit of your model.
- Use **Adjusted $R^2$** when you want a more accurate measure that accounts for the number of predictors, especially in **multiple regression** scenarios.
- In our next session, we'll discuss concepts like **overfitting** and **underfitting**, and how to use **train-test-validation splits** to evaluate model performance effectively.
