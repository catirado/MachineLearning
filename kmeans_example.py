import kmeans
import arff


def flores_clustering_data_set_run():
    data_set = arff.load(open('./data/flores_clustering.arff'))
    k = 3
    results = kmeans.run(data_set['data'], k)
    print "Centroids"
    print results[0]
    print "Clusters"
    print results[1]
    print "Resolved in " + str(results[2]) + " iterations"


def baloncesto_data_set_run():
    data_set = arff.load(open('./data/baloncesto.arff'))
    k = 3
    results = kmeans.run(data_set['data'], k)
    print "Centroids"
    print results[0]
    print "Clusters"
    print results[1]
    print "Resolved in " + str(results[2]) + " iterations"


if __name__ == '__main__':
    flores_clustering_data_set_run()
    baloncesto_data_set_run()