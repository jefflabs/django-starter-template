FROM nginx:stable-alpine

# replace the default config with our own config
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

EXPOSE 80