#python 3.8 lambda base image
FROM public.ecr.aws/lambda/python:3.8

#copy requirements.txt to the container
COPY requirements.txt ./

#installing dependencies
RUN pip3 install -r requirements.txt

#copy function code to container
COPY app.py ./

#setting your CMD to the handler filename.function name
CMD | "app.handler" |
