FROM python:3.10

RUN mkdir wd
WORKDIR wd
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./ ./

CMD ["gunicorn", "--workers=5", "--threads=1", "-b 0.0.0.0:80", "app:server", "--timeout=120"]
