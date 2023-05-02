import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
import matplotlib.pyplot as plt
import numpy

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

    # Visualize training history
    from keras.models import Sequential
    from keras.layers import Dense
    import matplotlib.pyplot as plt
    import numpy
    # load pima indians dataset
    # dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
    # split into input (X) and output (Y) variables
    import speechData1
    X, Y = speechData1.loadDataSet()
    # create model
    model = Sequential()
    model.add(Dense(12, input_dim=8, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # Fit the model
    history = model.fit(X, Y, validation_split=0.33, epochs=150, batch_size=10, verbose=0)
    # list all data in history
    print(history.history.keys())
    # summarize history for accuracy
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()
    # summarize history for loss
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()
    # print("Logistic Regression ",cnn(1,85,66,29,0,26.6,0.351,31))

print(X)
print(y)

