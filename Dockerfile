FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE "/armaTuVaca/settings.py"

WORKDIR /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

# Define environment variable
ENV NAME World

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
