FROM python3.11:slim-bullseye

WORKDIR /project

COPY backend .

RUN poetry install

ENTRYPOINT [ "uvicorn" ]