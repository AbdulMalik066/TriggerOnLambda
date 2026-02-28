FROM nginx:alpine
COPY calculator.html /usr/share/nginx/html/index.html
EXPOSE 80
