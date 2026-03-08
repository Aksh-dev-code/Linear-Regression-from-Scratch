# Multi-Linear Regression From Scratch

## Project Overview

This project implements **Multi-Linear Regression from scratch using Gradient Descent** to understand how machine learning models work internally without relying on high-level ML libraries.

Instead of using frameworks like scikit-learn, the regression algorithm and optimization process are implemented manually using **NumPy**.

The project also includes a **Streamlit web application** that predicts the **tip amount** based on input features.

---

## Features

* Multi-Linear Regression implemented from scratch
* Gradient Descent optimization
* One-Hot Encoding for categorical variables
* Exploratory Data Analysis using visualization libraries
* Tip prediction web application built with Streamlit

---

## Python libraries are Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Streamlit

---

## Project Structure

```
MultiLinearRegression/
│
├── app.py                 # Streamlit web application
├── setup.py               # Package configuration
├── requirements.txt       # Project dependencies
├── .gitignore             # Files ignored by Git
│
├── NOTEBOOKS/
│   └── MultiLinearRegression.ipynb   # Model development and experiments
│
└── README.md              # Project documentation
```

---


## How the Model Works

The model is built using **Multi-Linear Regression with Gradient Descent**.

Main steps:

1. Data preprocessing
2. One-Hot Encoding for categorical variables
3. Parameter initialization
4. Gradient Descent optimization
5. Model prediction

The algorithm iteratively updates the weights to minimize the **Mean Squared Error (MSE)** loss function.

---

## Key Learnings

Building the model from scratch helped in understanding:

* How regression models learn parameters
* How Gradient Descent minimizes loss
* Feature encoding techniques
* The internal mechanics of machine learning algorithms

---

## Future Work

* Apply the model to larger real-world datasets
* Perform deeper Exploratory Data Analysis
* Implement additional machine learning algorithms from scratch

---

## Author

Anuska Maity

Learning Machine Learning and Data Science by building projects from scratch.
