import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def WinePredictor(data_path):
    # Step 1 : Load the data
    data = pd.read_csv(data_path)
    print("Size of the actual dataset is %s"%len(data))
    print(data)

    # Step 2 : Clean , prepare and Manipulate data
    feature_name = ['Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue','OD280/OD315 of diluted wines','Proline']
    print("Name of Features \n",feature_name)

    X = data[feature_name].values  # Extracting feature columns as a NumPy array
    Y = data['Class'].values  # Assuming 'Wine' is the column name for labels

    # Normalize the features using StandardScaler
    scaler = StandardScaler()
    X = scaler.fit_transform(X)    

    features_train , features_test , wine_train , wine_test = train_test_split(X,Y,test_size=0.3,random_state=42)

    # Step 3 : Train Data
    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(features_train , wine_train)

    predictions = model.predict(features_test )
    print("Prediction is : \n",predictions)


    Accuracy = accuracy_score(wine_test,predictions)

    print(f'Accuracy: {Accuracy * 100:.2f}%')


def main():
    print("----------Machine Learning Application-------------")

    print("Wine Predictor Application using K Nearest Knighbor Algorithm")

    WinePredictor("WinePredictor.csv")



if __name__ == "__main__":
    main()