import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
data=pd.read_csv('cpdata.csv')
#print(data.head)

x=data.iloc[:,:-1].values
y=data.iloc[:,4:].values
Ly=LabelEncoder()
y=Ly.fit_transform(y)
mapped=Ly.classes_

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=20)

model=RandomForestClassifier(n_estimators=20,random_state=30)

model.fit(x_train,y_train)

pred=model.predict(x_test)

#print(pred)
from sklearn import metrics
print('Accuracy :',metrics.accuracy_score(y_test,pred))

def getPred(query):
    o=model.predict(query)
    print(o)
    return mapped[o][0]

print(getPred([[27.35152643,55.99375012,7.13411409,148.9812525]]))

'''
p=list(label.columns)
data.drop('label',axis=1,inplace=True)
X=data.iloc[:,0:4].values
y=data.iloc[:,4:].values
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
#print(x_test[0])
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
from sklearn.tree import DecisionTreeRegressor
model=DecisionTreeRegressor()
model.fit(x_train,y_train)
pred=model.predict(x_test)
from sklearn.metrics import accuracy_score
# Finding the accuracy of the model
a=accuracy_score(y_test,pred)
print("The accuracy of this model is: ", a*100)
l=[27.35152643,55.99375012,7.13411409,148.9812525]
predictcrop=[l]
predictions = model.predict(predictcrop)
print(predictions)
count=0

crops=['Black gram', 'Chickpea', 'Coconut', 'Coffee', 'Cotton', 'Ground Nut', 'Jute', 'Kidney ',
    'Beans', 'Lentil', 'Moth Beans', 'Mung Bean', 'Peas', 'Pigeon Peas', 'Rubber', 'Sugarcane',
    'Tea', 'Tobacco', 'apple', 'banana', 'grapes', 'maize', 'mango', 'millet', 'muskmelon', 'orange',
    'papaya', 'pomegranate', 'rice', 'watermelon', 'wheat']
cr='Adzuki Beans'

for i in range(0,30):
    if(predictions[0][i]==1):
        c=crops[i]
        count=count+1
        break
    i=i+1
if(count==0):
    print('The predicted crop is %s'%cr)
else:
    print('The predicted crop is %s'%c)'''