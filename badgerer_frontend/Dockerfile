FROM node:carbon-jessie as build

WORKDIR /app

COPY package*.json /app/

RUN npm install

COPY ./ /app/

RUN npm run build

FROM nginx:1.17.5

COPY --from=build /app/build /usr/share/nginx/html
COPY conf/nginx.conf /etc/nginx/conf.d/default.conf