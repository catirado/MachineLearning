import math
import operator


def classify(train_set, test_data, k=3):

    #Sea U la lista vacia
    distances = []
    #Para cada t de TraintSet incluir ((d(x,t),t) en U;
    for t in range(len(train_set)):
        distance = euclidean_distance(test_data, train_set[t][:-1])
        distances.append((distance, train_set[t]))

    #Ordenar U respecto a la primera componente;
    distances.sort()

    k_neighbors_classes = {}
    #Calcular las frecuencias de las clases en los k primeros elementos de U
    for i in range(k):
        klass = distances[i][1][-1]
        k_neighbors_classes[klass] = k_neighbors_classes.get(klass, 0) + 1

    #Devolver j, la clase de mayor frecuencia
    sorted_classes = sorted(k_neighbors_classes.iteritems(), key=operator.itemgetter(1), reverse=True)

    return sorted_classes[0][0]


def euclidean_distance(x,y):
    distance = 0
    for i in range(len(x)):
        distance += pow((x[i] - y[i]),2)
    return math.sqrt(distance)


def calculate_accuracy(test_set, results):
    correct = 0
    for x in range(len(test_set)):
        if test_set[x][-1] is results[x]:
			correct += 1
    return (correct/float(len(test_set))) * 100.0