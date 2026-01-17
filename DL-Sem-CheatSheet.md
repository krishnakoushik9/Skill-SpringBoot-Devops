# Deep Learning Exam Checklist (Units I - V)

## Unit I: Basics & Feedforward Networks

_11A focuses on ML theory, while 11B focuses on the Neural Network architecture._

### 11 A: Machine Learning Foundations

- [x] **Capacity, Overfitting and Underfitting:** The "No Free Lunch" theorem and model complexity.

> [!NOTE] Capacity, Overfitting and Underfitting The balance between model complexity and generalization error, where overfitting memorizes data and underfitting fails to capture patterns.

- [x] **Hyperparameters and Validation Sets:** How to split data correctly.

> [!NOTE] Hyperparameters and Validation Sets Parameters set before training (e.g., learning rate) and the use of validation sets to tune them without overfitting.

- [x] **Estimators, Bias and Variance:** Understanding the trade-off.

> [!NOTE] Estimators, Bias and Variance Bias is error due to overly simplistic assumptions, variance is error due to excessive sensitivity to small fluctuations in the training set.

- [ ] **Maximum Likelihood Estimation (MLE):** The math behind how models learn.

> [!NOTE] Maximum Likelihood Estimation (MLE) A method to estimate model parameters by maximizing the likelihood of observing the given data.

- [x] **Stochastic Gradient Descent (SGD):** The basic optimization algorithm.

> [!NOTE] Stochastic Gradient Descent (SGD) An iterative method for optimizing an objective function by updating parameters using a random subset of data.

- [x] **Supervised vs Unsupervised Learning:** Definitions and examples.

> [!NOTE] Supervised vs Unsupervised Learning Supervised learning uses labeled data for prediction, while unsupervised learning finds patterns in unlabeled data.

### 11 B: Deep Feedforward Networks

- [x] **Learning XOR:** The classic problem that necessitated hidden layers.

> [!NOTE] Learning XOR A non-linear problem that cannot be solved by a single-layer perceptron, demonstrating the need for hidden layers.

- [x] **Gradient-Based Learning:** Cost functions and output units.

> [!NOTE] Gradient-Based Learning Training models by iteratively adjusting parameters in the direction of the negative gradient of the cost function.

- [x] **Hidden Units:** ReLU, Sigmoid, Tanh.

> [!NOTE] Hidden Units Activation functions (ReLU, Sigmoid, Tanh) introduce non-linearity to enable learning complex patterns.

- [x] **Architecture Design:** Width vs. Depth.

> [!NOTE] Architecture Design Width refers to the number of neurons per layer, depth refers to the number of layers in a network.

- [x] **Back-Propagation:** The core algorithm for calculating gradients.

> [!NOTE] Back-Propagation An efficient method to compute gradients of the loss function with respect to each weight using the chain rule.

- [x] **Differentiation Algorithms:** Forward vs. Backward mode.

> [!NOTE] Differentiation Algorithms Forward mode computes derivatives by propagating through the computational graph forward, backward mode does so backward.

---

## Unit II: Regularization & Optimization

_12A covers how to stop overfitting, 12B covers how to actually train the model._

### 12 A: Regularization Strategies

- [x] **Parameter Norm Penalties:** L1 and L2 Regularization (Weight Decay).

> [!NOTE] Parameter Norm Penalties L1 (Lasso) and L2 (Ridge) regularization penalize large weights to prevent overfitting.

- [x] **Dataset Augmentation:** Creating more data from existing data.

> [!NOTE] Dataset Augmentation Artificially expanding the training set by applying transformations (e.g., rotation, flipping) to existing data.

- [x] **Dropout:** Randomly disabling neurons (very important topic).

> [!NOTE] Dropout A regularization technique that randomly sets a fraction of input units to zero during training to prevent over-reliance on specific neurons.

- [x] **Early Stopping:** Stopping training when validation error rises.

> [!NOTE] Early Stopping Halting training when validation error starts increasing to avoid overfitting.

- [x] **Bagging and Ensemble Methods:** Combining models.

> [!NOTE] Bagging and Ensemble Methods Bagging (Bootstrap Aggregating) trains multiple models on different data subsets and combines their predictions.

