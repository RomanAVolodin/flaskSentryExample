FROM python:3.8
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY app/requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
COPY app/uwsgi.ini /usr/local/etc/uwsgi.ini

CMD uwsgi --ini /usr/local/etc/uwsgi.ini