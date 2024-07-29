# Student Management System

This is a simple backend for a Student Management System built using Flask and MongoEngine. The system allows for adding, updating, retrieving, and deleting student records.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- MongoDB
- pip (Python package installer)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/student-management-system.git
    cd student-management-system
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Make sure your MongoDB server is running on `localhost:27017`.

### Running the Application

1. Start the Flask application:

    ```bash
    python app.py
    ```

2. The application will be available at `http://localhost:5000`.

## Running Tests

You can use Postman to test the API endpoints. Import the provided Postman collection (`postman_collection.json`) to get started quickly.

## Built With

- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [MongoEngine](https://mongoengine.org/) - The ORM used for MongoDB
