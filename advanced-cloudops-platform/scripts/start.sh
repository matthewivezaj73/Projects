#!/bin/bash

echo "Starting CloudOps Platform..."

cd ../monitoring

docker compose up -d --build

echo "All services are up!"
