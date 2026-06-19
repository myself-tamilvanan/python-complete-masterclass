# Chapter 40: Scheduling with Cron & Airflow
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 09:04:37
# ============================================

import sched
import time
from datetime import datetime

print("--- Scheduling in Python ---")

# -----------------------------------------------
# SECTION 1: Basic Scheduling with sched
# -----------------------------------------------

print("--- sched module (built-in) ---")

scheduler = sched.scheduler(time.time, time.sleep)


def say_hello(name):
    print(f"  [{datetime.now().strftime('%H:%M:%S')}] Hello, {name}!")


# Schedule events
scheduler.enter(1, 1, say_hello, ("Alice",))
scheduler.enter(2, 1, say_hello, ("Bob",))
scheduler.enter(3, 1, say_hello, ("Charlie",))

print("Running scheduler (3 events)...")
scheduler.run()

# -----------------------------------------------
# SECTION 2: APScheduler (pip install apscheduler)
# -----------------------------------------------

print("\n--- APScheduler Example ---")

try:
    from apscheduler.schedulers.background import BackgroundScheduler
    from apscheduler.triggers.cron import CronTrigger
    from apscheduler.triggers.interval import IntervalTrigger

    scheduler = BackgroundScheduler()

    job_run_count = [0]

    def my_job():
        job_run_count[0] += 1
        print(f"  Job ran at {datetime.now().strftime('%H:%M:%S')} (run #{job_run_count[0]})")

    # Run every 2 seconds
    scheduler.add_job(my_job, IntervalTrigger(seconds=2))

    # Run at specific times (cron-style)
    # scheduler.add_job(my_job, CronTrigger(hour=8, minute=30))

    scheduler.start()
    print("  Scheduler started, running for 6 seconds...")
    time.sleep(6)
    scheduler.shutdown()
    print(f"  Total job runs: {job_run_count[0]}")

except ImportError:
    print("  APScheduler not installed. Run: pip install apscheduler")
    print("  Showing equivalent manual implementation:")

    def run_every_n_seconds(func, n, total_time):
        """Simple scheduler without APScheduler."""
        start = time.time()
        count = 0
        while time.time() - start < total_time:
            func()
            count += 1
            time.sleep(n)
        return count

    def task():
        print(f"  Task ran at {datetime.now().strftime('%H:%M:%S')}")

    count = run_every_n_seconds(task, 1, 3)
    print(f"  Task ran {count} times")

# -----------------------------------------------
# SECTION 3: Cron Expression Reference
# -----------------------------------------------

print("\n--- Cron Expression Reference ---")

cron_examples = [
    ("*    *    *    *    *", "Every minute"),
    ("0    *    *    *    *", "Every hour at :00"),
    ("0    8    *    *    *", "Every day at 8:00 AM"),
    ("0    8    *    *    1", "Every Monday at 8:00 AM"),
    ("0    0    1    *    *", "First day of every month"),
    ("*/5  *    *    *    *", "Every 5 minutes"),
    ("0    */6  *    *    *", "Every 6 hours"),
    ("30   23   *    *    *", "Every day at 11:30 PM"),
    ("0    9    *    *    1-5", "Weekdays at 9:00 AM"),
]

print("Cron Expression          | Description")
print("-" * 55)
for expr, desc in cron_examples:
    print(f"{expr:<25} | {desc}")

# -----------------------------------------------
# SECTION 4: Airflow DAG Example (conceptual)
# -----------------------------------------------

print("\n--- Apache Airflow DAG Example ---")

airflow_example = """
# Example Airflow DAG (requires: pip install apache-airflow)
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "gowtham",
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

def extract():
    print("Extracting data from source...")
    return {"records": 1000}

def transform(**context):
    data = context["ti"].xcom_pull(task_ids="extract")
    print(f"Transforming {data['records']} records...")

def load():
    print("Loading data to warehouse...")

with DAG(
    dag_id="etl_pipeline",
    default_args=default_args,
    schedule_interval="@daily",    # Run every day
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:
    t1 = PythonOperator(task_id="extract", python_callable=extract)
    t2 = PythonOperator(task_id="transform", python_callable=transform)
    t3 = PythonOperator(task_id="load", python_callable=load)
    
    t1 >> t2 >> t3  # Define execution order
"""

print("Airflow DAG code structure:")
for line in airflow_example.strip().split("\n")[:15]:
    print(" ", line)
print("  ...")
print("  (Full code shown above as string for reference)")

print("\n" + "=" * 50)
print("Chapter 40 Complete!")
print("=" * 50)
