![[Pasted image 20250716105952.png]]
![[Pasted image 20250716111210.png]]

### Below is the Code for the Week 1 code DL lab
```
import numpy as np
input_size = 2
hidden_size = 2
output_size = 1
Weight_input_hidden = np.random.rand(input_size,hidden_size)
bias_hidden = np.random.rand(1,hidden_size)

Weight_hidden_output = np.random.rand(hidden_size,output_size)
bias_output = np.random.rand(1,output_size)

#Print initialized weights
print("Weights connecting to Hidden layer")
print(Weight_input_hidden)

#Print Bias Sizes
print("Bias Size for hidden layers")
print(bias_hidden)

#Print hidden to output
print("Weight from hidden layer to Output")
print(Weight_hidden_output)

#Print bias size at output
print("Bias size from hidden to ouput")
print(bias_output)
```

