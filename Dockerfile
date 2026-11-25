FROM python:3.12-slim
WORKDIR /app

# Обновляем системные пакеты Debian
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Обновляем pip и setuptools до безопасных версий, ставим зависимости
RUN pip install --no-cache-dir --upgrade "pip>=25.2" "setuptools>=83.0.0" \
    && pip install --no-cache-dir -r requirements.txt \
    && python3 -m pip uninstall -y pip

COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
