# Crypto Blog with Predictive AI for Cryptocurrency Prices

This project is a blog that utilizes predictive AI to forecast cryptocurrency prices. It is structured into three main components: a Flask backend, an AI module for predictions, and a JavaScript frontend.

## Project Structure

```
crypto-blog
├── backend          # Contains the Flask application
│   ├── app.py      # Main entry point for the Flask app
│   ├── models.py   # Database models and schema definitions
│   ├── routes.py   # API endpoints for the application
│   ├── database.db  # SQLite database file
│   ├── requirements.txt  # Python dependencies
│   └── README.md   # Documentation for the backend
├── frontend         # Contains the frontend application
│   ├── index.html   # Main HTML file for the frontend
│   ├── styles.css   # CSS styles for the frontend
│   ├── script.js     # JavaScript code for dynamic interactions
│   └── README.md    # Documentation for the frontend
├── ai               # Contains the AI module
│   ├── model.py     # Machine learning model definition
│   ├── train.py     # Data collection and model training
│   └── README.md    # Documentation for the AI module
├── .gitignore       # Files and directories to ignore by Git
└── README.md        # Overall documentation for the project
```

## Features

- **Predictive AI**: Uses machine learning to forecast cryptocurrency prices.
- **User Subscription**: Allows users to subscribe for updates on predictions.
- **Dynamic Blog**: A frontend that displays predictions and user interactions.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd crypto-blog
   ```

2. Set up the backend:
   - Navigate to the `backend` directory.
   - Install the required Python packages:
     ```
     pip install -r requirements.txt
     ```

3. Run the Flask application:
   ```
   python app.py
   ```

4. Set up the frontend:
   - Open `frontend/index.html` in a web browser.

5. For AI model training, navigate to the `ai` directory and run:
   ```
   python train.py
   ```

## Usage

- Access the blog at `http://localhost:5000` after starting the Flask server.
- Users can subscribe to receive updates on cryptocurrency predictions.
- Predictions will be displayed dynamically on the frontend.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.