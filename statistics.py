import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
df = pd.DataFrame(np.c_[cancer['data'], cancer['target']],
                  columns=np.append(cancer['feature_names'], ['target']))
df = df[['mean radius', 'mean texture', 'target']]
df['radius'] = (df['mean radius']>df['mean radius'].mean())*1
df['texture'] = (df['mean texture']>df['mean texture'].mean())*1
df = df.iloc[:, [2, 3, 4]]
df['target'].sum()

print(df.head())

df2 = df.groupby(['radius', 'texture'], as_index=False).agg('sum')
print(df2)

a = df2[df2['radius']==0]['target'].sum()
b = df['target'].sum()
print(a/b)

a = df2[(df2['radius']==0) & (df2['texture']==1)]['target'].sum()
b = df['target'].sum()
print(a/b)
