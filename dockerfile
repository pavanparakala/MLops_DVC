FROM python:3.8-slim-buster
RIN apt update -y && apt install awscli y
WORKDIR /app
I
COPY/app
RUN pip install -r requirements.txt
CMD ["python3", "app.py"]