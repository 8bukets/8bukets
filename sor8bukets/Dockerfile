FROM node:18-alpine

WORKDIR /app

COPY package.json ./
RUN npm install

COPY src/ ./src/
COPY wrangler.toml ./

# Expose the default port wrangler dev uses (8787)
EXPOSE 8787

# Use wrangler dev to run the worker locally, bound to 0.0.0.0 so the tunnel can reach it
CMD ["npm", "run", "dev", "--", "--ip", "0.0.0.0", "--port", "8787"]
