FROM python:3.12

WORKDIR /app

COPY pyproject.toml ./

RUN pip install poetry && poetry install

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0"]
