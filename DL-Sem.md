# Deep Learning Exam Checklist (Units I - V)

## Unit I: Basics & Feedforward Networks
*11A focuses on ML theory, while 11B focuses on the Neural Network architecture.*

### 11 A: Machine Learning Foundations
- [ ] **Capacity, Overfitting and Underfitting:** The "No Free Lunch" theorem and model complexity.
- [ ] **Hyperparameters and Validation Sets:** How to split data correctly.
- [ ] **Estimators, Bias and Variance:** Understanding the trade-off.
- [ ] **Maximum Likelihood Estimation (MLE):** The math behind how models learn.
- [ ] **Stochastic Gradient Descent (SGD):** The basic optimization algorithm.
- [ ] **Supervised vs Unsupervised Learning:** Definitions and examples.

### 11 B: Deep Feedforward Networks
- [ ] **Learning XOR:** The classic problem that necessitated hidden layers.
- [ ] **Gradient-Based Learning:** Cost functions and output units.
- [ ] **Hidden Units:** ReLU, Sigmoid, Tanh.
- [ ] **Architecture Design:** Width vs. Depth.
- [ ] **Back-Propagation:** The core algorithm for calculating gradients.
- [ ] **Differentiation Algorithms:** Forward vs. Backward mode.

---

## Unit II: Regularization & Optimization
*12A covers how to stop overfitting, 12B covers how to actually train the model.*

### 12 A: Regularization Strategies
- [ ] **Parameter Norm Penalties:** L1 and L2 Regularization (Weight Decay).
- [ ] **Dataset Augmentation:** Creating more data from existing data.
- [ ] **Dropout:** Randomly disabling neurons (very important topic).
- [ ] **Early Stopping:** Stopping training when validation error rises.
- [ ] **Bagging and Ensemble Methods:** Combining models.
- [ ] **Noise Robustness & Semi-Supervised Learning:** Handling imperfect data.

### 12 B: Optimization for Training
- [ ] **Parameter Initialization Strategies:** Xavier/He initialization (why we don't init to zero).
- [ ] **Adaptive Learning Rates:** Algorithms like Adam, RMSProp, Adagrad.
- [ ] **Challenges in Optimization:** Local Minima, Saddle Points, Cliffs.
- [ ] **Batch Normalization:** (Often falls here under optimization strategies).
- [ ] **Basic Algorithms:** Momentum, Nesterov Momentum.

---

## Unit III: Convolutional Networks (CNNs)
*13A covers the mechanism, 13B covers the variations.*

### 13 A: CNN Fundamentals
- [ ] **The Convolution Operation:** Kernel, Stride, Padding math.
- [ ] **Motivation:** Sparse interactions, Parameter sharing, Equivariant representations.
- [ ] **Pooling:** Max Pooling vs. Average Pooling.
- [ ] **Convolution and Pooling as an Infinitely Strong Prior:** Theoretical concept.

### 13 B: Variants & Efficiency
- [ ] **Variants of the Basic Convolution Function:** Dilated convolution, Tiled convolution.
- [ ] **Structured Outputs:** Predicting dense pixel maps.
- [ ] **Data Types:** 1D (Audio), 2D (Image), 3D (Video/Volumetric).
- [ ] **Efficient Convolution Algorithms:** Fourier transform approaches (FFT).
- [ ] **Random or Unsupervised Features:** Learning features without labels.

---

## Unit IV: Sequence Modeling (RNNs)
*14A covers the basic structure, 14B covers the solutions to memory problems.*

### 14 A: Basic Recurrent Architectures
- [ ] **Unfolding Computational Graphs:** Visualizing RNNs over time.
- [ ] **Recurrent Neural Networks (RNNs):** Standard architecture.
- [ ] **Bidirectional RNNs:** Looking at past and future context.
- [ ] **Encoder-Decoder Architectures:** Seq2Seq models (Translation).
- [ ] **Recursive Neural Networks:** Tree-structured networks.

### 14 B: Advanced Gated RNNs & Long Term Dependencies
- [ ] **The Challenge of Long-Term Dependencies:** Vanishing/Exploding gradients in time.
- [ ] **Long Short-Term Memory (LSTM):** Forget, Input, and Output gates.
- [ ] **Gated Recurrent Units (GRUs):** Simplified LSTMs (often included here).
- [ ] **Echo State Networks:** Fixed reservoir weights.
- [ ] **Optimization for Long-Term Dependencies:** Clipping gradients.
---
# Unit V Exam Checklist

## 15 A: Practical Methodology
- [ ] **Performance Metrics:** Accuracy, Precision, Recall, F1 Score, ROC Curves.
- [ ] **Default Baseline Models:** Establishing simple baselines (e.g., Logistic Regression) before deep learning.
- [ ] **Determining Whether to Gather More Data:** Analyzing Bias vs. Variance (Learning Curves).
- [ ] **Selecting Hyperparameters:** Manual selection, Grid Search, Random Search.
- [ ] **Debugging Strategies:** Handling Overfitting (Dropout/Regularization) and Underfitting.
- [ ] **Example: Multi-Digit Number Recognition:** Pipeline application (Localization -> Segmentation -> Recognition).

## 15 B: Applications
- [ ] **Applications: Large-Scale Deep Learning:** Distributed training, Model/Data Parallelism, GPU/TPU usage.
- [ ] **Computer Vision:** Convolutional Neural Networks (CNNs), Object Detection, Image Classification.
- [ ] **Speech Recognition:** Acoustic modeling, sequence mapping (Audio to Text).
- [ ] **Natural Language Processing (NLP):** Word embeddings, RNNs, LSTMs, Transformers.
- [ ] **Other Applications:** Recommender Systems, Reinforcement Learning (brief overview).


---
