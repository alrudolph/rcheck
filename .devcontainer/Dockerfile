ARG PYTHON_VERSION=3.11-slim
FROM python:${PYTHON_VERSION} as base

# install poetry
ARG POETRY_VERSION=1.2.2
RUN apt-get -y update && apt-get -y install git
RUN pip install "poetry==${POETRY_VERSION}"
RUN poetry config virtualenvs.in-project true 
