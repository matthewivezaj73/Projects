#!/bin/bash

echo "Stopping CloudOps Platform..."

cd ../monitoring

docker compose down -v

echo "All services stopped!"
