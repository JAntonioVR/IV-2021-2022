FROM python:3.8-slim

RUN useradd --create-home iv_app \
&& mkdir -p /app/test

USER iv_app

WORKDIR /home/iv_app
COPY poetry.lock pyproject.toml tasks.py ./

RUN export PATH=$PATH:/home/iv_app/.local/bin \
&&  pip install poetry \
&&  poetry install

WORKDIR /app/test

ENV PATH=$PATH:/home/iv_app/.local/bin 


ENTRYPOINT [ "invoke", "test" ]
