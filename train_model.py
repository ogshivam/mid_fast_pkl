# train_model.py
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

# Create a simple regression dataset
X, y = make_regression(n_samples=100, n_features=1, noise=0.1, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the model as a pickle file
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")
