# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KaxVIXZGn7JT5PsFVYWMkpqecEeXZ1VC
"""

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

titanic_data=pd.read_csv('/content/drive/MyDrive/train (1).csv')

titanic_data.head()

titanic_data.describe()

sns.countplot(x='Survived',data=titanic_data)

titanic_data['Age'].plot.hist()

sns.countplot(x='Survived',hue='Sex',data=titanic_data, palette='winter')

sns.countplot(x='Survived',hue='Pclass', data=titanic_data,palette='PuBu')

titanic_data['Fare'].plot.hist(bins=20, figsize=(10,5))

sns.countplot(x='SibSp',data=titanic_data,palette='rocket')

sns.countplot(x='Parch',data=titanic_data, palette='winter')

"""**Check Missing Values**"""

titanic_data.info()

titanic_data.isnull().sum()

import seaborn as sns
sns.heatmap(titanic_data.isnull(),cmap='spring')

"""**Handle missing values**"""

corr_matrix=titanic_data.corr()

corr_matrix['Age'].abs()

sns.boxplot(x='Pclass',y='Age', data=titanic_data)

group_Pclass=titanic_data.groupby(['Sex','Pclass'])

group_Pclass.mean()

def input_age(cols):
  Age=cols[0]
  Pclass=cols[1]
  Sex=cols[2]

  if(pd.isnull(Age)):
    if(Pclass==1):
      if(Sex=='male'):
        return 41
      else:
        return 34
    elif(Pclass==2):
      if(Sex=='male'):
            return 30
      else:
           return 28
    else:
      if(Sex=='male'):
            return 26
      else:
           return 21
  else:
      return Age

titanic_data['Age']=titanic_data[['Age','Pclass','Sex']].apply(input_age,axis=1)

titanic_data.isnull().sum()

titanic_data.drop('Cabin',axis=1,inplace=True)

titanic_data.isnull().sum()

titanic_data[titanic_data['Embarked'].isnull()]

titanic_data.dropna(inplace=True)

titanic_data.isnull().sum()

titanic_data['Survived'].value_counts()

"""**Correlations**"""

titanic_data.drop(['PassengerId'],axis=1,inplace=True)

titanic_data.info()

cor_matrix=titanic_data.corr().abs()

cor_matrix

"""The highest correlation between features is **0.548193** in data set between **Fare** and **Pclass** .
Other also highly correlated.
More data sets are correlated higher than 0.1
"""

titanic_data.drop(['Name','Sex','Ticket','Embarked'],axis=1,inplace=True)

titanic_data.info()

x=titanic_data.drop('Survived',axis=1)
y=titanic_data['Survived']

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=4)

"""**Logistic Regression**"""

from sklearn.linear_model import LogisticRegression
lm=LogisticRegression()

lm.fit(x_train,y_train)

prediction=lm.predict(x_test)

from sklearn.metrics import classification_report

classification_report(y_test,prediction)

from sklearn.metrics import confusion_matrix

confusion_matrix(y_test,prediction)

from sklearn.metrics import accuracy_score

accuracy_score(y_test,prediction)

"""## Conclusion
I notice here that accuracy score is close to 70% which makes our model a good model to predict the values accurately , here in Titanic data set our model accurately predicts as to who will survive and who will not survive.

Through Visualization we found out that females have more chances of survival than males, class 1 have more changes of survival, youth age group 20-35 yrs male from class 3 have not survived.

Further, other Machine Learning Algorithms can be applied on the same data set, Ensemble algorithms to boost the performance of the model and get good predictions
"""