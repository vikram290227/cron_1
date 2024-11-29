import schedule
import time
from datetime import datetime

#Task
def my_cron_task():
    now = datetime.now()
    print(f"Running the cron job task at {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Schedule
schedule.every(1).minutes.do(my_cron_task)  # Runs every 1 min


# Run schedule
print("Starting the cron job...")
while True:
    schedule.run_pending()  
    time.sleep(5)  
