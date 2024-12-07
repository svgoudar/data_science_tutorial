### Ridge Regression Overview

**Ridge Regression** is a technique used to handle the problem of **overfitting** in linear regression by introducing a penalty term in the cost function. This penalty discourages the model from fitting the training data too perfectly, thereby improving its generalization on unseen test data.

---

### Revisiting Linear Regression Cost Function
The cost function for linear regression is:  
$
J(\theta) = \frac{1}{2m} \sum_{i=1}^m \left(h_\theta(x^{(i)}) - y^{(i)}\right)^2
$  
where:
- $ h_\theta(x^{(i)}) $: predicted value
- $ y^{(i)} $: actual value
- $ m $: number of training examples  

This cost function measures the **mean squared error (MSE)**. If the model overfits the data (e.g., achieves nearly 100% accuracy on training data), the test data error will likely increase, indicating poor generalization.

---

### Ridge Regression: L2 Regularization
In Ridge Regression, a penalty term proportional to the square of the model's coefficients ($\theta$) is added to the cost function. The modified cost function becomes:  

$
J(\theta) = \frac{1}{2m} \sum_{i=1}^m \left(h_\theta(x^{(i)}) - y^{(i)}\right)^2 + \lambda \sum_{j=1}^n \theta_j^2
$

Here:
1. $ \lambda $: **Regularization parameter** (hyperparameter that controls the strength of the penalty).
2. $ \sum_{j=1}^n \theta_j^2 $: Sum of squares of the coefficients (excluding $\theta_0$).

#### Why Add Regularization?
- The penalty term discourages large coefficient values, thereby reducing model complexity.
- Helps in scenarios where overfitting occurs due to collinearity or noise in the data.

---

### Effect of Ridge Regression
- **Overfitting Reduction**: By adding $\lambda$, the model avoids learning a perfect fit for the training data.
- **Bias-Variance Tradeoff**:  
  - **Low $\lambda$**: Model behaves like linear regression, with a higher risk of overfitting.
  - **High $\lambda$**: Adds stronger penalties, simplifying the model but potentially underfitting.
  
---

### Impact of $\lambda$ on Cost Function
- **When $\lambda = 0$**: Ridge regression reduces to standard linear regression.
- **When $\lambda > 0$**: Global minima shift, reducing coefficients $\theta_j$.
- Increasing $\lambda$ pushes the model to reduce the magnitude of $\theta_j$, effectively "shrinking" the coefficients.

---

### Visualizing the Effect
In a graph of cost function $J(\theta)$ vs. $\theta$:
- **$\lambda = 0$**: The global minima is at the original point of linear regression.
- **$\lambda > 0$**: The minima shifts, with $\theta_j$ decreasing in magnitude.
- As $\lambda$ increases, the model prioritizes simplicity, and coefficients $\theta_j$ shrink further.

---

### Key Takeaways
1. **Ridge Regression** adds a penalty to prevent overfitting by controlling the magnitude of coefficients.
2. **$\lambda$** is a hyperparameter, tuned to balance bias and variance.
3. **When $\lambda$ increases**, slope values ($\theta_j$) decrease, avoiding overly complex models.
4. It is most useful when dealing with multicollinearity or noisy datasets.

In the next videos, we’ll discuss **Lasso Regression** (L1 regularization), its ability to perform feature selection, and **Elastic Net**, which combines Ridge and Lasso.

### Ridge Regression (L2 Regularization)

Ridge Regression, also known as **L2 regularization**, is primarily used to address **overfitting**. Overfitting occurs when a model performs exceptionally well on training data but poorly on test data. 

#### Why Use Ridge Regression?
- **To reduce overfitting** by adding a penalty term to the cost function, which discourages large coefficients.
- Helps maintain all features in the model but with reduced impact of less important features by shrinking their coefficients closer to zero.

#### Cost Function:
The cost function for Ridge Regression is:
$
J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} \left( h_\theta(x^{(i)}) - y^{(i)} \right)^2 + \lambda \sum_{j=1}^{n} \theta_j^2
$
Where:
- $\lambda$: Regularization parameter. As $\lambda$ increases, the model penalizes large coefficients more aggressively.
- $\theta_j^2$: Sum of the squares of the coefficients (L2 norm).

---

### Lasso Regression (L1 Regularization)

Lasso Regression, also known as **L1 regularization**, is particularly useful for **feature selection**. It reduces the impact of less important features by driving their coefficients to zero.

#### Why Use Lasso Regression?
- **To perform feature selection** by eliminating less important features.
- Helps create simpler and more interpretable models by retaining only the most significant features.

#### Cost Function:
The cost function for Lasso Regression is:
$
J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} \left( h_\theta(x^{(i)}) - y^{(i)} \right)^2 + \lambda \sum_{j=1}^{n} |\theta_j|
$
Where:
- $|\theta_j|$: Sum of the absolute values of the coefficients (L1 norm).
  
#### Key Behavior:
- As $\lambda$ increases, coefficients of less important features shrink to zero, effectively removing those features from the model.

**Example**:  
For a hypothesis $ h_\theta(x) = \theta_0 + \theta_1x_1 + \theta_2x_2 + \theta_3x_3 + \theta_4x_4 $, if $\theta_4$ has a very small coefficient, Lasso Regression will likely shrink $\theta_4$ to zero, removing $x_4$ as an input feature.

---

### Elastic Net Regression

Elastic Net is a hybrid method that combines both Ridge (L2) and Lasso (L1) regularizations. 

#### Why Use Elastic Net?
- Simultaneously reduces overfitting (like Ridge) and performs feature selection (like Lasso).
- Useful when dealing with datasets containing highly correlated features or when there are many irrelevant features.

#### Cost Function:
The cost function for Elastic Net is:
$
J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} \left( h_\theta(x^{(i)}) - y^{(i)} \right)^2 + \lambda_1 \sum_{j=1}^{n} \theta_j^2 + \lambda_2 \sum_{j=1}^{n} |\theta_j|
$
Where:
- $\lambda_1$: Controls L2 regularization (Ridge).
- $\lambda_2$: Controls L1 regularization (Lasso).

---

### Key Differences and When to Use:
1. **Ridge Regression**:
   - Use when you want to reduce overfitting but retain all features.
   - Ideal when all features are moderately important.

2. **Lasso Regression**:
   - Use when you need feature selection in addition to reducing overfitting.
   - Effective in identifying and eliminating less relevant features.

3. **Elastic Net Regression**:
   - Use when you have datasets with many features, some of which are highly correlated or irrelevant.
   - Combines the strengths of Ridge and Lasso.

---

### Practical Insights:
- **Relationship Between $\lambda$ (or $\alpha$) and Coefficients**:
  - As $\lambda$ increases, the model penalizes the coefficients more.
  - For Lasso, coefficients may shrink to zero.
  - For Ridge, coefficients only shrink but never reach zero.

- **When to Use Each**:
  - **Ridge**: Training accuracy is high but test accuracy is low (overfitting).
  - **Lasso**: Many features, some of which are irrelevant.
  - **Elastic Net**: Overfitting with many features and multicollinearity.

By mastering Ridge, Lasso, and Elastic Net, you're essentially learning how to **hyperparameter tune linear regression** models effectively for different scenarios.