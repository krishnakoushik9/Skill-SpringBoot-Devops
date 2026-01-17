# K-Nearest Neighbors (KNN) – Mathematical Explanation

KNN is a **non-parametric**, **instance-based** learning algorithm used for **classification** and **regression**. It predicts the output of a test sample based on the **k training samples closest to it**.

---

## Step-by-Step Math

### 1. Input

- Training data:
  $$
  X = \{x_1, x_2, \dots, x_n\}, \quad Y = \{y_1, y_2, \dots, y_n\}
  $$
- Test data point:  
  $$
  x_{\text{test}}
  $$

---

### 2. Distance Calculation

Compute the distance between the test point and all training points.  
**Euclidean Distance** is most commonly used:

$$
d(x_i, x_{\text{test}}) = \sqrt{\sum_{j=1}^{m} (x_{ij} - x_{\text{test},j})^2}
$$

Where:
- \( m \) is the number of features
- \( x_{ij} \) is the \( j^{th} \) feature of \( x_i \)

---

### 3. Select K Nearest Neighbors

Sort the distances and choose the \( k \) nearest neighbors based on the smallest distances.

---

### 4. Prediction (Classification)

Use **majority voting** among the labels of the \( k \) nearest neighbors:

$$
\hat{y} = \text{mode}(y_{(1)}, y_{(2)}, \dots, y_{(k)})
$$

Where \( y_{(i)} \) is the label of the \( i^{th} \) closest neighbor.

---

### 5. Prediction (Regression)

Take the **mean** of the target values of the \( k \) nearest neighbors:

$$
\hat{y} = \frac{1}{k} \sum_{i=1}^{k} y_{(i)}
$$

---

## Notes

- Distance metrics can also be:
  - **Manhattan**:
    $$
    d(x_i, x_{\text{test}}) = \sum_{j=1}^{m} |x_{ij} - x_{\text{test},j}|
    $$
  - **Minkowski**:
    $$
    d(x_i, x_{\text{test}}) = \left( \sum_{j=1}^{m} |x_{ij} - x_{\text{test},j}|^p \right)^{1/p}
    $$

- Feature **scaling** is crucial (use normalization or standardization).

- High-dimensional data may degrade performance due to the **curse of dimensionality**.

