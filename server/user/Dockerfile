FROM python:3.12
ENV POETRY_VERSION=1.8.4

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"
WORKDIR /app

COPY server/user/pyproject.toml server/user/poetry.lock /app/
RUN poetry install --no-root --no-dev

COPY server/dbSettings/* /app/
COPY server/user/main.py /

EXPOSE 8000

# ENTRYPOINT [ "poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--reload" ]
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

