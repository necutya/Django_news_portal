from apscheduler.schedulers.background import BackgroundScheduler
from .models import Post


def start():
    """ Start a scheduled task every 24 hours using apscheduler module"""
    scheduler = BackgroundScheduler()
    scheduler.add_job(Post.delete_votes, "interval", hours=24)
    scheduler.start()
