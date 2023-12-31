FROM python:3.10

WORKDIR /

COPY . .

ENV PYTHONPATH=${PYTHONPATH}:${PWD} 

RUN pip3 install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

CMD [ "python", 'main.py']