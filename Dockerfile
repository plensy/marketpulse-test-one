FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONPATH=/app/src
ARG VERSION=dev
ENV APP_VERSION=$VERSION
EXPOSE 8050
CMD ["gunicorn", "-b", "0.0.0.0:8050", "marketpulse.app:server"]