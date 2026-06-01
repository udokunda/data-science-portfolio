import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

# ---------------------------------------------------
# LOAD DATASET
# ---------------------------------------------------

# Load Iris dataset
data = pd.read_csv(r"C:\Users\2539990\Documents\Iris Neural Network Classification Project\Iris_DataSet.csv", sep=";", header=None)
data.columns = [
    "SepalLength",
    "SepalWidth",
    "PetalLength",
    "PetalWidth",
    "Species"
]
# Display first rows
print(data.head())

# ---------------------------------------------------
# PREPARE INPUTS AND TARGETS

# Features
X = data.iloc[:, :-1]

# Labels
y = data.iloc[:, -1]

# Labels
y = data.iloc[:, -1]
print(X.head())
print(y.head())

# ---------------------------------------------------
# NORMALISE INPUT VALUES
# USING MAX-MIN NORMALISATION
# ---------------------------------------------------

scaler = MinMaxScaler()

X_scaled = scaler.fit_transform(X)
print(X_scaled[:5])

# ---------------------------------------------------
# ONE-HOT ENCODING OF TARGET VALUES
# ---------------------------------------------------

encoder = OneHotEncoder(sparse_output=False)

y_encoded = encoder.fit_transform(y.values.reshape(-1, 1))

# ---------------------------------------------------
# ONE-HOT ENCODING OF TARGET VALUES
# ---------------------------------------------------

encoder = OneHotEncoder(sparse_output=False)

y_encoded = encoder.fit_transform(y.values.reshape(-1, 1))

# ---------------------------------------------------
# SPLIT DATASET
# 50% TRAINING
# 25% VALIDATION
# 25% TESTING
# ---------------------------------------------------

X_train, X_temp, y_train, y_temp = train_test_split(
    X_scaled,
    y_encoded,
    test_size=0.5,
    random_state=42
)

X_validation, X_test, y_validation, y_test = train_test_split(
    X_temp,
    y_temp,
    test_size=0.5,
    random_state=42
)

# ---------------------------------------------------
# CREATE NEURAL NETWORK
# ---------------------------------------------------

model = MLPClassifier(
    hidden_layer_sizes=(20,),
    activation='relu',
    solver='sgd',
    max_iter=1,
    warm_start=True,
    random_state=42
)

# # ---------------------------------------------------
# # TRAIN NETWORK EPOCH BY EPOCH
# # ---------------------------------------------------
train_losses = []
validation_losses = []

epochs = 100

for epoch in range(epochs):

    model.fit(X_train, y_train)

    train_predictions = model.predict_proba(X_train)
    validation_predictions = model.predict_proba(X_validation)

    train_loss = np.sum((y_train - train_predictions) ** 2)
    validation_loss = np.sum((y_validation - validation_predictions) ** 2)

    train_losses.append(train_loss)
    validation_losses.append(validation_loss)

    print(f"Epoch {epoch+1}")
    print("Training Loss:", train_loss)
    print("Validation Loss:", validation_loss)

# ---------------------------------------------------
# TESTING PHASE
# ---------------------------------------------------

# Predict test data
test_predictions = model.predict(X_test)

# Convert one-hot encoded values to class labels
y_test_labels = np.argmax(y_test, axis=1)

test_prediction_labels = np.argmax(test_predictions, axis=1)

# Calculate accuracy
accuracy = accuracy_score(
    y_test_labels,
    test_prediction_labels
)

# Display accuracy
print("\nFinal Test Accuracy:", accuracy)

plt.figure(figsize=(10,6))

plt.plot(range(1, epochs + 1), train_losses,
         label='Training Loss')

plt.plot(range(1, epochs + 1), validation_losses,
         label='Validation Loss')

plt.xlabel('Epoch')
plt.ylabel('Sum of Squares Loss')
plt.title('Training vs Validation Loss')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(6,4))
plt.bar(['Test Accuracy'], [accuracy])
plt.ylabel('Accuracy')
plt.title('Neural Network Test Accuracy')
plt.ylim(0, 1)
plt.show()


cm = confusion_matrix(
    y_test_labels,
    test_prediction_labels
)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm
)

disp.plot()
plt.title("Confusion Matrix")
plt.show()