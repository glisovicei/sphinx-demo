"""
Basic Python REST API using Flask
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# In-memory data store for demo purposes
items = [
    {"id": 1, "name": "Item 1", "description": "First item", "created_at": datetime.now().isoformat()},
    {"id": 2, "name": "Item 2", "description": "Second item", "created_at": datetime.now().isoformat()}
]

next_id = 3


@app.route('/', methods=['GET'])
def home():
    """Home endpoint with API information"""
    return jsonify({
        "message": "Welcome to the Basic Python REST API",
        "version": "1.0.0",
        "endpoints": {
            "GET /": "API information",
            "GET /api/items": "Get all items",
            "GET /api/items/<id>": "Get item by ID",
            "POST /api/items": "Create new item",
            "PUT /api/items/<id>": "Update item by ID",
            "DELETE /api/items/<id>": "Delete item by ID"
        }
    })


@app.route('/api/items', methods=['GET'])
def get_items():
    """Get all items"""
    return jsonify({
        "success": True,
        "count": len(items),
        "data": items
    })


@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """Get a specific item by ID"""
    item = next((item for item in items if item['id'] == item_id), None)
    
    if item is None:
        return jsonify({
            "success": False,
            "error": "Item not found"
        }), 404
    
    return jsonify({
        "success": True,
        "data": item
    })


@app.route('/api/items', methods=['POST'])
def create_item():
    """Create a new item"""
    global next_id
    
    if not request.json:
        return jsonify({
            "success": False,
            "error": "Request must be JSON"
        }), 400
    
    name = request.json.get('name')
    description = request.json.get('description', '')
    
    if not name:
        return jsonify({
            "success": False,
            "error": "Name is required"
        }), 400
    
    new_item = {
        "id": next_id,
        "name": name,
        "description": description,
        "created_at": datetime.now().isoformat()
    }
    
    items.append(new_item)
    next_id += 1
    
    return jsonify({
        "success": True,
        "message": "Item created successfully",
        "data": new_item
    }), 201


@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    """Update an existing item"""
    item = next((item for item in items if item['id'] == item_id), None)
    
    if item is None:
        return jsonify({
            "success": False,
            "error": "Item not found"
        }), 404
    
    if not request.json:
        return jsonify({
            "success": False,
            "error": "Request must be JSON"
        }), 400
    
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    item['updated_at'] = datetime.now().isoformat()
    
    return jsonify({
        "success": True,
        "message": "Item updated successfully",
        "data": item
    })


@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """Delete an item"""
    global items
    
    item = next((item for item in items if item['id'] == item_id), None)
    
    if item is None:
        return jsonify({
            "success": False,
            "error": "Item not found"
        }), 404
    
    items = [item for item in items if item['id'] != item_id]
    
    return jsonify({
        "success": True,
        "message": "Item deleted successfully"
    })


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        "success": False,
        "error": "Endpoint not found"
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        "success": False,
        "error": "Internal server error"
    }), 500


if __name__ == '__main__':
    # Only use debug mode in development. 
    # Set FLASK_ENV=production for production deployments
    debug_mode = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
