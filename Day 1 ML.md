## 🧠 Math Behind Scikit-learn (Supervised Learning)

Scikit-learn uses a mix of **linear algebra, calculus, probability, statistics, and optimization** to power its supervised learning algorithms.

---

### 1. Linear Regression

- Goal: Minimize **Mean Squared Error (MSE)**.
- Closed-form solution:

$$
\hat{\beta} = (X^T X)^{-1} X^T y
$$

- Solved using either the normal equation (closed-form) or **gradient descent** for large datasets.

---

### 2. Logistic Regression

- Uses the **sigmoid function**:

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

- Loss function (cross-entropy):

$$
L = -\sum_{i=1}^{n} \left[y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i)\right]
$$

- Solved via **gradient descent** or other optimization techniques.

---

### 3. Decision Trees

- Uses criteria like **Gini impurity** or **entropy** for splitting:

**Gini Impurity:**

$$
\text{Gini}(t) = 1 - \sum_{i=1}^{C} p_i^2
$$

**Entropy:**

$$
H(t) = -\sum_{i=1}^{C} p_i \log_2(p_i)
$$

---

### 4. Random Forests / Gradient Boosting

- **Random Forest**: Ensemble of decision trees + bagging.
- **Gradient Boosting**: Sequentially fits to residuals.

$$
F_{m}(x) = F_{m-1}(x) + h_m(x)
$$

---

### 5. Support Vector Machines (SVM)

- Optimization objective:

$$
\min_{w,b} \frac{1}{2} \|w\|^2 \quad \text{s.t. } y_i(w^T x_i + b) \geq 1
$$

- Kernel trick for nonlinear boundaries:

$$
K(x_i, x_j) = \phi(x_i)^T \phi(x_j)
$$

---

### 6. K-Nearest Neighbors (KNN)

- Based on **distance metric** (Euclidean distance):

$$
d(x, y) = \sqrt{\sum_{i=1}^{n}(x_i - y_i)^2}
$$

- No training; uses majority voting over `k` neighbors.

---

### 7. Naive Bayes

- Based on **Bayes' Theorem**:

$$
P(y|x) = \frac{P(x|y) P(y)}{P(x)}
$$

- Assumes **feature independence**:

$$
P(x_1, x_2, ..., x_n | y) = \prod_{i=1}^{n} P(x_i | y)
$$

---

### 📚 Libraries Under the Hood

- **NumPy** — for efficient linear algebra
- **SciPy** — for stats, distributions, optimization
- **liblinear / libsvm / XGBoost / LightGBM** — high-performance backends used under the hood

---
