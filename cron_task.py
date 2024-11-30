import logging
from datetime import datetime

# Set up logging to both console and file
log_filename = "cron_task.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # Log to console
        logging.FileHandler(log_filename, mode='a')  # Log to file
    ]
)

# Define the task
def my_cron_task():
    now = datetime.now()
    logging.info(f"Running the cron job task at {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Run the task
try:
    logging.info("Starting the cron job...")
    my_cron_task()  # Execute the task
    logging.info("Cron job completed successfully.")
except Exception as e:
    logging.error(f"Error occurred: {e}")
except KeyboardInterrupt:
    logging.info("Cron job interrupted by user.")