- [x] **Noise Robustness & Semi-Supervised Learning:** Handling imperfect data.

> [!NOTE] Noise Robustness & Semi-Supervised Learning Techniques to improve model performance with noisy or partially labeled data.

### 12 B: Optimization for Training

- [x] **Parameter Initialization Strategies:** Xavier/He initialization (why we don't init to zero).

> [!NOTE] Parameter Initialization Strategies Xavier and He initialization scale initial weights based on the number of input/output units to avoid vanishing/exploding gradients.

- [x] **Adaptive Learning Rates:** Algorithms like Adam, RMSProp, Adagrad.

> [!NOTE] Adaptive Learning Rates Optimization algorithms that adjust the learning rate during training for each parameter (e.g., Adam, RMSProp).

- [x] **Challenges in Optimization:** Local Minima, Saddle Points, Cliffs.

> [!NOTE] Challenges in Optimization Local minima, saddle points, and cliffs are problematic regions in the loss landscape that can hinder optimization.

- [ ] **Batch Normalization:** (Often falls here under optimization strategies).

> [!NOTE] Batch Normalization Normalizing layer inputs to reduce internal covariate shift and accelerate training.

- [ ] **Basic Algorithms:** Momentum, Nesterov Momentum.

> [!NOTE] Basic Algorithms Momentum and Nesterov Momentum use past gradients to accelerate SGD in relevant directions.

---

## Unit III: Convolutional Networks (CNNs)

_13A covers the mechanism, 13B covers the variations._

### 13 A: CNN Fundamentals

- [x] **The Convolution Operation:** Kernel, Stride, Padding math.

> [!NOTE] The Convolution Operation Applying a filter (kernel) to input data to produce feature maps, with stride and padding controlling output size.

- [x] **Motivation:** Sparse interactions, Parameter sharing, Equivariant representations.

> [!NOTE] Motivation CNNs use sparse interactions and parameter sharing to reduce computational cost and achieve translation equivariance.

- [x] **Pooling:** Max Pooling vs. Average Pooling.

> [!NOTE] Pooling Downsampling operation (Max or Average) to reduce spatial dimensions and computational load.

- [x] **Convolution and Pooling as an Infinitely Strong Prior:** Theoretical concept.

> [!NOTE] Convolution and Pooling as an Infinitely Strong Prior Convolution and pooling encode strong assumptions about the structure of natural signals.

### 13 B: Variants & Efficiency

- [x] **Variants of the Basic Convolution Function:** Dilated convolution, Tiled convolution.

> [!NOTE] Variants of the Basic Convolution Function Dilated convolution expands the receptive field without increasing parameters, tiled convolution processes input in patches.

- [x] **Structured Outputs:** Predicting dense pixel maps.

> [!NOTE] Structured Outputs Models that predict structured outputs like pixel-wise labels (e.g., segmentation).

- [x] **Data Types:** 1D (Audio), 2D (Image), 3D (Video/Volumetric).

> [!NOTE] Data Types CNNs can process 1D (audio), 2D (images), and 3D (video/volumetric) data.

- [ ] **Efficient Convolution Algorithms:** Fourier transform approaches (FFT).

> [!NOTE] Efficient Convolution Algorithms Using FFT to speed up convolution operations by transforming them into the frequency domain.

- [x] **Random or Unsupervised Features:** Learning features without labels.

> [!NOTE] Random or Unsupervised Features Learning useful features from unlabeled data using techniques like autoencoders or random projections.

---

## Unit IV: Sequence Modeling (RNNs)

_14A covers the basic structure, 14B covers the solutions to memory problems._

### 14 A: Basic Recurrent Architectures

- [x] **Unfolding Computational Graphs:** Visualizing RNNs over time.

> [!NOTE] Unfolding Computational Graphs Representing RNNs as a sequence of identical operations over time steps.

- [x] **Recurrent Neural Networks (RNNs):** Standard architecture.

> [!NOTE] Recurrent Neural Networks (RNNs) Networks with loops to maintain a hidden state, enabling processing of sequential data.

- [x] **Bidirectional RNNs:** Looking at past and future context.

> [!NOTE] Bidirectional RNNs RNNs that process data in both forward and backward directions to capture full context.

- [x] **Encoder-Decoder Architectures:** Seq2Seq models (Translation).

> [!NOTE] Encoder-Decoder Architectures Models that encode input sequences into a fixed representation and decode it into an output sequence.

- [x] **Recursive Neural Networks:** Tree-structured networks.

> [!NOTE] Recursive Neural Networks Networks that operate on hierarchical tree structures, useful for parsing and NLP.

### 14 B: Advanced Gated RNNs & Long Term Dependencies

- [x] **The Challenge of Long-Term Dependencies:** Vanishing/Exploding gradients in time.

> [!NOTE] The Challenge of Long-Term Dependencies Difficulty in learning dependencies over long sequences due to vanishing or exploding gradients.

- [x] **Long Short-Term Memory (LSTM):** Forget, Input, and Output gates.

> [!NOTE] Long Short-Term Memory (LSTM) A gated RNN architecture designed to mitigate vanishing gradients and capture long-term dependencies.

- [x] **Gated Recurrent Units (GRUs):** Simplified LSTMs (often included here).

> [!NOTE] Gated Recurrent Units (GRUs) A simplified version of LSTM with fewer gates, designed for efficiency and similar performance.

- [x] **Echo State Networks:** Fixed reservoir weights.

> [!NOTE] Echo State Networks RNNs with a fixed, randomly initialized hidden layer and only output weights trained.

- [x] **Optimization for Long-Term Dependencies:** Clipping gradients.

> [!NOTE] Optimization for Long-Term Dependencies Techniques like gradient clipping to stabilize training and prevent exploding gradients.

---

## Unit V: Practical Methodology & Applications

### 15 A: Practical Methodology

- [x] **Performance Metrics:** Accuracy, Precision, Recall, F1 Score, ROC Curves.

> [!NOTE] Performance Metrics Metrics to evaluate model performance: accuracy, precision, recall, F1 score, and ROC curves.

- [x] **Default Baseline Models:** Establishing simple baselines (e.g., Logistic Regression) before deep learning.

> [!NOTE] Default Baseline Models Simple models (e.g., logistic regression) used as a performance baseline before applying complex models.

- [x] **Determining Whether to Gather More Data:** Analyzing Bias vs. Variance (Learning Curves).

> [!NOTE] Determining Whether to Gather More Data Using learning curves to diagnose if collecting more data will improve model performance.

- [ ] **Selecting Hyperparameters:** Manual selection, Grid Search, Random Search.

> [!NOTE] Selecting Hyperparameters Methods for tuning hyperparameters: manual, grid search, or random search.

- [x] **Debugging Strategies:** Handling Overfitting (Dropout/Regularization) and Underfitting.

> [!NOTE] Debugging Strategies Techniques to address overfitting (e.g., dropout, regularization) and underfitting (e.g., increasing model capacity).

- [ ] **Example: Multi-Digit Number Recognition:** Pipeline application (Localization -> Segmentation -> Recognition).

> [!NOTE] Example: Multi-Digit Number Recognition A pipeline for recognizing multi-digit numbers: localization, segmentation, and recognition.

### 15 B: Applications

- [x] **Applications: Large-Scale Deep Learning:** Distributed training, Model/Data Parallelism, GPU/TPU usage.

> [!NOTE] Applications: Large-Scale Deep Learning Techniques for scaling deep learning: distributed training, model/data parallelism, and hardware acceleration.

- [x] **Computer Vision:** Convolutional Neural Networks (CNNs), Object Detection, Image Classification.

> [!NOTE] Computer Vision CNNs for tasks like object detection and image classification in computer vision.

- [x] **Speech Recognition:** Acoustic modeling, sequence mapping (Audio to Text).

> [!NOTE] Speech Recognition Converting audio signals to text using acoustic models and sequence mapping.

- [x] **Natural Language Processing (NLP):** Word embeddings, RNNs, LSTMs, Transformers.

> [!NOTE] Natural Language Processing (NLP) Techniques for processing text: word embeddings, RNNs, LSTMs, and transformers.

- [ ] **Other Applications:** Recommender Systems, Reinforcement Learning (brief overview).

> [!NOTE] Other Applications Deep learning applications in recommender systems and reinforcement learning.

---