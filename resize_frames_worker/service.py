from pathlib import Path

import cv2
from celery import Celery

import settings
from resize_frames_flow.resize_frames import resize_image


class CeleryConfig(object):
    """
    Celery Clinet Configuration Class
    """
    CELERY_IGNORE_RESULTS = False
    BROKER_URL = settings.MQ_URL
    CELERY_RESULT_BACKEND = 'amqp'


app = Celery(settings.WORKER_NAME)
app.config_from_object(CeleryConfig)


@app.task(max_retries=3)
def resize_videos_frames_report(image_path):
    print(f'Worker Just Got{image_path}')
    img = MyImage(image_path=image_path)
    try:
        response_json = resize_image(image=img)
    except Exception as e:
        return {'exception': e.__str__()}
    return response_json


class MyImage(object):
    def __init__(self, image_path):
        self.img = cv2.imread(image_path)
        self.__name = Path(image_path).name.split(".")[0]

    def __str__(self):
        return self.__name

