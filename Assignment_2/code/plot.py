import numpy as np
import matplotlib.pyplot as plt

n=11
pmf = np.full((n,), 1/8)
cdf = np.cumsum(pmf)
for i in range(8,n):
    cdf[i] = 1

plt.bar(np.arange(1, n+1)-0.15, pmf, color = 'b', width = 0.3, edgecolor = 'black', label='PMF')
plt.bar(np.arange(1, n+1)+0.15, cdf, color = 'g', width = 0.3, edgecolor = 'black', label='CDF')

plt.xlabel('Outcome', fontsize="45", labelpad=20)
plt.ylabel('Probability', fontsize="45", labelpad=20)
plt.xticks(fontsize=36)
plt.yticks(fontsize=36)
plt.ylim([0, 1.2])
plt.title('Probability Mass Function & Cumulative Distribution Function for the spinner', fontsize="45", pad=30)
plt.legend(fontsize="45")
plt.show()