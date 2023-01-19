FROM python:3.11-slim-bullseye

WORKDIR /project

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "uvicorn", "database_api.app:app", "--host", "0.0.0.0", "--port", "80" ]

EXPOSE 80
