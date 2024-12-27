Here’s a detailed overview of the key metrics used during model training, including their formulas, ranges, and how they relate to model accuracy:

---

### 1. **Mean Absolute Error (MAE)**  

- **Formula**:  
  $
  \text{MAE} = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|
  $  
  Where:  
  - \$y_i$: Actual value  
  - \$\hat{y}_i$: Predicted value  
  - \$n$: Number of observations  

- **Range**: \$[0, \infty)$  
  A lower MAE indicates better accuracy.

- **Impact on Accuracy**:  
  MAE gives the average magnitude of errors without considering direction. It measures how far predictions are from actual values on average.

---

### 2. **Mean Squared Error (MSE)**  

- **Formula**:  
  $
  \text{MSE} = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2
  $

- **Range**: \$[0, \infty)$  
  A lower MSE signifies better model performance.

- **Impact on Accuracy**:  
  MSE penalizes larger errors more than smaller ones because errors are squared. Useful when large errors are particularly undesirable.

---

### 3. **Root Mean Squared Error (RMSE)**  

- **Formula**:  
  $
  \text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2}
  $

- **Range**: \$[0, \infty)$  
  A lower RMSE implies better model accuracy.

- **Impact on Accuracy**:  
  RMSE is similar to MSE but gives results in the same unit as the target variable. It is more sensitive to large errors than MAE.

---

### 4. **R-squared (\$R^2$) or Coefficient of Determination**  

- **Formula**:  
  $
  R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}
  $  
  Where:  
  - \$\bar{y}$: Mean of actual values  

- **Range**: \$(-\infty, 1]$  
  - \$R^2 = 1$: Perfect fit  
  - \$R^2 = 0$: Predictions are no better than the mean  
  - \$R^2 < 0$: Model performs worse than predicting the mean  

- **Impact on Accuracy**:  
  Indicates how well the model explains the variance in the target variable. Higher values indicate better fit.

---

### 5. **Accuracy (Classification Models)**  

- **Formula**:  
  $
  \text{Accuracy} = \frac{\text{Number of Correct Predictions}}{\text{Total Predictions}}
  $

- **Range**: \$[0, 1]$ or \$[0, 100\%]$  
  Higher accuracy indicates better model performance.

- **Impact on Accuracy**:  
  Measures the overall correctness of predictions but may not handle class imbalance well.

---

### 6. **Precision (Classification Models)**  

- **Formula**:  
  $
  \text{Precision} = \frac{\text{True Positives}}{\text{True Positives + False Positives}}
  $

- **Range**: \$[0, 1]$  
  Higher precision implies fewer false positives.

- **Impact on Accuracy**:  
  Useful in scenarios where false positives are costly (e.g., spam detection).

---

### 7. **Recall (Sensitivity, True Positive Rate)**  

- **Formula**:  
  $
  \text{Recall} = \frac{\text{True Positives}}{\text{True Positives + False Negatives}}
  $

- **Range**: \$[0, 1]$  
  Higher recall indicates fewer false negatives.

- **Impact on Accuracy**:  
  Useful in scenarios where missing a positive instance is costly (e.g., medical diagnoses).

---

### 8. **F1 Score**  

- **Formula**:  
  $
  F1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
  $

- **Range**: \$[0, 1]$  
  Higher F1 scores indicate a better balance between precision and recall.

- **Impact on Accuracy**:  
  Ideal when precision and recall need to be optimized simultaneously.

---

### 9. **Log Loss (Logarithmic Loss)**  

- **Formula**:  
  $
  \text{Log Loss} = -\frac{1}{n} \sum_{i=1}^n \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right]
  $

- **Range**: \$[0, \infty)$  
  Lower log loss indicates better probabilistic predictions.

- **Impact on Accuracy**:  
  Measures the uncertainty of predictions. Penalizes wrong predictions with high confidence more than less confident ones.

---

### 10. **Area Under the ROC Curve (AUC-ROC)**  

- **Formula**:  
  $
  AUC = \int_{\text{0}}^{\text{1}} \text{TPR (y-axis)} \, d\text{FPR (x-axis)}
  $  

- **Range**: \$[0, 1]$  
  - \$1.0$: Perfect classifier  
  - \$0.5$: Random guessing  
  - \$< 0.5$: Worse than random  

- **Impact on Accuracy**:  
  Evaluates the ability of the model to differentiate between classes across different thresholds.

---

### Summary of Metric-Accuracy Relationships

1. **Lower is better**: MAE, MSE, RMSE, Log Loss  
2. **Higher is better**: \$R^2$, Accuracy, Precision, Recall, F1 Score, AUC-ROC  
3. **Trade-offs**: Metrics like precision and recall often conflict, requiring a balance (e.g., F1 Score).  

Choosing the right metric depends on the problem type (classification or regression) and the domain-specific requirements (e.g., minimizing false positives or handling outliers).
