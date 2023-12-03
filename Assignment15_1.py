import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def WinePredictor(data_path):
    # Step 1 : Load the data
    data = pd.read_csv(data_path)
    print("Size of the actual dataset is %s"%len(data))

    # Step 2 : Clean , prepare and Manipulate data
    feature_name = ['Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue','OD280/OD315 of diluted wines','Proline']
    print("Name of Features \n",feature_name)

    Alcohol = data['Alcohol']
    Malic_acid = data['Malic acid']
    Ash = data['Ash']
    Alcalinity_of_ash = data['Alcalinity of ash']
    Magnesium = data['Magnesium']
    Total_phenols = data['Total phenols']
    Flavanoids = data['Flavanoids']
    Nonflavanoid_phenols = data['Nonflavanoid phenols']
    Proanthocyanins = data['Proanthocyanins']
    Color_intensity = data['Color intensity']
    Hue = data['Hue']
    OD280_OD315_of_diluted_wines = data['OD280/OD315 of diluted wines']
    Proline = data['Proline']
    Wine = data['Class']

    # Combining whether and temperature into single list of tuples
    features = list(zip(Alcohol,Malic_acid,Ash,Alcalinity_of_ash,Magnesium,Total_phenols,Flavanoids,Nonflavanoid_phenols,Proanthocyanins,Color_intensity,Hue,OD280_OD315_of_diluted_wines,Proline,Wine))

    # Step 3 : Train Data
    model = KNeighborsClassifier(n_neighbors=3)

    features_train , features_test , wine_train , wine_test = train_test_split(features,Wine,test_size=0.5)

    model.fit(features_train , wine_train)

    predictions = model.predict(features_test )
    print("Prediction is : ",predictions)



def CalculateAccuracyKNeighbor(data_path):
    data = pd.read_csv(data_path,index_col=0)

    Alcohol = data['Alcohol']
    Malic_acid = data['Malic acid']
    Ash = data['Ash']
    Alcalinity_of_ash = data['Alcalinity of ash']
    Magnesium = data['Magnesium']
    Total_phenols = data['Total phenols']
    Flavanoids = data['Flavanoids']
    Nonflavanoid_phenols = data['Nonflavanoid phenols']
    Proanthocyanins = data['Proanthocyanins']
    Color_intensity = data['Color intensity']
    Hue = data['Hue']
    OD280_OD315_of_diluted_wines = data['OD280/OD315 of diluted wines']
    Proline = data['Proline']
    Wine = data['Class']

    

    # Combining whether and temperature into single list of tuples
    features = list(zip(Alcohol,Malic_acid,Ash,Alcalinity_of_ash,Magnesium,Total_phenols,Flavanoids,Nonflavanoid_phenols,Proanthocyanins,Color_intensity,Hue,OD280_OD315_of_diluted_wines,Proline,Wine))


    features_train , features_test , wine_train , wine_test = train_test_split(features,Wine,test_size=0.5)
    
    classifier = KNeighborsClassifier()

    classifier.fit(features_train , wine_train)

    predictions = classifier.predict(features_test )

    Accuracy = accuracy_score(wine_test,predictions)

    return Accuracy


def main():
    print("----------Machine Learning Application-------------")

    print("Wine Predictor Application using K Nearest Knighbor Algorithm")

    WinePredictor("WinePredictor.csv")

    Accuracy = CalculateAccuracyKNeighbor("WinePredictor.csv")
    print("Accuracy of classification algorithm with K Neighbour classifier is : ",Accuracy*100,"%")

if __name__ == "__main__":
    main()