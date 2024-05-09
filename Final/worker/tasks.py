from worker.worker import celery_worker

@celery_worker.task
def create_application(user_id, data):
    try:
        print('create_application:', user_id, data)
    except Exception as e:
        print(f'{e}')
