FROM python:3.11

ADD main.py .
ADD requirements.txt .

RUN python -m pip install -r requirements.txt

CMD ["python", "./main.py"]
