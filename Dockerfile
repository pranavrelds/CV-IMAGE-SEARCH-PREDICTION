FROM python:3.9
COPY . /image_search

WORKDIR /image_search

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["python","app.py"]