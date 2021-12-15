FROM python:3.9.7-alpine
WORKDIR /app
ADD . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
ARG TAG=null
ENV VERSION=${TAG}
ENTRYPOINT ["python", "-u", "app.py"]