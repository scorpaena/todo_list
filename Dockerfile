FROM python:3.8.11-alpine3.14

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

#EXPOSE 8000
#CMD ["python3.8", "manage.py", "runserver", "0.0.0.0:8000"]
