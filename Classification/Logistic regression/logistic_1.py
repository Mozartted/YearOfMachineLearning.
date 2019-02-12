# Logistic regression - classification.
import pandas as pd

df = pd.read_csv('./dataset/iris/iris.csv') ## Load data
df = df.drop(['Id'],axis=1)
rows = list(range(100,150))
df = df.drop(df.index[rows])  ## Drop the rows with target values Iris-virginica
Y = []
target = df['Species']
for val in target:
    if(val == 'Iris-setosa'):
        Y.append(0)
    else:
        Y.append(1)
df = df.drop(['Species'],axis=1)
X = df.values.tolist()