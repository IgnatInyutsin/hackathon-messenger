FROM nginx:latest
COPY ./frontend/dist/frontend/ /usr/share/nginx/html/
COPY ./docker/insult-app_instances/dockerfiles/configs/nginx.conf /etc/nginx/conf.d/nginx.conf
