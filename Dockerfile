FROM python:3.11

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /code

COPY ./requirements.txt .
# RUN apt-get update \
#     && apt-get install -y \
#         netcat-openbsd \
#     && pip install --upgrade pip \
#     && pip install -r requirements/requirements.txt
RUN apt-get update \
    && apt-get install -y \
        netcat-openbsd \
        binutils libproj-dev gdal-bin \
        software-properties-common \
        libgeos++-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN chmod +x /code/entrypoint.sh

COPY . .

ENTRYPOINT ["/code/entrypoint.sh"]