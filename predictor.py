# predictor.py
import pickle
import numpy as np

# Load the pickled model
with open("./model.pkl", "rb") as f:
    model = pickle.load(f)

def predict(input_data):
    # Ensure the input is a NumPy array
    input_array = np.array(input_data).reshape(-1, 1)
    # Make predictions
    predictions = model.predict(input_array)
    return predictions.tolist()
