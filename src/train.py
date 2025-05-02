from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import joblib

# Use iris dataset as a placeholder for EEG-like data
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3)

# Train a simple model
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'model/sleep_stage_model.h5')
print("✅ Model trained and saved to model/sleep_stage_model.h5")
