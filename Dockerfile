FROM python:3.11-alpine

ADD main.py .
ADD requirements.txt .

RUN python -m pip install -r requirements.txt

CMD ["python", "./main.py"]
