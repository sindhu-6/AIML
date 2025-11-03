from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
import pandas as pd
import numpy as np


iris=datasets.load_iris()
x=pd.DataFrame(iris.data)
x.columns=['Sepal_length','Sepal_width','Petal_length','Petal_width']
print(x)


y=pd.DataFrame(iris.target)
y.columns=['targets']
print(y)


x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.1)
print("Dataset is split into training and testing")
print("Size of training data and its label",x_train.shape,y_train.shape)
print("Size of testing data and its label",x_test.shape,y_test.shape)


for i in range(len(iris.target_names)):
    print("label",i,".",str(iris.target_names[i]))


Classifier=KNeighborsClassifier(n_neighbors=3)
Classifier.fit(x_train,y_train)
y_pred=Classifier.predict(x_test)
print("Results of Classification using KNN with k=3")
for r in range (0,len(x_test)):
    print("sample:",str(x_test[r]),"Actual-label:",str(y_test[r]),"predict-label:",str(y_pred[r]))
print("Classification Accuracy:",Classifier.score(x_test,y_test))


from sklearn.metrics import  classification_report,confusion_matrix
print("confusion matrix")
print(confusion_matrix(y_test,y_pred))
print("Accuracy Ketrics")
print(classification_report(y_test,y_pred))
