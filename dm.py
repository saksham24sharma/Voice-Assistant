import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl


test_df = pd.DataFrame(np.random.rand(30,5),index = np.arange(30))
x = test_df[1]
print(test_df.head(3))
y = pd.DataFrame(test_df,index=np.arange(1,2))
print(x)
print(y)

Y = y.drop([3,4],axis=1)
X = x.head(3)
print(X)
print(Y)
x1=list(X)
y1 = list(Y)

mpl.plot(x1,y1)
mpl.show()
