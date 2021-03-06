FROM python:3.9.10-alpine AS build

WORKDIR /app

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

ADD requirements.txt .
RUN apk add --no-cache gcc jpeg-dev zlib-dev musl-dev && \
    pip install --upgrade pip && \
    pip install --no-cache-dir wheel && \
    pip install --no-cache-dir -r requirements.txt

FROM python:3.9.10-alpine AS runtime

COPY --from=build /opt/venv /opt/venv
RUN apk add --no-cache jpeg-dev zlib-dev musl-dev

ENV PATH="/opt/venv/bin:$PATH"
ENV HOST 0.0.0.0
ENV PORT 5000

ENV ONYX_HOSTNAME "localhost"
ENV ONYX_LOG_LEVEL "WARNING"
ENV ONYX_ENABLE_REDIS false
ENV ONYX_REDIS_HOST "http://localhost"
ENV ONYX_REDIS_PORT 6379

WORKDIR /app

COPY startup.sh /app
COPY onyx /app/onyx

RUN chmod +x ./startup.sh
ENTRYPOINT ["./startup.sh"]