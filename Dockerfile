FROM python:3.9

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
        libatlas-base-dev gfortran nginx supervisor

RUN pip3 install uwsgi

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

RUN useradd --no-create-home nginx

RUN rm /etc/nginx/sites-enabled/default
RUN rm -r /root/.cache

COPY ./config/nginx.conf /etc/nginx/
COPY ./config/flask-site-nginx.conf /etc/nginx/conf.d/
COPY ./config/uwsgi.ini /etc/uwsgi/
COPY ./config/supervisord.conf /etc/
COPY /app /app

WORKDIR /app

CMD ["/usr/bin/supervisord"]