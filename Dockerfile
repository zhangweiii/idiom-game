FROM python:3.6
WORKDIR /Project/idiom

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.douban.com/simple

COPY . .

# CMD ["gunicorn", "start:app", "-c", "./gunicorn.conf.py"]
CMD ["flask", "run", "-h", "0.0.0.0"]