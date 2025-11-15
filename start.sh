#!/bin/bash
# Start the MCP Core server

PORT="${PORT:-8000}"
echo "Starting MCP Core server on port $PORT..."
uvicorn main:app --host 0.0.0.0 --port $PORT --reload
