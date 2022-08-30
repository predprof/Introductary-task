FROM python:3

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
EXPOSE 8080
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

CMD ["python", "main.py"]