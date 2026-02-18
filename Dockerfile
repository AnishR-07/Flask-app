FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
build-essential \
curl \
&& rm -rf var/lib//apt/lists*

COPY . .

RUN pip install flask mysql-connector-python

EXPOSE 5000

CMD ["python" "flask-app.py"]

