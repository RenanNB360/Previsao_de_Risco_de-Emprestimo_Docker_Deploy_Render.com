FROM python:3.12.7-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app/ /code/app/

CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "8787"]