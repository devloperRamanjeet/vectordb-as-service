# 🧱 Base image (amd64-compatible)
FROM --platform=linux/amd64 python:3.11-slim

# 🔧 Set working directory
WORKDIR /app/backend

# 🧰 Install system packages
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 📦 Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 📁 Copy entire backend project
COPY . .

# 🌐 Expose backend port
EXPOSE 5000

# ⚙️ Entry point
CMD ["python", "app.py"]
