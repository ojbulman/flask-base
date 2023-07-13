FROM python:3.9

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
        libatlas-base-dev gfortran nginx supervisor

COPY ./requirements.txt /app/requirements.txt
COPY ./config/nginx.conf /etc/nginx/
COPY ./config/flask-site-nginx.conf /etc/nginx/conf.d/
COPY ./config/uwsgi.ini /etc/uwsgi/
COPY ./config/supervisord.conf /etc/
COPY /app /app

RUN pip3 install uwsgi
RUN pip3 install -r /app/requirements.txt
RUN rm /etc/nginx/sites-enabled/default
RUN rm -r /root/.cache

RUN useradd --no-create-home nginx

WORKDIR /app
CMD ["/usr/bin/supervisord"]