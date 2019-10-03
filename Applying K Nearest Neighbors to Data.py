import pandas as pd
import numpy as np
from sklearn import preprocessing , neighbors
from sklearn.model_selection import train_test_split

df=pd.read_csv(r"C:\Users\Home\Desktop\New folder\breast-cancer-wisconsin.txt") 

df.replace('?',-99999,inplace=True)
df.drop(['id'],1,inplace=True)

X=np.array(df.drop(['class'],1))
y=np.array(df['class'])

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

clf=neighbors.KNeighborsClassifier()

clf.fit(X_train,y_train)

accuracy=clf.score(X_test,y_test)
print(accuracy)

example_measures = np.array([[4,2,1,1,1,2,3,2,1],[4,2,1,1,1,2,3,2,1]])
example_measures = example_measures.reshape(2,-1)

prediction= clf.predict(example_measures)

print(prediction)
