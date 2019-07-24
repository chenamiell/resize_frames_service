from sys import platform

import settings
from resize_frames_worker.service import app

CONCURRENCY = '--concurrency=1'
WORKER = 'worker'
A = '-A'
SUFFIX = '-0fair'
SERVICE_NAME = f'{settings.WORKER_NAME}.service'
WIN_OS = 'win32'
POOL = '--pool=solo'


def start():
    argv = [WORKER, CONCURRENCY]
    if platform == WIN_OS:
        argv.append(POOL)
    app.worker_main(argv=argv)


def stop():
    app.close()


if __name__ == '__main__':
    start()