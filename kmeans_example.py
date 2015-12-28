import kmeans
import arff


if __name__ == '__main__':
    data_set = arff.load(open('./data/flores_clustering.arff'))
    results = kmeans.run(data_set['data'], 100)
    print(results)
