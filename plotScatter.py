import matplotlib.pyplot as plt
import pandas as pd

df  = pd.read_csv("data.csv")
values = df.values
nData = values[:,0]
primsData = values[:,1]
otherData = values[:,2]
kruskalsData = values[:,3]

primsPlt = plt.scatter(nData,primsData,alpha=1,color='#66DDAA')
otherPlt = plt.scatter(nData,otherData,alpha=1,color='#FF6600')
kruskalsPlt = plt.scatter(nData,kruskalsData,alpha=1,color='#FFAADD')

plt.legend((primsPlt,otherPlt,kruskalsPlt),('Prims','Other','Kruskals'))
plt.show()
