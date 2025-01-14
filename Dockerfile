FROM python:3.12-slim

# Add user app
RUN python -m pip install -U pip
RUN adduser -uid 2001 app
USER app

# install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /home/app

# set environment varibles
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONHASHSEED random
ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on



COPY --chown=app:app pyproject.toml .
COPY --chown=app:app uv.lock .


RUN uv sync --frozen
RUN uv add gunicorn

COPY --chown=app:app . .
RUN chmod +x ./start_web.sh
RUN chmod +x ./start_api.sh

EXPOSE 8000
