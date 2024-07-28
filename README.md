# Customer Segmentation Using K-Means Clustering
This project was made as part of the requirements for completing a Python for AI addon course at college.

* [Google Collab Version](https://colab.research.google.com/drive/1X8rVN6RHm6bWsXzWHC4jfn0RpALM0sAK?usp=sharing)
* [Source for the dataset used](https://raw.githubusercontent.com/ugis22/clustering_analysis/master/customers.csv)

## Aim
To group the customers from a given dataset into different segments(clusters) using the K-Means clustering method

## Notes
* Using the Davies-Bouldin Score method to calculate the optimal number of clusters. The Elbow method can't be used because it is a visual method and thus hard to obtain "elbow point" mathematically.
* The dataset is clustered and plotted as a function of ***Annual Income*** versus ***Spending Score***

## How To Run This
* You need to have python3 and pip installed.
* It is recommended to set up a [virtual environment](https://docs.python.org/3/library/venv.html).
* First, from the project root, open a shell/terminal and run the following commands:
``` shell
pip install -r requirements.txt
cd src
python app.py
```
* note to use `python3` or `python` according to the executable provided by your environment.