import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)

def black_box_function(x):
    y = np.sin(x) + np.cos(2*x)
    return y

# range of x values
x_range = np.linspace(-2*np.pi, 2*np.pi, 100)

# output for each x value
black_box_output = black_box_function(x_range)

# plot
# plt.plot(x_range, black_box_output)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Black Box Function Output')
# plt.show()

# random x values for sampling
num_samples = 10
sample_x = np.random.choice(x_range, size=num_samples)

# output for each sampled x value
sample_y = black_box_function(sample_x)

# plot
plt.plot(x_range, black_box_function(x_range), label='Black Box Function')
plt.scatter(sample_x, sample_y, color='red', label='Samples')
plt.xlabel('x')
plt.ylabel('Black Box Output')
plt.title('Sampled Points')
plt.legend()
plt.show()