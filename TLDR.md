# Sales Force Location Tracking System - Quick Start

## Prerequisites
- Docker and Docker Compose
- VS Code (optional, for dev container)

## Quick Start Options

### Option 1: Using Docker Compose
```bash
# Build and start the containers
docker compose build
docker compose up -d

# Run the tests
docker compose exec service pytest
```

### Option 2: Using VS Code Dev Container (Recommended)
1. Install the "Remote - Containers" extension in VS Code
2. Open the project in VS Code
3. Click "Reopen in Container" when prompted
4. Wait for the container to build and start
5. Open a terminal in VS Code and run:
```bash
pytest
```

## Available Endpoints

### List All Sales Reps
```bash
curl http://localhost:3000/api/persons
```

### Get a Specific Sales Rep
```bash
curl http://localhost:3000/api/persons/1
```

### Create a New Sales Rep
```bash
curl -X PUT http://localhost:3000/api/persons \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "John",
    "last_name": "Smith"
  }'
```

### Add a Location Segment (Unimplemented)
```bash
curl -X PUT http://localhost:3000/api/persons/1/segment \
  -H "Content-Type: application/json" \
  -d '{
    "start_date": "2024-03-20T09:00:00Z",
    "end_date": "2024-03-21T17:00:00Z",
    "city": "Chicago",
    "state": "IL",
    "zip_code": "60601"
  }'
```

## Development Features
- Hot reload enabled
- PostgreSQL database
- Python 3.11
- Flask web framework
- SQLAlchemy ORM
- Pytest for testing

## Interview Preparation
1. Review the requirements in `BASIC.md`
2. Identify any unclear requirements or edge cases
3. Prepare questions about:
   - Technical constraints
   - Business rules
   - Edge cases
   - Additional information needed

Note: No implementation is required before the interview. We'll work through the solution together. 