# -------- 1. Build Stage --------
    FROM node:18-bookworm-slim AS builder

    WORKDIR /app
    
    # Install dependencies for native modules
    RUN apt-get update && apt-get install -y \
      python3 make g++ \
      && rm -rf /var/lib/apt/lists/*
    
    # Copy repo
    COPY . .
    
    # Install dependencies
    RUN yarn install --frozen-lockfile
    
    # Build backend + frontend
    RUN yarn build:all
    
    # -------- 2. Runtime Stage --------
    FROM node:18-bookworm-slim
    
    WORKDIR /app
    
    # Install only runtime deps
    RUN apt-get update && apt-get install -y \
      python3 \
      && rm -rf /var/lib/apt/lists/*
    
    # Copy built app from builder
    COPY --from=builder /app .
    
    # Set production env
    ENV NODE_ENV=production
    
    # Expose Backstage port
    EXPOSE 7007
    
    # Start backend (serves UI + API)
    CMD ["node", "packages/backend", "--config", "app-config.yaml"]