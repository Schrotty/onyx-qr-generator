FROM python:3.9.10-alpine

# prevent creation of *.pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV HOST 0.0.0.0
ENV PORT 5000

WORKDIR /app

ADD requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ADD startup.sh /app
ADD onyx /app/onyx

CMD ["./startup.sh"]