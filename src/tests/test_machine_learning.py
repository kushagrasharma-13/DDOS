import unittest
from machine_learning.model import DDoSModel
import numpy as np

class TestDDoSModel(unittest.TestCase):

    def setUp(self):
        self.model = DDoSModel()
        self.X_train = np.array([[10, 0.1], [50, 0.6], [100, 0.9]])
        self.y_train = np.array([0, 0, 1])
        self.X_test = np.array([[20, 0.2], [90, 0.8]])

    def test_train_and_predict(self):
        self.model.train(self.X_train, self.y_train)
        predictions = self.model.predict(self.X_test)
        self.assertEqual(len(predictions), 2)

    def test_save_and_load_model(self):
        self.model.train(self.X_train, self.y_train)
        self.model.save_model('test_model.pkl')
        loaded_model = DDoSModel()
        loaded_model.load_model('test_model.pkl')
        predictions = loaded_model.predict(self.X_test)
        self.assertEqual(len(predictions), 2)

if __name__ == '__main__':
    unittest.main()