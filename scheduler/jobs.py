from core.runner import run
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

scheduler.add_job(run, 'interval', minutes=15)

print("Scheduler started...")
scheduler.start()