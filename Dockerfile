FROM nginx:alpine

# Copy static site generated from mkdocs
COPY ./notes/site /usr/share/nginx/html
