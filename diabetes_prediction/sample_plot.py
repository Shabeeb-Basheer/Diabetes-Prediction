def cnn():
    # Visualize training history
    from keras.models import Sequential
    from keras.layers import Dense
    import matplotlib.pyplot as plt
    import pandas as pd

    from sklearn.model_selection import train_test_split

    import numpy
    # load pima indians dataset
    # dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
    # split into input (X) and output (Y) variables

    df = pd.read_csv(r'E:\django\diabetes_prediction\static\diabetes.csv')
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=66)

    # create model
    model = Sequential()
    model.add(Dense(12, input_dim=8, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # Fit the model
    history = model.fit(X, y, validation_split=0.33, epochs=150, batch_size=10, verbose=0)
    # list all data in history
    print(history.history.keys())
    # summarize history for accuracy
    print("CNN accuracy=====>",history.history['accuracy'][-1])

    # summarize history for loss
def xb_bst_fn():
    import xgboost as xgb
    import pandas as pd
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import train_test_split

    # Load data
    df = pd.read_csv(r'E:\django\diabetes_prediction\static\diabetes.csv')
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=66)

    # Create XGBoost model
    model = xgb.XGBClassifier(n_estimators=100, max_depth=3)

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f"xgboost Accuracy: {accuracy}")



import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


df = pd.read_csv(r'E:\django\diabetes_prediction\static\diabetes.csv')
X = df.drop('Outcome', axis=1)
y = df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=66)

def random_forest():
    rfc = RandomForestClassifier()
    rfc.fit(X_train,y_train)

    ab = rfc.score(X_test, y_test)
    print("RandomForestClassifier Accuracy",ab)
#     ls=pd.DataFrame(lst)

def mysvm():
    svclassifier = SVC(kernel='linear')
    svclassifier.fit(X_train, y_train)

    ab = svclassifier.score(X_test, y_test)
    print("SVM Accuracy",ab)



def decisiontree():
    dcclassifier = DecisionTreeClassifier()
    dcclassifier.fit(X_train,y_train)

    ab = dcclassifier.score(X_test,y_test)
    print("DecisionTreeClassifier Accuracy",ab)

def logistic_regression():
    classifier = LogisticRegression(random_state=0)
    classifier.fit(X_train, y_train)


    ab = classifier.score(X_test, y_test)
    print("LogisticRegression Accuracy",ab)


cnn()
xb_bst_fn()

random_forest()
mysvm()
decisiontree()
logistic_regression()