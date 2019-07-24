FROM python:alpine
COPY . /src
WORKDIR /src
RUN pip install  --index-url https://pypi.python.org/simple/ -r requirements.txt
CMD python /src/resize_frames_worker_celery.py
