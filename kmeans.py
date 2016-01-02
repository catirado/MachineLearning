import numpy as np
import math

MAX_ITERATIONS = 100


def run(data_set, k):
    iterations = 0
    centroids = []
    old_centroids = [[] for i in range(k)]

    centroids = get_random_centroids(data_set, centroids, k)

    while not has_converged(old_centroids, centroids, iterations):
        old_centroids = centroids
        iterations += 1
        clusters = get_clusters(data_set, centroids, k)
        centroids = calculate_new_centroids(clusters, data_set, k)

    return centroids, clusters, iterations


def has_converged(old_centroids, centroids, iterations):
    return (iterations > MAX_ITERATIONS) or old_centroids == centroids


def get_random_centroids(data_set, centroids, k):
    for cluster in range(k):
        centroids.append(data_set[np.random.randint(0, len(data_set), size=1)])
    return centroids


def get_clusters(data_set, centroids, k):
    clusters = [[] for i in range(k)]
    for x in data_set:
        best = centroids.index(min(centroids, key=lambda c: euclidean_distance(x,c)))
        clusters[best] += [x]
    return clusters


def calculate_new_centroids(clusters, data_set, k):
    new_centroids = [[] for i in range(k)]
    i = 0
    for cluster in clusters:
        if not cluster:
            new_centroids[i] = data_set[np.random.randint(0, len(data_set), size=1)]
        else:
            new_centroids[i] = np.mean(cluster, axis=0).tolist()
        i += 1

    return new_centroids


def euclidean_distance(x,y):
    distance = 0
    for i in range(len(x)):
        distance += pow((x[i] - y[i]),2)
    return math.sqrt(distance)