#schedule app
FROM python:3.12
ENV POETRY_VERSION=1.8.4

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH" 
WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-root --no-dev

COPY main.py models.py database.py producer.py /app/


EXPOSE 4000

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "4000", "--reload"]

