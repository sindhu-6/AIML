#IMPORTING THE LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#IMPORTING THE DATASET
dataset=pd.read_csv('C:/Users/student/Desktop/salary_Data.csv')
print(dataset)

#DATA PREPROCESSING
x=dataset.iloc[:,:-1].values #INDEPENDENT VARIABLE ARRAY
y=dataset.iloc[:,1].values #DEPENDENT VARIABLE ARRAY

#SPLITTING THE DATASET INTO THE TRAINING SET AND TEST SET
from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test=train_test_split(x,y,test_size=1/3,random_state=0)

#FITTING THE REGRESSION MODEL 
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train) #ACTUALLY PRODUCES THE LINEAR EQN FOR THE DATA

#PREDICTING THE TEST SET RESULTS
y_pred=regressor.predict(x_test)
print(x_test)
y_test

#VISUALIZING THE RESULTS
#PLOT FOR THE TRAIN
plt.scatter(x_train,y_train,color="red")#plotting the observation line
plt.plot(x_train,regressor.predict(x_train),color="blue") 
plt.title("Salary vs Experience (Training Set)") #stating the title of the graph
plt.xlabel("Years of experience") #adding the name of x-axis
plt.ylabel("Salaries") #adding the name of y-axis
plt.show() #specifies the end of graph

#VISUALIZING THE RESULTS
#PLOT FOR THE TEST
plt.scatter(x_test,y_test,color="red")#plotting the observation line
plt.plot(x_train,regressor.predict(x_train),color="blue") 
plt.title("Salary vs Experience (Training Set)") #stating the title of the graph
plt.xlabel("Years of experience") #adding the name of x-axis
plt.ylabel("Salaries") #adding the name of y-axis
plt.show() #specifies the end of graph
