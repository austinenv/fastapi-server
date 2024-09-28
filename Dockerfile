# import a base image
FROM python:3.11

# create a directory for the app and go to it
WORKDIR /usr/local/fastapi

# copy the requirements file and install the dependencies
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy the source code into the image
COPY src ./src

# setup a user and switch to it
RUN useradd fastapi-user
USER fastapi-user

# start the FastAPI server
CMD ["fastapi", "run", "src/main.py", "--port", "80"]