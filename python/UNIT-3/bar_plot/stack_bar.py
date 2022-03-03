import numpy as np
import matplotlib.pyplot as plt

n = 5

menMeans = (20,35,30,35,27)
femaleMeans = (25,32,34,20,27)

ind = np.arange(n)

width = 0.35

fig = plt.figure()

ax = fig.add_axes([0.1,0.1,0.8,0.8])

ax.bar(ind,menMeans,width,color='r')
ax.bar(ind,femaleMeans,width,bottom=menMeans,color='b')

ax.set_ylabel('Scores')

ax.set_title("Score by the group and gender")
ax.set_xticks(ind,('G1', 'G2', 'G3', 'G4', 'G5'))
ax.set_yticks(np.arange(0,81,10))
ax.legend(labels=['man',"woman"])
plt.show()





