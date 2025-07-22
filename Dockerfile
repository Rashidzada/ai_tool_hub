# Use a stable Python version
FROM python:3.13.3

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .

# Collect static files (if needed for production)
RUN python manage.py collectstatic --noinput || true

# Default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
