# start by pulling the python image
FROM python:latest

 

# copy the requirements file into the image
COPY ./requirement.txt /root/dockerImage/requirement.txt

 

# switch working directory
WORKDIR /root/dockerImage

 

# install the dependencies and packages in the requirements file
RUN pip install -r requirement.txt

 

# Expose the port
EXPOSE 5000
# copy every content from the local file to the image
COPY . /root/dockerImage/requirement.txt

 

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

 

CMD ["MathCalc.py" ]
