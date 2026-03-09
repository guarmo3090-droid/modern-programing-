FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
Run pip install pytest


COPY . .

CMD ["python", "app.py"]
