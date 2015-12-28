import unittest
import knn

class KnnTests(unittest.TestCase):
    def test_euclidean_distance(self):
        data1 = [2, 2, 2, 2]
        data2 = [4, 4, 4, 4]
        distance = knn.euclidean_distance(data1, data2)
        self.assertEqual(distance, 4)

    def test_calculate_accuracy(self):
        self.assertEqual(True,False)

    #test para ambas

if __name__ == '__main__':
    unittest.main()
