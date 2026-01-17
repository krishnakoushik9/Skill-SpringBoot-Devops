### **Week 1: Neural Network Initialization**
**Q1:** Why is it important to initialize weights randomly in a neural network, and what could go wrong if all weights were set to zero?
**A1:** Random initialization breaks symmetry, allowing neurons to learn different features. Zero initialization would cause all neurons to update identically, preventing effective learning.

**Q2:** How does the choice of weight initialization scale (e.g., `randn` vs `rand`) affect training dynamics?
**A2:** `randn` (Gaussian) allows for both positive/negative values, aiding gradient flow, while `rand` (uniform) may cause slower convergence due to asymmetric updates.

---

### **Week 2: Forward Propagation with Sigmoid**
**Q1:** Why is the sigmoid function used as an activation in hidden layers, and what are its limitations?
**A1:** Sigmoid squashes outputs to [0,1], useful for probabilities, but suffers from vanishing gradients for extreme inputs.

**Q2:** How does the weighted sum at the output layer differ from the hidden layer in a feedforward network?
**A2:** The output layer’s weighted sum is computed from hidden layer activations, while the hidden layer uses raw inputs.

---

### **Week 3: Multi-Layer Network Initialization**
**Q1:** Why is the architecture 5-3-2-3-1 chosen, and how does increasing hidden layers impact model capacity?
**A1:** Deeper layers capture hierarchical features, but excessive layers risk overfitting without sufficient data.

**Q2:** What role do biases play in a neural network, and why can’t we omit them?
**A2:** Biases shift activation functions, allowing the network to fit data not passing through the origin.

---

### **Week 4: Tanh Activation**
**Q1:** How does `tanh` differ from `sigmoid` in terms of output range and gradient behavior?
**A1:** `tanh` outputs [-1,1], centering data and mitigating vanishing gradients better than sigmoid’s [0,1].

**Q2:** Why are biases initialized to zero in this week’s code, and when might non-zero initialization help?
**A2:** Zero biases simplify initial symmetry-breaking, but non-zero values can help avoid dead neurons in deep networks.

---

### **Week 5: ReLU Activation**
**Q1:** What is the "dying ReLU" problem, and how can it be mitigated?
**A1:** Neurons stuck at zero due to negative inputs; leaky ReLU (small slope for x<0) prevents this.

**Q2:** Why is ReLU preferred over sigmoid/tanh in deep networks?
**A2:** ReLU avoids saturation, speeds up convergence, and reduces computational cost (no exponentials).

---

### **Week 6: CNN with K-Fold Cross-Validation**
**Q1:** Why is K-fold cross-validation used instead of a single train-test split?
**A1:** K-fold reduces variance in performance estimates by training/evaluating on multiple data subsets.

**Q2:** How does `MaxPooling2D` improve CNN performance, and what’s the trade-off?
**A2:** It reduces spatial dimensions, lowering computation and overfitting, but may lose fine-grained features.

---

### **Week 7: Feature Visualization & Confusion Matrix**
**Q1:** What does a confusion matrix reveal that accuracy alone cannot?
**A1:** It shows per-class errors (e.g., misclassifying 3s as 8s), highlighting specific model weaknesses.

**Q2:** Why visualize hidden layer activations in CNNs?
**A2:** It helps interpret what features (edges, textures) each layer detects, aiding debugging and design.

---

### **Week 8: 7-Layer CNN for Cats vs Dogs**
**Q1:** Why use `StratifiedKFold` instead of regular K-fold for imbalanced datasets?
**A1:** It preserves class distribution in each fold, ensuring minority classes are represented.

**Q2:** How does increasing CNN depth (e.g., 7 layers) impact feature extraction?
**A2:** Deeper layers capture complex hierarchies (edges → textures → object parts), but risk overfitting.

---

### **Week 9: AlexNet on MNIST**
**Q1:** Why is AlexNet, designed for ImageNet, adapted for MNIST despite its smaller images?
**A1:** It demonstrates transfer learning principles, though MNIST’s simplicity makes it overkill.

**Q2:** How does `GlobalAveragePooling2D` differ from `Flatten` in CNNs?
**A2:** GAP reduces parameters by averaging feature maps, while Flatten concatenates all values, risking overfitting.