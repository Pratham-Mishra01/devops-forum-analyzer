FROM python:3.11-slim       
WORKDIR /app

COPY scraper/ ./scraper/
COPY analyzer/ ./analyzer/
COPY pipeline.py .
COPY requirements.txt .

# no-cache means do not store the packages in the cache (ensures pip does not store copies in the cache and bloat up the img size in docker)
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "pipeline.py"]
