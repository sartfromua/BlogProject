FROM python:3.13-slim

WORKDIR /app

# 🧱 Встановлюємо системні пакети, потрібні для mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .

CMD ["uvicorn", "blog.asgi:application", "--host", "0.0.0.0", "--port", "8000", "--reload"]
