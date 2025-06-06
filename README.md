# Credit Card Customer Segmentation using K-Means Clustering

This project performs customer segmentation on credit card data using K-Means clustering. It includes data visualization, clustering evaluation using the Elbow Method and Silhouette Score, and dimensionality reduction using PCA for cluster visualization.

##  Dataset
- **File**: `Credit Card Customer Data.csv`
- Contains features such as:
  - `Sl_No`
  - `Avg_Credit_Limit`
  - `Total_Credit_Cards`

##  Objective
Segment customers based on credit card usage and credit limits to identify distinct customer groups using unsupervised learning.

---

##  Technologies & Libraries Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

##  Steps Performed

### 1. Data Loading & Exploration
- Loaded dataset using `pandas`.
- Viewed dataset structure with `.info()` and `.describe()`.

### 2. Data Visualization
- Scatter plot between `Sl_No` and `Avg_Credit_Limit`.
- Heatmap of correlations using `seaborn.heatmap`.
- Pairplot to explore relationships between features.

### 3. Feature Selection
- Selected features for clustering:  
  `['Sl_No', 'Avg_Credit_Limit', 'Total_Credit_Cards']`

### 4. Elbow Method
- Iterated `K` from 1 to 10.
- Plotted Within-Cluster Sum of Squares (WCSS) to identify the optimal number of clusters.

### 5. K-Means Clustering
- Applied `KMeans` with `n_clusters=5`.
- Predicted cluster labels.
- Identified cluster centers.

### 6. Evaluation
- Used **Silhouette Score** to assess clustering quality.

### 7. Cluster Visualization
- Used **3D scatter plot** to visualize clusters across 3 features.
- Applied **PCA** to reduce dimensions and visualize clusters in 2D.

---

##  Example Output

- **Predicted cluster** for new point `[12, 6000, 3]`
- **Silhouette Score** indicating clustering quality
- **Visualizations**: Scatter plot, heatmap, elbow graph, PCA-based cluster plot, 3D cluster plot

---

##  Requirements

Make sure the following libraries are installed:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
