import knn
import arff

if __name__ == '__main__':

    train_set = arff.load(open('./data/flores_train.arff'))
    test_set = arff.load(open('./data/flores_test.arff'))
    results = []

    print train_set
    for x in range (len(test_set['data'])):
        result = knn.classify(train_set['data'], test_set['data'][x][:-1])
        results.append(result)
        print "Real: " + test_set['data'][x][-1] + " - Predicted: " + result

    accuracy = knn.calculate_accuracy(test_set['data'], results)
    print "Accuracy: " + str(accuracy) + "%"