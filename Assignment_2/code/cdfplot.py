import numpy as np
import matplotlib.pyplot as plt

# Define the PMF of the spinner
pmf = np.full((8,), 1/8)

# Compute the CDF of the spinner
cdf = np.cumsum(pmf)

# Plot the CDF
plt.bar(np.arange(1, 9), cdf)
plt.title('Cumulative Distribution Function of Spinner')
plt.xlabel('Number')
plt.ylabel('PMF')
plt.xticks(np.arange(1, 9))
plt.ylim([0, 1.2])
plt.show()
