FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
RUN python -m pip install --no-cache-dir --default-timeout=60 \
    -i https://mirror-pypi.runflare.com/simple \
    -r requirements.txt


COPY . /code/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]