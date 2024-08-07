from waitress import serve
from app import app  # Import the Flask app instance from app.py

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
