API Endpoints
=============


Root Endpoint
-------------

- ``**GET /**`` - Get API information and available endpoints.


Items Endpoints
---------------

- ``**GET /api/items**`` - Get all items.
- ``**GET /api/items/<id>**`` - Get a specific item by ID.
- ``**POST /api/items**`` - Create a new item.
- ``**PUT /api/items/<id>**`` - Update an item by ID.
- ``**DELETE /api/items/<id>**`` - Delete an item by ID.


Usage Examples
--------------


Get all items
-------------

.. code-block:: console

    curl http://localhost:5000/api/items


Get a specific item
-------------------

.. code-block:: console

    curl http://localhost:5000/api/items/1


Create a new item
-----------------

.. code-block:: console

    curl -X POST http://localhost:5000/api/items \
        -H "Content-Type: application/json" \
        -d '{"name": "New Item", "description": "A new item description"}'


Update an item
--------------

.. code-block:: console

    curl -X PUT http://localhost:5000/api/items/1 \
        -H "Content-Type: application/json" \
        -d '{"name": "Updated Item", "description": "Updated description"}'


Delete an item
--------------

.. code-block:: console

    curl -X DELETE http://localhost:5000/api/items/1


Response Format
---------------

All responses are in JSON format with the following structure:


Success Response
----------------

.. code-block:: json

    {
        "success": true,
        "data": {},
        "message": "Optional message"
    }


Error Response
--------------

.. code-block:: json

    {
        "success": false,
        "message": "Error message"
    }


Project Structure
-----------------

.. code-block:: text

    sphinx-demo/
    ├── app.py              # Main application file
    ├── config.json         # Configuration file
    ├── requirements.txt    # Python dependencies
    ├── .gitignore         # Git ignore rules
    └── README.md          # This file


Dependencies
------------

- Flask 3.0.0 - Web framework
- Flask-CORS 4.0.0 - CORS support


Development
-----------

The API runs in debug mode by default for development. This enables:
- Auto-reload on code changes
- Detailed error messages
- Debug toolbar

For production deployment, set the environment variable:

.. code-block:: console

    export FLASK_ENV=production
    python app.py


Or use a production WSGI server like gunicorn:

.. code-block:: console

    pip install gunicorn
    gunicorn -w 4 -b 0.0.0.0:5000 app:app


License
-------

MIT License
