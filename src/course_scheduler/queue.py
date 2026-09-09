import os

def broker_url() -> str:
    return os.environ.get("COURSE_SCHEDULER_REDIS_URL", "redis://localhost:6379/0")
