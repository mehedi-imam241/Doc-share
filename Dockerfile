FROM python:3.12.2

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host=pypi.org --trusted-host=files.pythonhosted.org --user -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 4020

# Use an environment variable to switch between dev and prod
ARG ENVIRONMENT=prod

# Run the command to start uWSGI
CMD if [ "$ENVIRONMENT" = "dev" ] ; then python3 -m uvicorn main:app --host 0.0.0.0 --port 4020 --reload ; else python3 -m uvicorn main:app --host 0.0.0.0 --port 4020 ; fi

#docker build --build-arg ENVIRONMENT=dev -t my-fastapi-app .

#docker build -t my-fastapi-app .