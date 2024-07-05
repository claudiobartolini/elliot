#!/bin/bash

# Root directory of the project
mkdir my_flask_app
cd my_flask_app

# Create main files
touch app.py config.py requirements.txt run.py

# Create instance folder and config file
mkdir instance
touch instance/config.py

# Create main application package
mkdir my_flask_app
cd my_flask_app

# Create __init__.py and core files
touch __init__.py models.py views.py forms.py

# Create static files structure
mkdir -p static/css static/js static/images

# Create templates folder
mkdir templates
touch templates/layout.html templates/index.html

# Create API package
mkdir api
cd api
touch __init__.py datasets.py experiments.py recommendations.py models.py metrics.py
cd ..

# Create utils package
mkdir utils
cd utils
touch __init__.py helper.py
cd ..

# Create migrations directory
mkdir migrations

# Create tests directory
mkdir tests
cd tests
touch __init__.py test_models.py test_views.py
cd ..

echo "Directory structure for Flask application created successfully."

