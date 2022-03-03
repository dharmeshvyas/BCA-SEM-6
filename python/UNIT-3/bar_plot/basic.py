import matplotlib.pylab as plt

fig =  plt.figure()

ax= fig.add_axes([0.1,0.1,0.9,0.9])
langs = ['C','C++','Java','Python','PHP']
student = [23,17,35,29,12]
ax.bar(langs,student)
plt.show()