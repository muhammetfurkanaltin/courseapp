# 1. Temel imajı belirleyin
FROM python:3.9-slim

# 2. Çalışma dizinini ayarlayın
WORKDIR /courseApp

# 3. Bağımlılık dosyasını kopyalayın
COPY requirements.txt .

# 4. Bağımlılıkları yükleyin
RUN pip install --no-cache-dir -r requirements.txt

# 5. Uygulama dosyalarını kopyalayın
COPY . .

# 6. Varsayılan komut (Django server için)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]