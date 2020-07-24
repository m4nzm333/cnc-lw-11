FROM node:12
# Masuk ke app directory
WORKDIR /usr/src/app
# install dependencies
COPY package*.json ./
RUN npm install
# Copy semua source code ke dalam container
COPY . .
# Informasikan bahwa listen ke port 8080
EXPOSE 8080
# Jalankan app
CMD [ "node", "server.js" ]