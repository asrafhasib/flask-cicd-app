FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --requirement requirements.txt

COPY app.py .

RUN useradd --system --uid 10001 --create-home appuser
USER 10001

EXPOSE 5000

CMD ["python", "app.py"]
