FROM python:3.9.10-alpine

# prevent creation of *.pyc files
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app
EXPOSE 8080

ADD requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ADD onyx /app/onyx

CMD ["gunicorn", "-b", "0.0.0.0:8080", "onyx.app:app"]