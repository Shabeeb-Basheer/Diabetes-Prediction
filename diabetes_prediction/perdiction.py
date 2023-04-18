import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv(r'E:\django\diabetes_prediction\static\diabetes.csv')
X = df.drop('Outcome', axis=1)
y = df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=66)

def random_forest(t1,t2,t3,t4,t5,t6,t7,t8):
    rfc = RandomForestClassifier()
    rfc.fit(X_train,y_train)
    lst=[[t1,t2,t3,t4,t5,t6,t7,t8]]
    lst=np.array(lst)
    lst.reshape(-1,1)

    rfc_predict = rfc.predict(lst)
    print(rfc_predict)
    ab = rfc.score(X_test, y_test)
    return str(rfc_predict[0]),ab
#     ls=pd.DataFrame(lst)

def mysvm(t1,t2,t3,t4,t5,t6,t7,t8):
    svclassifier = SVC(kernel='linear')
    svclassifier.fit(X_train, y_train)
    lst = [[t1,t2,t3,t4,t5,t6,t7,t8]]
    lst = np.array(lst)
    lst.reshape(-1, 1)
    presult = svclassifier.predict(lst)
    ab = svclassifier.score(X_test, y_test)
    return presult[0],ab



def decisiontree(t1,t2,t3,t4,t5,t6,t7,t8):
    dcclassifier = DecisionTreeClassifier()
    dcclassifier.fit(X_train,y_train)
    lst = [[t1,t2,t3,t4,t5,t6,t7,t8]]
    lst = np.array(lst)
    lst.reshape(-1,1)
    presult = dcclassifier.predict(lst)
    ab = dcclassifier.score(X_test,y_test)
    return presult[0],ab

def logistic_regression(t1,t2,t3,t4,t5,t6,t7,t8):
    classifier = LogisticRegression(random_state=0)
    classifier.fit(X_train, y_train)
    lst = [[t1, t2, t3, t4, t5, t6, t7, t8]]
    lst = np.array(lst)
    lst.reshape(-1, 1)
    presult = classifier.predict(lst)
    ab = classifier.score(X_test, y_test)
    return presult[0], ab



print(X)
print(y)

# print("Logistic Regression ",logistic_regression(1,85,66,29,0,26.6,0.351,31))