FROM python:3.8

RUN useradd --create-home iv_app \
&& mkdir -p /app/test

USER iv_app

WORKDIR /app/test

COPY poetry.lock pyproject.toml /app/test/
RUN export PATH="$PATH:/home/iv_app/.local/bin" \
&&  pip install --upgrade pip \
&&  pip install poetry \
&&  poetry install