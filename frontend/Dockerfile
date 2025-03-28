FROM node:23.10-bookworm

RUN apt-get update

WORKDIR /app

COPY . .

RUN npm install

CMD ["npm", "run", "dev"]