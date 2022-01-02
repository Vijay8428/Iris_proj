import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

def flower_prediction(sepal_length,sepal_width,petal_length,petal_width):

    df=pd.read_csv('iris.csv')

    X=df.drop('species',axis=1)
    y=df['species']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    scaler=StandardScaler()
    scaled_X_train=scaler.fit_transform(X_train)

    X_test=[[sepal_length,sepal_width,petal_length,petal_width]]

    scaled_X_test=scaler.transform(X_test)

    model=LogisticRegression()

    model.fit(scaled_X_train,y_train)

    
    

    return model.predict(scaled_X_test)[0]