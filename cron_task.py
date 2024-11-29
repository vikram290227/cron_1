import schedule
import time
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Define the task
def my_cron_task():
    now = datetime.now()
    logging.info(f"Running the cron job task at {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Schedule the task
schedule.every(1).minutes.do(my_cron_task)  # Run every 1 minute
logging.info("Cron job scheduled to run every 1 minute")

# Run the scheduler
try:
    while True:
        logging.info("Scheduler is running...")
        schedule.run_pending()  # Check for pending jobs
        time.sleep(5)           # Sleep to reduce CPU usage
except Exception as e:
    logging.error(f"Error occurred: {e}")
