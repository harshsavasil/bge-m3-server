# --------- requirements ---------
FROM python:3.11 AS requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes


# final image build
FROM python:3.11

# Install dev utilities
RUN apt-get update
RUN apt-get install -y vim

#It creates a working directory(app) for the Docker image and container
WORKDIR /bge-m3-server

#It copies the framework and the dependencies for the FastAPI application into the working directory
COPY --from=requirements-stage /tmp/requirements.txt /bge-m3-server/requirements.txt

#It will install the framework and the dependencies in the `requirements.txt` file in our Docker image and container.
RUN pip install --no-cache-dir --upgrade -r /bge-m3-server/requirements.txt

#It will copy the remaining files and the source code from the host `fast-api` folder to the `app` container working directory
COPY . .

# -------- replace with comment to run with gunicorn --------
CMD ["python", "server.py"]
