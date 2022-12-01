from math import *
import random as random
import numpy as np
import matplotlib.pyplot as plt


def kMeans(k, X, Y, iterations=1):
    data = list(zip(X, Y))
    centroids = [(random.uniform(min(X), max(X)), random.uniform(min(Y), max(Y))) for _ in range(k)]
    for _ in range(iterations):
        new_centroids = centroids
        centroids, data_group_list = calcMeans(data, centroids)
    return new_centroids, data_group_list

    
def calcMeans(data, centroids):
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
        new_x, new_y = 0, 0
        if len(group) > 0:
            for point in group:
                new_x += point[0]/len(group)
                new_y += point[1]/len(group)
            new_centroids.append((new_x, new_y))
        else: 
            new_centroids.append(centroids[i])

    return centroids, data_group_list

def calcDist(p0, p1) -> float:
    return abs(sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2))

if __name__ == "__main__":
    X = [random.uniform(1, 10) for _ in range(500)]
    Y = [random.uniform(1, 10) for _ in range(500)]

    centroids, data_group_list = kMeans(4, X, Y, 4)
    
    for i, (x_c, y_c) in enumerate(centroids):
        hexadecimal = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
        plt.scatter(x_c, y_c, color = hexadecimal, marker='s')
        for (x, y) in data_group_list[i]:
            plt.scatter(x, y, color = hexadecimal)
    plt.savefig("Exemplo01 (k-Means).png")
    plt.close()
            

    

    
