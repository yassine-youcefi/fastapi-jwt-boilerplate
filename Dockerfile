# Use an official Python runtime as a parent image
FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --upgrade pip

RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt

COPY . /code/

EXPOSE 80

# Run uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]