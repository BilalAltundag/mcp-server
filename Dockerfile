FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .

# MCP server için port (varsayılan: stdio, HTTP için 8000)
EXPOSE 8000

# Server'ı başlat
CMD ["python", "server.py"]