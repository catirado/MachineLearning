import knn
import arff
import list_helper


def flores_data_set_run():
    data_set = arff.load(open('./data/flores.arff'))
    test_set, train_set = list_helper.separate_list(data_set['data'], 10)
    results = []

    for x in range(len(test_set)):
        result = knn.classify(train_set, test_set[x][:-1])
        results.append(result)
        print "Real: " + test_set[x][-1] + " - Predicted: " + result

    accuracy = knn.calculate_accuracy(test_set, results)
    print "Accuracy: " + str(accuracy) + "%"


def prediccion_data_set_run():
    data_set = arff.load(open('./data/prediccion.arff'))
    cleaned_data_set = [list_helper.unicode_to_int(x) for x in data_set['data']]
    test_set, train_set = list_helper.separate_list(cleaned_data_set, 1)

    results = []

    for x in range(len(test_set)):
        result = knn.classify(train_set, test_set[x][:-1])
        results.append(result)
        print "Real: " + str(test_set[x][-1]) + " - Predicted: " + str(result)

    accuracy = knn.calculate_accuracy(test_set, results)
    print "Accuracy: " + str(accuracy) + "%"


if __name__ == '__main__':
    flores_data_set_run()
    prediccion_data_set_run()

