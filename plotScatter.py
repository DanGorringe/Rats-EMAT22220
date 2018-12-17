import matplotlib.pyplot as plt
import pandas as pd

df  = pd.read_csv("data.csv")
values = df.values
nData = values[:,0]
primsData = values[:,1]
print(primsData)
otherData = values[:,2]
primsPlt = plt.scatter(nData,primsData,alpha=1,color='#66DDAA')
otherPlt = plt.scatter(nData,otherData,alpha=1,color='#FF6600')

plt.legend((primsPlt,otherPlt),('Prims','Other'))
plt.show()
