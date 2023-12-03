import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def MarvellousPlayPredictor(data_path):

    #Step 1 : Load Data
    data = pd.read_csv(data_path,index_col=0)

    print("Size of Actual dataset",len(data))

    # Step 2 : Clean , Prepare and manipulate data
    feature_names = ['Whether','Temperature']

    print("Names of Features : ",feature_names)

    whether = data.Whether
    Temperature = data.Temperature
    play = data.Play

    # Creating labelEncoder
    le = preprocessing.LabelEncoder() 

    # Converting string labels into numbers
    whether_encoded = le.fit_transform(whether)
    print(whether_encoded)

    # Converting string labels into numbers
    temp_encoded = le.fit_transform(Temperature)
    label = le.fit_transform(play)

    print(temp_encoded)

    # Combining whether and temperature into single list of tuples
    features = list(zip(whether_encoded,temp_encoded))

    # Step 3 : Train Data
    model = KNeighborsClassifier(n_neighbors=3)

    # Train the model using the training sets
    model.fit(features,label)

    # Test data
    predicted = model.predict([[0,2]])  # 0 : Overcast 2 : Mild
    print(predicted)

    if predicted:
        print("You can play")
    else:
        print("You cant play")

def CalculateAccuracyKNeighbor(data_path):
    data = pd.read_csv(data_path,index_col=0)

    whether = data.Whether
    Temperature = data.Temperature
    play = data.Play

    # Creating labelEncoder
    le = preprocessing.LabelEncoder() 

    # Converting string labels into numbers
    whether_encoded = le.fit_transform(whether)

    # Converting string labels into numbers
    temp_encoded = le.fit_transform(Temperature)
    label = le.fit_transform(play)

    # Combining whether and temperature into single list of tuples
    features = list(zip(whether_encoded,temp_encoded))

    features_train , features_test , play_train , play_test = train_test_split(features,label,test_size=0.5,random_state=42)
    
    classifier = KNeighborsClassifier()

    classifier.fit(features_train , play_train)

    predictions = classifier.predict(features_test )

    Accuracy = accuracy_score(play_test,predictions)

    return Accuracy

def main():
    print("------Marvellous InfoSystem by Piyush Khairnar------")

    print("Machine Learning Application")

    print("Play Predictor Application using K Nearest Knighbor Algorithm")

    MarvellousPlayPredictor("PlayPredictor.csv")

    Accuracy = CalculateAccuracyKNeighbor("PlayPredictor.csv")
    print("Accuracy of classification algorithm with K Neighbour classifier is : ",Accuracy*100,"%")


if __name__ == "__main__":
    main()
