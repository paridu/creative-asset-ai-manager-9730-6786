#!/bin/bash
# Initialize production environment on the target server

set -e

echo "🚀 Initializing OVERLORD Production Environment..."

# 1. Create directory structure
mkdir -p /opt/overlord/{models,nginx}

# 2. Create docker-compose symlink or copy
# Assumes docker-compose.yml is already uploaded via CI/CD or Ansible

# 3. Setup Environment Variables
if [ ! -f .env ]; then
    echo "⚠️ .env file missing! Creating from template..."
    cp .env.example .env
    echo "Please update .env with production secrets."
fi

# 4. Pull and Start
docker compose pull
docker compose up -d

echo "✅ Deployment Successful!"