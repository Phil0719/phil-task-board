FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*
COPY . /app/
RUN chmod +x /app/.github/scripts/entrypoint.sh
ENTRYPOINT ["/app/.github/scripts/entrypoint.sh"]
