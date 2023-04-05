FROM python:latest
COPY requirement.txt /requirement.txt
RUN pip install -r /requirement.txt
COPY square.py /square.py
CMD ["python", "/square.py"]
