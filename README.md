# Basic Python REST API

A simple REST API built with Flask that demonstrates CRUD operations for managing items.

## Features

- RESTful API endpoints
- CRUD operations (Create, Read, Update, Delete)
- JSON request/response format
- CORS enabled
- Error handling
- In-memory data storage

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/glisovicei/sphinx-demo.git
cd sphinx-demo
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the API

Start the server:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### Root Endpoint
- **GET /** - Get API information and available endpoints

### Items Endpoints
- **GET /api/items** - Get all items
- **GET /api/items/<id>** - Get a specific item by ID
- **POST /api/items** - Create a new item
- **PUT /api/items/<id>** - Update an item by ID
- **DELETE /api/items/<id>** - Delete an item by ID

## Usage Examples

### Get all items
```bash
curl http://localhost:5000/api/items
```

### Get a specific item
```bash
curl http://localhost:5000/api/items/1
```

### Create a new item
```bash
curl -X POST http://localhost:5000/api/items \
  -H "Content-Type: application/json" \
  -d '{"name": "New Item", "description": "A new item description"}'
```

### Update an item
```bash
curl -X PUT http://localhost:5000/api/items/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Item", "description": "Updated description"}'
```

### Delete an item
```bash
curl -X DELETE http://localhost:5000/api/items/1
```

## Response Format

All responses are in JSON format with the following structure:

### Success Response
```json
{
  "success": true,
  "data": {...},
  "message": "Optional message"
}
```

### Error Response
```json
{
  "success": false,
  "error": "Error message"
}
```

## Project Structure

```
sphinx-demo/
├── app.py              # Main application file
├── config.json         # Configuration file
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Dependencies

- Flask 3.0.0 - Web framework
- Flask-CORS 4.0.0 - CORS support

## Development

The API runs in debug mode by default when started with `python app.py`. This enables:
- Auto-reload on code changes
- Detailed error messages
- Debug toolbar

For production deployment, set `DEBUG=False` in the configuration.

## License

MIT License
