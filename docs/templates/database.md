# Database Templates and Operations

This document describes the database-related templates and operations available in the Code Generation Library.

## Database Connection Template

The library provides a template for generating database connection code. This template is used by the `setup_database_connection` method of the `CodeGenerator` class.

### Template Location
        templates/database/connection.py

### Usage

```python
from code_gen_lib import CodeGenerator

generator = CodeGenerator('path/to/config.yaml')

db_config = {
    'host': 'localhost',
    'port': 5432,
    'database': 'my_app_db',
    'user': 'db_user',
    'password': 'db_password'
}

generator.setup_database_connection(db_config, 'output/database/connection.py')

Template Content
The connection.py template generates code for establishing a database connection. It supports multiple database types, including PostgreSQL, MySQL, and SQLite. Here's an example of what the generated code might look like for a PostgreSQL database:
import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host="{{ db_config.host }}",
        port="{{ db_config.port }}",
        database="{{ db_config.database }}",
        user="{{ db_config.user }}",
        password="{{ db_config.password }}"
    )
    return conn

    CRUD Operation Templates
The library provides templates for generating CRUD (Create, Read, Update, Delete) operations for database models.
Template Locations

templates/crud/create.py
templates/crud/read.py
templates/crud/update.py
templates/crud/delete.py

## Usage
from code_gen_lib import CodeGenerator

generator = CodeGenerator('path/to/config.yaml')

generator.generate_crud('User', 'output/models')

This will generate four files in the output/models directory:

User_create.py
User_read.py
User_update.py
User_delete.py

Template Content Examples
Create Operation (create.py)

from database.connection import get_db_connection

def create_{{ model_name.lower() }}({{ model_fields | join(', ') }}):
    conn = get_db_connection()
    cur = conn.cursor()
    
    query = """
    INSERT INTO {{ model_name.lower() }}s ({{ model_fields | join(', ') }})
    VALUES ({{ '%s, ' * (model_fields | length - 1) }}%s)
    RETURNING id;
    """
    
    values = ({{ model_fields | join(', ') }})
    
    cur.execute(query, values)
    new_id = cur.fetchone()[0]
    
    conn.commit()
    cur.close()
    conn.close()
    
    return new_id


Read Operation (read.py)
from database.connection import get_db_connection

def get_{{ model_name.lower() }}(id):
    conn = get_db_connection()
    cur = conn.cursor()
    
    query = "SELECT * FROM {{ model_name.lower() }}s WHERE id = %s;"
    
    cur.execute(query, (id,))
    result = cur.fetchone()
    
    cur.close()
    conn.close()
    
    if result:
        return dict(zip([{{ model_fields | join(', ') }}], result))
    else:
        return None

def get_all_{{ model_name.lower() }}s():
    conn = get_db_connection()
    cur = conn.cursor()
    
    query = "SELECT * FROM {{ model_name.lower() }}s;"
    
    cur.execute(query)
    results = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return [dict(zip([{{ model_fields | join(', ') }}], row)) for row in results]

Update Operation (update.py)
from database.connection import get_db_connection

def update_{{ model_name.lower() }}(id, {{ model_fields | join(', ') }}):
    conn = get_db_connection()
    cur = conn.cursor()
    
    query = """
    UPDATE {{ model_name.lower() }}s
    SET {{ model_fields | map('lower') | map('regex_replace', '^(.*)$', '\\1 = %s') | join(', ') }}
    WHERE id = %s;
    """
    
    values = ({{ model_fields | join(', ') }}, id)
    
    cur.execute(query, values)
    updated_rows = cur.rowcount
    
    conn.commit()
    cur.close()
    conn.close()
    
    return updated_rows > 0

Delete Operation (delete.py)
from database.connection import get_db_connection

def delete_{{ model_name.lower() }}(id):
    conn = get_db_connection()
    cur = conn.cursor()
    
    query = "DELETE FROM {{ model_name.lower() }}s WHERE id = %s;"
    
    cur.execute(query, (id,))
    deleted_rows = cur.rowcount
    
    conn.commit()
    cur.close()
    conn.close()
    
    return deleted_rows > 0
    
            