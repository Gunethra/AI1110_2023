import numpy as np
import matplotlib.pyplot as plt

n=11
pmf = np.full((n,), 1/8)
cdf = np.cumsum(pmf)
for i in range(8,n):
    cdf[i] = 1

fig, ax = plt.subplots()
ax.stem(np.arange(1, n+1), cdf)

ax.set_xlabel('Outcome', fontsize="45", labelpad=20)
ax.set_ylabel('CDF', fontsize="45", labelpad=20)

ax.set_xticks(np.arange(1, n+1))
ax.set_xticklabels(np.arange(1, n+1))

plt.xticks(fontsize=36)
plt.yticks(fontsize=36)

ax.set_ylim([0, 1.2])
plt.show()
