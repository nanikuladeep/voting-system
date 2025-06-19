from sklearn.ensemble import IsolationForest
import numpy as np
import pickle
import os

def load_model():
    if not os.path.exists('models/model.pkl'):
        model = IsolationForest(contamination=0.1)
        X_train = np.random.rand(100, 2)
        model.fit(X_train)
        with open('models/model.pkl', 'wb') as f:
            pickle.dump(model, f)
    else:
        with open('models/model.pkl', 'rb') as f:
            model = pickle.load(f)
    return model

def detect_anomaly(user_id):
    model = load_model()
    test_data = np.random.rand(1, 2)  # Simulate user voting pattern
    prediction = model.predict(test_data)
    return prediction[0] == -1
