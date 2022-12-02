from math import *
import random as random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


# This function receives the number of clusters k, the data points (it can have any dimension)
def kMeans(k, data, iterations=1):
    unziped_data = list(zip(*data))
    dimensions = len(unziped_data)
    centroids = []
    for i in range(k):
        coord = []
        for j in range(dimensions):
            coord.append(random.uniform(min(unziped_data[j]), max(unziped_data[j])))
        centroids.append(tuple(coord))

    for _ in range(iterations):
        new_centroids = centroids
        centroids, data_group_list = calcMeans(data, centroids, dimensions)
    return new_centroids, data_group_list

    
def calcMeans(data, centroids, dimensions):
    data_group_list = [[] for _ in range(len(centroids))]

    for point in data:
        dist, centroid_index = -1, -1
        for i, centroid in enumerate(centroids):
            if dist == -1 or dist > calcDist(point, centroid):
                dist = calcDist(point, centroid)
                centroid_index = i
        data_group_list[centroid_index].append(point)

    new_centroids = []
    for i, group in enumerate(data_group_list):
        new_coords = [0 for _ in range(dimensions)]
        if len(group) > 0:
            for point in group:
                for i, coord in enumerate(point):
                    new_coords[i] += coord/len(group)
            new_centroids.append(tuple(new_coords))
        else:
            new_centroids.append(centroids[i])

    return new_centroids, data_group_list

def calcDist(p0, p1) -> float:
    sum = 0
    for i in range(0, len(p0)):
        sum += (p0[i] - p1[i])**2
    return sum

if __name__ == "__main__":

    # Exemple01 (2d plot):
    X = [random.uniform(1, 200) for _ in range(200)]
    Y = [random.uniform(1, 200) for _ in range(200)]
    data = list(zip(X, Y))

    centroids, data_group_list = kMeans(8, data, 1)
    
    for i, (x_c, y_c) in enumerate(centroids):
        hexadecimal = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
        plt.scatter(x_c, y_c, c = hexadecimal, marker='o', s = 100, alpha = 0.5)
        for (x, y) in data_group_list[i]:
            plt.scatter(x, y, color = hexadecimal)
    plt.savefig("C:\\Users\\bruni\\OneDrive\\Documentos\\GitHub\\OTPA001I\\k-Means\\Exemplo01 (k-Means).png")
    plt.close()

    #Exemple02 (3d plot):
    X = [random.uniform(1, 200) for _ in range(200)]
    Y = [random.uniform(1, 200) for _ in range(200)]
    Z = [random.uniform(1, 200) for _ in range(200)]
    data = list(zip(X, Y, Z))

    centroids, data_group_list = kMeans(4, data, 1)
    
    for i, (x_c, y_c, z_c) in enumerate(centroids):
        hexadecimal = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
        ax = plt.axes(projection = '3d')
        ax.scatter3D(x_c, y_c, z_c, color = hexadecimal, marker='o', s = 100, alpha = 0.5)
        for (x, y, z) in data_group_list[i]:
            ax.scatter3D(x, y, z, color = hexadecimal)
    plt.savefig("C:\\Users\\bruni\\OneDrive\\Documentos\\GitHub\\OTPA001I\\k-Means\\Exemplo02 (k-Means).png")
    plt.close()
