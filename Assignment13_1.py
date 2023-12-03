
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

def AdvertisingPredictor():
    data = pd.read_csv("Advertising.csv")

    print("Size of the data is: ", data.shape)

    data.drop(["Sr.No"], axis=1, inplace=True)

    print(data.head())

    Features = ['TV', 'radio', 'newspaper']

    X = data[Features].values
    Y = data['sales'].values

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Create a Linear Regression model
    model = LinearRegression()

    # Fit the model to the training data
    model.fit(X_train, y_train)

    # Get the slope (coefficient) and intercept from the model
    m = model.coef_
    c = model.intercept_

    print("Slope of Regression line is: ", m)
    print("Y intercept of regression line is: ", c)

    # Predict sales using the model on the test set
    y_pred = model.predict(X_test)

    # Calculate the R-squared score
    r2 = r2_score(y_test, y_pred)

    print("R-squared:", r2)

    # Display the scatter plot and regression line for the training set
    x = np.arange(len(X_train))  # Create an array of data points for x

    # Predict sales using the model on the training set
    y_pred_train = model.predict(X_train)

    plt.plot(x, y_pred_train, color='#58b970', label='Regression Line')
    plt.scatter(x, y_train, color='#ef5423', label='Training Data')
    plt.xlabel('Data Point')
    plt.ylabel('Sales')
    plt.legend()
    plt.title('Linear Regression on Advertising Data (Training Set)')
    plt.show()

def main():
    print("Supervised Machine Learning")
    print("Linear Regression on dataset on Advertising Agency")
    AdvertisingPredictor()

if __name__ == "__main__":
    main()
