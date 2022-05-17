# Import latest python3 docker image
FROM python:3

# Install git
RUN apt-get -y update
RUN apt-get -y install git

# Clone github repository
RUN git clone https://github.com/blastomussa/Password-Generator-Api.git /generator/
WORKDIR /generator

RUN pip3 install --no-cache-dir -r requirements.txt

CMD [ "python3", "./app.py" ]
