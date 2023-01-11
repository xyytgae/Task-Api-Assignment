FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    gcc \
    libc6-dev \
 && apt-get -y clean \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /src

COPY pyproject.toml* poetry.lock* ./

RUN pip install --upgrade pip \
 && pip install poetry \
 && if [ -f pyproject.toml ]; then poetry install; fi

ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]
