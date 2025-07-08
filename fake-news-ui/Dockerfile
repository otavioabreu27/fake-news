FROM node:20-alpine AS builder

WORKDIR /app

COPY . .

# Garante execução sem prompts interativos
RUN npm install -g pnpm && \
    CI=true pnpm install && \
    CI=true pnpm run build

FROM nginx:alpine

COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
