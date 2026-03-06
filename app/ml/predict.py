import numpy as np
import pickle

model = pickle.load(open("app/ml/model.pkl","rb"))

def predict_price(cost, demand):

    data = np.array([[cost, demand]])

    price = model.predict(data)[0]
    if price < 0:
        price = abs(price)

    return round(float(price),2)