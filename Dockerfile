FROM python:3.11-slim       
WORKDIR /app

COPY . .

# no-cache means do not store the packages in the cache (ensures pip does not store copies in the cache and bloat up the img size in docker)
RUN pip install --no-cache-dir -r requirements.txt

# Flask runs on port 5000
EXPOSE 5000

CMD ["python", "dashboard/app.py"]
