FROM node:14.3.0-alpine3.11

# set workdir
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent 

# add app
COPY src ./src
COPY public ./public

# start app
EXPOSE 3000
CMD ["npm", "start"]
