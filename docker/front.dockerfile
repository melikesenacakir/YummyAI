FROM node:alpine
WORKDIR /app

COPY package*.json ./

RUN npm install
RUN npm install -g @angular/cli

COPY . .
CMD ["npx", "ng", "serve", "--host", "0.0.0.0"]