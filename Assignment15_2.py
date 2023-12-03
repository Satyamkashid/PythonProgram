import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
data = pd.read_csv("WinePredictor.csv")

# Visualizing the distribution of 'Class' using a histogram
plt.figure(figsize=(8, 6))
sns.histplot(data=data, x='Class', kde=True)
plt.title('Distribution of Class')
plt.xlabel('Class')
plt.ylabel('Frequency')
plt.show()

# Pairwise relationships between features
sns.pairplot(data, hue='Class', markers=["o", "s", "D"])
plt.title('Pairwise Relationships Between Features')
plt.show()

# Box plots to visualize the distribution of numerical features
numerical_features = ['Alcohol', 'Malic acid', 'Ash', 'Magnesium', 'Color intensity']
plt.figure(figsize=(10, 6))
sns.boxplot(data=data[numerical_features])
plt.title('Box Plot of Numerical Features')
plt.xlabel('Features')
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.show()
