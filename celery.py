from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)
app = Celery('tasks', broker='redis://localhost:6397/0/')

@app.task
def add(x, y):
    logger.info('Adding {0} + {1}'.format(x, y))
    return x + y

if __name__ == '__main__':
    app.start()