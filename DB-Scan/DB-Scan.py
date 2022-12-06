from math import *
import random as random
import numpy as np
import matplotlib.pyplot as plt

def dbScan(data, radius, minimum_cluster = 4):
    # Mark if the point was already:
    data_mark = {}
    for point in data:
        # No point has been selected yet:
        data_mark[point] = {'Selected' : False}

    # Start the groups creation:
    data_groups = []
    for point in data:
        # if the point is already set as selected, so it has also been included in a group already, so...
        # ... we must continue looking to the next point:
        if data_mark[point]['Selected'] == True:
            continue
        else:
            # The actual point is now selected:
            data_mark[point]['Selected'] = True
            # Create a group using the actual point selected and his neighbors:
            group = [point] + dbScanBuild(point, data, data_mark, radius, minimum_cluster)
            # Append the group to the list of groups:
            data_groups.append(group)
            # Set all the points in the group as selected:
            for point_group in group:
                data_mark[point_group]['Selected'] = True
    return data_groups

def dbScanBuild(actual_point, data, data_mark, radius, minimum_cluster):
     
    neighbors = []
    num_neighbors = 0

    # Verify how many and which are the points near the actual point:
    for point in data:
        # If the point is inside the radius of the actual point this point is a neighbor:
        if point != actual_point and calcDist(actual_point, point) < (radius**2):
            # If this point was not selected before then:
            if data_mark[point]['Selected'] == False:
                neighbors.append(point)
                # Notice that this mark cuts the possibility of infinite recursion:
                data_mark[point]['Selected'] = True
            # The maybe has been already selected, but in both cases he is counted as a neighbor:
            num_neighbors += 1
    
    # If the actual point has no neighbors (he is alone) then he will return no list (because a list containing only him self...
    # ... was already added to the list of groups in the call of dbScanBuild()), or...
    # ... if the actual point has neighbors but they have already been selected then this point was already been returned in...
    # ... in the next step of other call of this function (with some of his neighbors):
    if num_neighbors < minimum_cluster or neighbors == []:
        return []

    # If the actual point is a core, i.e., it has neighbors and this neighbors didn't have been selected before this function...
    # ... call, then:
    group = []
    for point in neighbors:
        # group has the return of the recursion of this function on the neighbor points:
        add_group = dbScanBuild(point, data, data_mark, radius, minimum_cluster)
        group = group + add_group
        # we need to actualize the dictionary setting the added points as selected points:
        for added in add_group:
            data_mark[added]['Selected'] = True
    # return the neighbors + the neighbor's neighbors:
    return neighbors + group

# This function calculates the distance squared between two points and these points can have...
# ... wherever dimension:
def calcDist(p0, p1) -> float:
    sum = 0
    for i in range(0, len(p0)):
        sum += (p0[i] - p1[i])**2
    return sum


def PlotdbScan(data_groups, file_name):
    for group in data_groups:
        hexadecimal = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
        plt.scatter(*zip(*group), color = hexadecimal, marker='o', s = 100, alpha = 0.5)
    plt.savefig(f"C:\\Users\\bruni\\OneDrive\\Documentos\\GitHub\\OTPA001I\\DB-Scan\\{file_name}.png")
    plt.close()

if __name__ == "__main__":
    data = [(random.uniform(1, 200), random.uniform(1, 200)) for _ in range(200)]
    radius = 20

    # X_circle_1 = np.linspace(-1, 1, 50)
    # Y_circle_1 = [sqrt(1 - x**2) for x in X_circle_1]
    # X_circle_2 = np.linspace(-2, 2, 50)
    # Y_circle_2 = [sqrt(4 - x**2) for x in X_circle_2]
    # X_circle_3 = np.linspace(-2, 2, 50)
    # Y_circle_3 = [sqrt(4.1 - x**2) for x in X_circle_3]
    # data = list(zip(X_circle_1, Y_circle_1)) + list(zip(X_circle_2, Y_circle_2)) + list(zip(X_circle_3, Y_circle_3))
    # radius = 0.9999999

    data_groups = dbScan(data, radius)
    PlotdbScan(data_groups, 'Exemplo01 (DB-Scan)')