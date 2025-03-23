FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# Run migrations before starting the server
CMD python manage.py makemigrations && python manage.py migrate && gunicorn --bind 0.0.0.0:8000 myproject.wsgi