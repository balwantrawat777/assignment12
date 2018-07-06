"""
import pandas as pd
data={'name':['tom','jack','steven' ,'ricky'],'age':[28,23,45,32]}
df=pd.DataFrame(data)
print (df)

import pandas as pd
data={'name':['tom','jack','steven' ,'ricky'],'age':[28,23,45,32]}
df=pd.DataFrame(data,index=['rank1','rank2','rank3','rank4'])


import pandas as pd

df=pd.read_csv('sample.csv')
df=pd.DataFrame(data,index=['rank1','rank2','rank3','rank4'])
#print(df)
#print (df.axes)
#print (df.dtypes)
#print (df.T)
#print (df.shape)
#print (df.values)



import pandas as pd
import numpy as np
data=np.array(['a','b','c'])
s=pd.Series(data)
print(s)


df=pd.read_csv('sample.csv')
print(df)

