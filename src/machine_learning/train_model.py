import numpy as np
from src.machine_learning.model import DDoSModel

X_train = np.array([[10, 0.1], [50, 0.6], [100, 0.9]])
y_train = np.array([0, 0, 1])

model = DDoSModel()
model.train(X_train, y_train)
model.save_model('ddos_model.pkl')

X_test = np.array([[20, 0.2], [90, 0.8]])
predictions = model.predict(X_test)
print(predictions)