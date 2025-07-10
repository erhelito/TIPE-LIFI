from math import sqrt
import matplotlib.pyplot as plt

with open('data/30m.csv', 'r') as f:
    raw_data = f.readlines()

data = []

for i in raw_data :
    x,y = i.split(',')
    
    data.append([float(x), float(y)])

def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

centers = [[min(point[0] for point in data), min(point[1] for point in data)],[max(point[0] for point in data), max(point[1] for point in data)]]

def k_means(data, centers, n=100):
    n_points = len(data)
    n_clusters = len(centers)
    
    labels = [0] * n_points
    
    for _ in range(n):
        plt.figure(f'K-mean, n={_}')
        plt.scatter([point[0] for point in data], [point[1] for point in data], c=labels, cmap='viridis', marker='+', s=40, label='Mesures')
        plt.scatter([center[0] for center in centers], [center[1] for center in centers], c='red', marker='x', s=100, label='Centres')
        plt.title(f'K-mean, n={_}')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.colorbar()
        plt.grid()
        plt.legend()
        plt.tight_layout()
        
        # update labels
        new_labels = []
        for i in range(n_points):
            # compute all distances, attribute new centers
            distances = [distance(data[i], center) for center in centers]
            new_labels.append(distances.index(min(distances)))

        plt.figure(f'K-mean, n={_}, nouveaux labels')
        plt.scatter([point[0] for point in data], [point[1] for point in data], c=new_labels, cmap='viridis', marker='+', s=40, label='Mesures')
        plt.scatter([center[0] for center in centers], [center[1] for center in centers], c='red', marker='x', s=100, label='Centres')
        plt.title(f'K-mean, n={_}, nouveaux labels')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.colorbar()
        plt.grid()
        plt.legend()
        plt.tight_layout()

        # update clusters
        new_centers = []
        for k in range(n_clusters):
            cluster_points = [data[i] for i in range(n_points) if new_labels[i] == k]
            if cluster_points != []: # for not empty clusters
                mean_x = sum(point[0] for point in cluster_points) / len(cluster_points)
                mean_y = sum(point[1] for point in cluster_points) / len(cluster_points)
                new_centers.append([mean_x, mean_y])

            else: # for empty clusters
                new_centers.append(centers[k])
        
        # check for convergence
        if new_centers == centers:
            break
        centers = new_centers
        labels = new_labels

    return centers, labels

centers, labels = k_means(data, centers, n=5000)

string = ''

for i in labels:
    string += str(i)

string

plt.show()