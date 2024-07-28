import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score
import matplotlib.pyplot as plt

customerData=pd.read_csv("./customers.csv")

# mapping string to integers for processing
customerData["Gender"]=customerData["Gender"].map({
  "Male":0,
  "Female":1
})

income_vs_spending_score=customerData[["Annual Income (k$)", "Spending Score (1-100)"]]

# Define a range of cluster sizes to test
k_values=range(2, 15)
davies_bouldin_scores=[]

# Iterate through different cluster sizes
for k in k_values:
  # Apply k-means clustering
  kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=300, n_init=10, random_state=0)
  kmeans.fit(income_vs_spending_score)
  # Calculate Davies-Bouldin score
  davies_bouldin_scores.append(davies_bouldin_score(income_vs_spending_score, kmeans.labels_))

# find k value with minimum davies-bouldin score
min_davies_bouldin_index = davies_bouldin_scores.index(min(davies_bouldin_scores))
optimal_num_clusters=k_values[min_davies_bouldin_index];

# Davies-Bouldin Score
plt.plot(k_values, davies_bouldin_scores, marker='o', zorder=1)
plt.title('Davies-Bouldin Score For Optimal Number Of Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('Davies-Bouldin Score')
plt.xticks(list(k_values))

# Mark the optimal number of clusters
plt.scatter(optimal_num_clusters, davies_bouldin_scores[min_davies_bouldin_index], color='red', marker='o', s=100, zorder=2)

plt.show()

print(f"\nThe optimal number of clusters is: {optimal_num_clusters}\n")

# creating the final model
kmeans=KMeans(n_clusters=optimal_num_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
model=kmeans.fit_predict(income_vs_spending_score)

# Visualize the clusters
plt.scatter(income_vs_spending_score["Annual Income (k$)"], income_vs_spending_score["Spending Score (1-100)"], c=model, cmap='rainbow', edgecolors='k', s=50)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', marker='X', label='Centroids')
plt.title('KMeans Clustering of Customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()