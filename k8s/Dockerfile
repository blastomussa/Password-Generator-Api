# To build: docker build --no-cache -f Dockerfile . -t blastomussa/flaskappv2
# To test image: docker run -d -p 5001:5000 blastomussa/flaskappv2
# Import latest python3 docker image
FROM python:3.8-slim-bullseye

# Install git
RUN apt-get -y update
RUN apt-get -y install git

# Clone github repository
RUN git clone https://github.com/blastomussa/Password-Generator-Api.git /generator/
WORKDIR /generator

RUN pip3 install --no-cache-dir -r requirements.txt

# This should run on the docker container: http://127.0.0.1:5000
# Expose the required port
EXPOSE 5000

# Must forward port when running container
CMD [ "python3", "./app.py" ]
