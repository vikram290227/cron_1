import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def process_data():
    logging.info("Starting data processing task.")
    # Simulated data processing logic
    data = [1, 2, 3, 4, 5]
    processed_data = [x * 2 for x in data]
    logging.info(f"Processed Data: {processed_data}")
    logging.info("Data processing task completed.")

if __name__ == "__main__":
    logging.info(f"Task 1: Data processing started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    process_data()
    logging.info(f"Task 1: Data processing finished at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
