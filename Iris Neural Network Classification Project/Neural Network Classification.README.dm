# Iris Neural Network Classification Project
This project demonstrates a supervised machine learning workflow using an Artificial Neural Network (ANN) on the Iris dataset with Python and scikit-learn.

## Project Overview
The neural network is trained to classify Iris flower species based on sepal and petal measurements. The project includes data preprocessing, normalization, one-hot encoding, dataset splitting, model training, validation, testing, and performance evaluation.

# Features
Loads and processes the Iris dataset from a CSV file
Applies Max-Min normalization to input features
Uses one-hot encoding for target labels
Splits the dataset into:
50% Training Data
25% Validation Data
25% Testing Data
Implements a neural network with:
4 Input Nodes
20 Hidden Nodes
3 Output Nodes
Monitors training and validation loss after every epoch
Evaluates model performance using test accuracy
Technologies Used
Python
Pandas
NumPy
Scikit-learn
Machine Learning Workflow
Import required libraries
Load the Iris dataset
Normalize input features using Max-Min normalization
Apply one-hot encoding to target labels
Split the dataset into training, validation, and testing sets
Build the neural network model
Train the model and monitor loss
Test the model on unseen data
Evaluate final accuracy
Evaluation Metrics
The following metrics are used to evaluate the model:

Training Loss (Sum-of-Squares)
Validation Loss (Sum-of-Squares)
Test Accuracy
Conclusion
This project demonstrates the implementation of a neural network for multiclass classification using the Iris dataset. It provides a practical introduction to data preprocessing, neural network training, and model evaluation using scikit-learn.
