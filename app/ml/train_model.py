import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data={
"cost":[10,20,30,40],
"demand":[100,90,80,70],
"price":[15,30,45,60]
}

df=pd.DataFrame(data)

X=df[["cost","demand"]]
y=df["price"]

model=LinearRegression()

model.fit(X,y)

pickle.dump(model,open("app/ml/model.pkl","wb"))