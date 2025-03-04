# Backend Documentation

## Overview
This is the backend for the Crypto Blog project, which includes a Flask application that serves as the API for managing user subscriptions and providing cryptocurrency price predictions.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd crypto-blog/backend
   ```

2. **Install Dependencies**
   It is recommended to use a virtual environment. You can create one using:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Initialization**
   The SQLite database is included as `database.db`. If you need to reset or initialize the database, you can run the necessary scripts defined in `app.py`.

4. **Running the Application**
   To start the Flask application, run:
   ```bash
   python app.py
   ```
   The application will be available at `http://127.0.0.1:5000`.

## Usage
- **API Endpoints**
  - `/api/predictions`: Get the latest cryptocurrency predictions.
  - `/api/subscribe`: Subscribe a user to the blog for updates.
  - `/api/reset`: Reset daily data for predictions.

## Contributing
Feel free to submit issues or pull requests for improvements or bug fixes. Please ensure that your code adheres to the project's coding standards.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.