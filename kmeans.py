#https://gist.github.com/iandanforth/5862470
#http://codereview.stackexchange.com/questions/80050/k-means-clustering-algorithm-in-python
#http://stanford.edu/~cpiech/cs221/handouts/kmeans.html
#http://pandoricweb.tumblr.com/post/8646701677/python-implementation-of-the-k-means-clustering

#centroides := lista con k instancias (arbitrarias);
#Mientras (no se decida salir) hacer:
#1. clusteres := lista con k listas vacias; // se corresponden 1 a 1 con los centroides
#2. para cada t de T, calcular el indice i del centroide que menos dista a t; incluir t en el cluster de ndice i
#3. nuevosCentroides := centroides de los nuevos clusteres [OJO] tengo que tener cuidado si llego a 0
#4. if nuevosCentroides == centroides then salir
#else if salir? then salir
#else centroides := nuevosCentroides
#finMientras
#devolver la funcion que lleva cada t al indice i del cluster en el que aparece.

def run(data_set, k):

    centroids = []

    centroids = get_random_centroids(data_set, centroids, k)
    iter = 0
    old_centroids = None

    while not has_converged(old_centroids, centroids, iter):
        old_centroids = centroids

        #centroids = calculate_new_centroids(data_set, labels, k)

    return centroids


def has_converged(old_centroids, centroids, iterations):
    return True


def get_random_centroids():
    return  True