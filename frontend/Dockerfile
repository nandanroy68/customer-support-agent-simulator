FROM node:18-alpine

WORKDIR /app

COPY package.json package-lock.json* yarn.lock* pnpm-lock.yaml* ./

RUN if [ -f yarn.lock ]; then yarn install --frozen-lockfile; \
    elif [ -f package-lock.json ]; then npm ci; \
    elif [ -f pnpm-lock.yaml ]; then npm i -g pnpm && pnpm i; \
    else npm i; fi

COPY . .

RUN npm run build || true

EXPOSE 3000

CMD ["npm", "run", "dev"]


