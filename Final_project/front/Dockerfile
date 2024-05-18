# Stage 1: Build stage
FROM node:14 AS build

WORKDIR /app

COPY package*.json ./

RUN npm install
RUN ln -snf /usr/share/zoneinfo/Asia/Almaty /etc/localtime && echo Asia/Almaty > /etc/timezone

COPY . .

# Stage 2: Production stage
FROM node:14-alpine

WORKDIR /app

COPY --from=build /app /app

EXPOSE 3000

CMD ["npm", "start"]