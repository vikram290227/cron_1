import logging
import requests
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def check_api_health():
    url = "https://jsonplaceholder.typicode.com/posts/1"  # Sample API endpoint
    try:
        logging.info(f"Sending request to {url}")
        response = requests.get(url)
        if response.status_code == 200:
            logging.info("API is healthy. Response data:")
            logging.info(response.json())
        else:
            logging.warning(f"API health check failed. Status code: {response.status_code}")
    except Exception as e:
        logging.error(f"Error during API health check: {e}")

if __name__ == "__main__":
    logging.info(f"Task 2: API health check started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    check_api_health()
    logging.info(f"Task 2: API health check finished at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
