#!/bin/bash
# Simple test script to verify the API is working

API_URL="${1:-http://localhost:8000}"

echo "Testing MCP Core API at $API_URL"
echo "================================"
echo ""

# Test 1: Health check
echo "1. Testing health check..."
response=$(curl -s "$API_URL/health")
if echo "$response" | grep -q "healthy"; then
    echo "✓ Health check passed"
else
    echo "✗ Health check failed"
    exit 1
fi
echo ""

# Test 2: Root endpoint
echo "2. Testing root endpoint..."
response=$(curl -s "$API_URL/")
if echo "$response" | grep -q "MCP Core API"; then
    echo "✓ Root endpoint passed"
else
    echo "✗ Root endpoint failed"
    exit 1
fi
echo ""

# Test 3: Create a card
echo "3. Testing card creation..."
response=$(curl -s -X POST "$API_URL/cards/" \
  -H "Content-Type: application/json" \
  -d '{"title":"Test Card","content":"Test content","metadata":{"tag":"test"}}')
if echo "$response" | grep -q "Test Card"; then
    echo "✓ Card creation passed"
    card_id=$(echo "$response" | python3 -c "import sys, json; print(json.load(sys.stdin)['id'])" 2>/dev/null || echo "1")
else
    echo "✗ Card creation failed"
    exit 1
fi
echo ""

# Test 4: Get cards
echo "4. Testing card retrieval..."
response=$(curl -s "$API_URL/cards/")
if echo "$response" | grep -q "Test Card"; then
    echo "✓ Card retrieval passed"
else
    echo "✗ Card retrieval failed"
    exit 1
fi
echo ""

# Test 5: Create an event
echo "5. Testing event creation..."
response=$(curl -s -X POST "$API_URL/events/" \
  -H "Content-Type: application/json" \
  -d '{"name":"Test Event","description":"Test description","event_type":"test"}')
if echo "$response" | grep -q "Test Event"; then
    echo "✓ Event creation passed"
else
    echo "✗ Event creation failed"
    exit 1
fi
echo ""

echo "================================"
echo "All tests passed! ✓"
