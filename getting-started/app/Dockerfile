FROM python:latest
WORKDIR /app/src

#to COPY the remote file at working directory in container
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Now the structure looks like this '/usr/app/src/test.py'


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "./Math.py"]
