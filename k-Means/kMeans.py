from math import *
import random as random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


# This function receives the number of clusters k, the data points (a list of tuples) and the number of iterations:
def kMeans(k, data, iterations=1):
    # Unzip a list of tuples returns other list of tuples where each element is a tuple with the values of the corresponding...
    # ... index of the tuples in the previus list:
    unziped_data = list(zip(*data))
    # Create random points to be the centroids:
    centroids = [(random.uniform(min(unziped_data[0]), max(unziped_data[0])), random.uniform(min(unziped_data[1]), max(unziped_data[1]))) for _ in range(k)]
    # Do each interaction to calculate the groups and new centroids:
    for _ in range(iterations):
        new_centroids = centroids
        centroids, data_group_list = calcMeans(data, centroids)
    # Returns the list of centroids and the list of group for each centroid:
    return new_centroids, data_group_list

    
def calcMeans(data, centroids):
    # The amount of group is equal the amount of centroids: 
    data_group_list = [[] for _ in range(len(centroids))]

    # Associating each point in a group:
    for point in data:
        dist, centroid_index = -1, -1
        for i, centroid in enumerate(centroids):
            if dist == -1 or dist > calcDist(point, centroid):
                dist = calcDist(point, centroid)
                centroid_index = i
        data_group_list[centroid_index].append(point)

    # Updating the centroids:
    new_centroids = []
    for i, group in enumerate(data_group_list):
        # The group must have at least one element:
        if len(group) > 0:
            new_x = 0
            new_y = 0
            for point in group:
                new_x += point[0]/len(group)
                new_y += point[1]/len(group)
            new_centroids.append((new_x, new_y))
        # If the group has no elements then the group old centroid must be...
        # ... deleted:
        else:
            data_group_list = data_group_list[:i] + data_group_list[i+1:]

    return new_centroids, data_group_list

# This function calculates the distance squared between two points and these points can have...
# ... wherever dimension:
def calcDist(p0, p1) -> float:
    sum = 0
    for i in range(0, len(p0)):
        sum += (p0[i] - p1[i])**2
    return sum

def PlotkMeans(centroids, data_group_list, file_name):
    for i, point in enumerate(centroids):
        hexadecimal = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
        plt.scatter(*zip(*[point]), color = hexadecimal, marker='o', s = 100, alpha = 0.5)
        for point_data in data_group_list[i]:
            plt.scatter(*zip(*[point_data]), color = hexadecimal)
    plt.savefig(f"C:\\Users\\bruni\\OneDrive\\Documentos\\GitHub\\OTPA001I\\k-Means\\{file_name}.png")
    plt.close()


if __name__ == "__main__":

    # Exemple01 (2d plot):
    X = [random.uniform(1, 200) for _ in range(200)]
    Y = [random.uniform(1, 200) for _ in range(200)]
    data = list(zip(X, Y))

    centroids, data_group_list = kMeans(8, data, 1)
    PlotkMeans(centroids, data_group_list, "Exemplo01 (k-Means)")