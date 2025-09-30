import flask
import logging
import os
from datetime import datetime

app = flask.Flask(__name__)

# Create logs directory if it doesn't exist
os.makedirs('/app/logs', exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler('/app/logs/app.log'),
        logging.StreamHandler()  # Also log to console
    ]
)

# Get the logger
logger = logging.getLogger(__name__)

@app.before_request
def log_request_info():
    """Log information about each request"""
    logger.info(f'Request: {flask.request.method} {flask.request.path} from {flask.request.remote_addr}')

@app.after_request
def log_response_info(response):
    """Log information about each response"""
    logger.info(f'Response: {response.status_code} for {flask.request.method} {flask.request.path}')
    return response

@app.route('/')
def home():
    return "Hello from Foodly in Docker!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)