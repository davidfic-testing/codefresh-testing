FROM python:3.6.8-alpine3.9
MAINTAINER David Ficociello "davidfic@gmail.com"
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT ["python"]
CMD ["flask-app.py"]
