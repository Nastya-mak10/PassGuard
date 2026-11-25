FROM python:3.12-slim
WORKDIR /app

# Обновляем системные пакеты Debian (закрывает уязвимости ОС)
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Обновляем pip и ставим зависимости (закрывает уязвимости Python)
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
