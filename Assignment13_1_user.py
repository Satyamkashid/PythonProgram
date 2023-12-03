# Code has some error

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def AdvertisingPredictor():
    data = pd.read_csv("Advertising.csv")

    print("Size of the data is : ",data.shape)

    data.drop(["Sr.No"],axis=1,inplace=True)

    print(data.head())

    Features = ['TV','radio','newspaper']

    X = data[Features].values
    Y = data['sales'].values

    # Least Square method
    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    n = len(X)

    numerator = 0
    denomenotor = 0

    for i in range(n):
        numerator += (X[i] - mean_x) * (Y[i] - mean_y)
        denomenotor += (X[i] -mean_x) ** 2

    m = numerator / denomenotor
    c = mean_y - (m * mean_x)

    print("Slope of Regression line is : ",m)
    print("Y intercept of regression line is : ",c)

    max_x = np.max(X) + 100
    min_x = np.min(X) - 100

    # Display plotting of above points
    x = np.linspace(min_x, max_x, n)

    y = c + m * x

    plt.plot(x,y,color = '#58b970',label = 'Regression Line')

    plt.scatter(X,Y,color = '#ef5423',label = 'scatter plot')

    plt.xlabel('Advertising Channels')

    plt.ylabel('Sales')

    plt.legend()
    plt.title('Linear Regression on Advertising Data')
    plt.show()

    # Goodness of fit

    ss_t = 0
    ss_r = 0

    for i in range(n):
        y_pred = c + m * X[i]
        ss_t += (Y[i] - mean_y) ** 2
        ss_r += (Y[i] - y_pred) ** 2

    r2 = 1-(ss_r / ss_t)
    print("Goodness of fit is %s"%r2)


def main():
    print("Supervised Machine Learning")

    print("Linear Regression on data set on Advertising Agency")

    AdvertisingPredictor()

if __name__ == "__main__":
    main()


