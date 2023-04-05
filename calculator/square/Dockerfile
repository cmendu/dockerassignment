FROM python:latest
COPY requirement.txt /requirement.txt
RUN pip install -r /requirement.txt
COPY cube.py /cube.py
CMD ["python", "/cube.py"]
