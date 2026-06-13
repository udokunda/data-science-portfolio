# Random Forest Rice Classification

# Overview
This project implements a Random Forest Classifier using Scikit-Learn to classify rice grains from the Rice (Cammeo and Osmancik) dataset obtained from the UCI Machine Learning Repository.
The objective is to predict whether a rice grain belongs to the Cammeo or Osmancik variety based on its physical characteristics.

# Dataset
- Dataset: Rice (Cammeo and Osmancik)
- Source: UCI Machine Learning Repository
Features include several geometric measurements of rice grains such as area, perimeter, major axis length, minor axis length, eccentricity, convex area, and extent.
## Target Variable:
 - Cammeo
 - Osmancik
## Technologies Used
- Python
- Pandas
- Scikit-Learn
- UCIMLRepo
  
# Machine Learning Workflow
1. Load the Rice dataset from UCI.
2. Split the data into training and testing sets.
3. Train a Random Forest Classifier.
4. Generate predictions on unseen data.
5. Evaluate model performance using:
    - Confusion Matrix
    - Accuracy
    - Precision
    - Recall (Sensitivity)
    - F1 Score
    - Classification Report

# Results
The Random Forest model achieves high classification performance on the Rice dataset, demonstrating its effectiveness in distinguishing between Cammeo and Osmancik rice varieties.

# Learning Outcomes

- This project demonstrates:
- Data loading and preprocessing
- Train-test splitting
- Random Forest classification
- Model evaluation
- Performance metric interpretation
- Binary classification using Scikit-Learn
