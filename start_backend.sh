#!/bin/bash

docker rm -f blog-backend 2>/dev/null || true

docker run -d \
  --name blog-backend \
  -p 8000:8000 \
  -v "$(pwd):/app" \
  --restart unless-stopped \
  blog-backend
