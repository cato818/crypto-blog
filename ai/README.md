# AI Module for Cryptocurrency Price Prediction

This directory contains the code and resources for the AI module of the cryptocurrency blog project. The AI module is responsible for training predictive models that forecast cryptocurrency prices based on historical data.

## Files

- **model.py**: Contains the machine learning model definition and training logic. This file includes functions for training the model and making predictions.

- **train.py**: Responsible for collecting data from APIs, training the predictive model, and saving predictions to the database or a JSON file.

## Setup Instructions

1. Ensure you have Python installed on your machine.
2. Install the required libraries by running:
   ```
   pip install -r requirements.txt
   ```
3. Run the training script to train the model and generate predictions:
   ```
   python train.py
   ```

## Usage

After training the model, you can use the functions defined in `model.py` to make predictions on cryptocurrency prices. The predictions can be accessed through the backend API and displayed on the frontend of the blog.