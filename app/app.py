import logging
import os
import random

from flask import Flask, request
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration


app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

sentry_sdk.init(
    dsn=os.getenv('SENTRY_DSN'),
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)


@app.before_request
def before_request():
    request_id = request.headers.get('X-Request-Id')
    if not request_id:
        raise RuntimeError('request id is requred')


@app.route('/')
def index():
    result = random.randint(1, 50)
    app.logger.info(f'Пользователю досталось число {result}')
    return f"Ваше число {result}!"

