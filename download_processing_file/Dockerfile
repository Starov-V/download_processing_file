FROM python:3.9

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt 
WORKDIR /app

CMD [ "python3", "./manage.py", "runserver", "0.0.0.0:8000"]