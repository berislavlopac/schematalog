FROM python:3.10-slim

RUN pip install -U pip pip-tools

WORKDIR /app

COPY pyproject.toml README.md ./
RUN pip-compile --all-extras pyproject.toml && pip-sync -q

COPY reference/ ./reference/
COPY schematalog/ ./schematalog/

EXPOSE 5000

ENTRYPOINT ["uvicorn", "schematalog:app", "--host", "0.0.0.0", "--port", "5000"]

CMD ["--reload", "--log-level", "debug"]
