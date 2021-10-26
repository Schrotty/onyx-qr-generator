FROM node:17-alpine

ADD package.json /app/package.json
ADD app.js /app/app.js

WORKDIR /app

RUN npm install express --save

CMD ["node", "app.js"]

EXPOSE 8080
