import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


df=quandl.get("WIKI/GOOGL")


df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]


df['HL_PCT']=(df['Adj. High']-df['Adj. Low'])/df['Adj. Close']*100.0
df['PCT_change']=(df['Adj. Close']-df['Adj. Open'])/df['Adj. Open']*100.0

df=df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

forecast_col=df['Adj. Close']
df.fillna(value=-99999, inplace=True)
forecast_out=int(math.ceil(0.01*len(df)))

print(forecast_out)

df['label']=forecast_col.shift(-forecast_out)

df.dropna(inplace=True)


X=np.array(df.drop(['label'],1))
X=preprocessing.scale(X)

y=np.array(df['label'])

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
clf=svm.SVR()

clf.fit(X_train, y_train)

confidence=clf.score(X_test,y_test)

print(confidence)
