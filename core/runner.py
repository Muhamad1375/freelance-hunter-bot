
import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from scrapers.remoteok import get_jobs
from utils.matcher import is_match
from database.db import init_db
from database.db import job_exists, save_job, is_skipped
from bot.bot import send_job, make_id





def run():

    init_db()

    jobs = get_jobs()

    for job in jobs:

        if not is_match(job):
            continue

        if job_exists(job["link"]):
            continue

        job_id = make_id(job["link"])

        
        if is_skipped(job_id):
            continue

        send_job(job)

        save_job(
            job_id,
            job["title"],
            job["link"],
            job["source"]
        )

if __name__ == "__main__":
    run()