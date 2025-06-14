# -*- coding: utf-8 -*-
"""DAY-8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Hi_aBCM0mIT13b_4baybPZMnXReqijqn
"""

import numpy as np        # For numerical operations and arrays
import pandas as pd         # For data loading, manipulation, and analysis
import matplotlib.pyplot as  plt # for data visualzing
import seaborn as sns        # For advanced data visualization with better styling

data=pd.read_csv("/content/Credit Card Customer Data.csv") # Import dataset
data # display the data

data.info() # Show basic information about the dataset

data.describe() # Show descriptive statistics

# Visualize the dataset using a scatter plot
plt.scatter(data['Sl_No'],data['Avg_Credit_Limit'],color="orange")
plt.xlabel('Sl_No')
plt.ylabel('average credit card limit')
plt.show()

sns.heatmap(data.corr()) # Show heatmap of correlation matrix

sns.pairplot(data) # Visualize pairwise relationships in the dataset

x=data[['Sl_No','Avg_Credit_Limit','Total_Credit_Cards']] # Select features for clustering
x.head()  # displaying top 5 x features data

x.shape # Check the shape of feature matrix

# Elbow Method to determine optimal number of clusters
wcss = []  # List to store Within-Cluster Sum of Squares for each value of K

# Loop through different values of K (from 1 to 10)
for i in range(1, 11):
    # Initialize KMeans with i clusters
    kmeans = KMeans(n_clusters=i, n_init='auto', init='k-means++', algorithm='lloyd')
    kmeans.fit(x)  # Fit the model to the data
    wcss.append(kmeans.inertia_)  # Append WCSS (inertia) to the list

# Plot the Elbow Graph
plt.figure(figsize=(6, 4))  # Set figure size
plt.plot(range(1, 11), wcss, marker='o')  # Plot WCSS values for each K
plt.xlabel('Number of clusters')  # Label for X-axis
plt.ylabel('WCSS')  # Label for Y-axis
plt.title('Elbow Method For Optimal K')  # Title of the plot
plt.grid(True)  # Display grid
plt.show()  # Show the plot

from sklearn.cluster import KMeans # Import KMeans from sklearn

# Initialize the KMeans model with 5 clusters
model=KMeans(n_clusters=5,n_init='auto',init='k-means++',algorithm='lloyd')

model.fit(x) # Fit the model to the data

output=model.predict([[12,6000,3]])
# Predict the cluster for a new data point [12,6000,3]

output # giving the output as which cluster it is belongs to

from sklearn.metrics import silhouette_score  # Import function to evaluate clustering quality using Silhouette Score

# Silhouette Score
labels = model.labels_
sil_score = silhouette_score(x, labels)
print("Silhouette Score:", sil_score)

centre=model.cluster_centers_ # pair the centriods

# Visualize the clustered data with color-coded clusters
plt.scatter(x['Sl_No'],x['Avg_Credit_Limit'], c=model.labels_, cmap='viridis') # plt.scatter always supports 2D so here i am taking only to 2 inputs
plt.title("k-means clustering")

from sklearn.decomposition import PCA  # Import PCA (Principal Component Analysis) for dimensionality reduction

# Optional: PCA for 2D Visualization of high-dimensional data
pca= PCA(n_components=2)  # Initialize PCA to reduce to 2 components
x_pca=pca.fit_transform(x)  # Fit and transform the original features into 2D

# Plot the 2D PCA projection with cluster coloring
plt.figure(figsize=(6,4))  # Set the figure size
plt.scatter(x_pca[:,0],x_pca[:,1],c=model.labels_,cmap='viridis')  # Scatter plot with cluster labels as colors
plt.xlabel("PCA 1")  # Label for the first principal component
plt.ylabel("PCA 2")  # Label for the second principal component
plt.title("Cluster Visualization with PCA")  # Title of the plot
plt.show()  # Display the plot