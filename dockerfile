FROM python:3.10

WORKDIR /app

# Копируем зависимости
COPY user-custom-sys/requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY user-custom-sys /app

EXPOSE 8000

CMD ["uvicorn", "ucs.main:app", "--host", "0.0.0.0", "--port", "8000"]
