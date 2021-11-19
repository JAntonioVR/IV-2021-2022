FROM python:3.8

RUN useradd --create-home iv_app \
&& mkdir -p /app/test

USER iv_app

COPY poetry.lock pyproject.toml tasks.py /home/iv_app/
WORKDIR /home/iv_app
RUN export PATH=$PATH:/home/iv_app/.local/bin \
&&  pip install --upgrade pip \
&&  pip install poetry \
&&  poetry config virtualenvs.create false \
&&  pip install invoke \
&&  invoke install

WORKDIR /app/test

ENV PATH=$PATH:/home/iv_app/.local/bin 


ENTRYPOINT [ "invoke", "test" ]

# Ejecutar con docker run -it -v `pwd`:/app/test --rm 21f80092f114