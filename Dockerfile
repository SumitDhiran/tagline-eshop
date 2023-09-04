FROM python:3.10-alpine3.13
ENV PYTHONUNBUFFERED=1

WORKDIR /tagline_task

# COPY . .
COPY requirements.txt requirements.txt

#EXPOSE 8000

RUN pip install -r requirements.txt


# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
