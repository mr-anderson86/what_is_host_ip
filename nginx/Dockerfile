FROM nginx:1.21.4-alpine
ARG TAG=null
ENV VERSION=${TAG}
ADD default.conf.template /etc/nginx/conf.d/
ADD index.html script.js /usr/share/nginx/html/
ENV BACKEND_URL="my-host-ip:5000"
ENTRYPOINT ["/bin/sh" , "-c" , "envsubst < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf && exec nginx -g 'daemon off;'"]