import numpy as np
import matplotlib.pyplot as plt

pmf = np.full((n,), 1/8)
pmf[0]=0

fig, ax = plt.subplots()
ax.stem(np.arange(1, n+1), pmf)

ax.set_xlabel('Outcome', fontsize="45", labelpad=10)
ax.set_ylabel('PMF', fontsize="45", labelpad=20)
ax.set_xticks(np.arange(0, 9))
ax.set_xticklabels(np.arange(0, 9))
ax.set_ylim([0, 1.2])
plt.xticks(fontsize=36)
plt.yticks(fontsize=36)
plt.show()
