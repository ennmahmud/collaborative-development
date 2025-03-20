This is the backend repo for the Collaborative Development Module.

Backend
This is the backend repo.

Technologies
Flask (Python)
PostgresSQL
Platform
The application is hosted on Render with a PostgresSQL database and automatic deployment from the main branch on GitHub.

Project Setup
Install required packages
pip install -r requirements.txt
Create .env and .env.local file in the root directory using the .env.example file
cp env.example .env
Create a virtual environment
python3 -m venv .venv
Activate the virtual environment
. .venv/bin/activate
Freeze the requirements (if you install any new package)
pip freeze > requirements.txt
Run the server
flask --app index run
Database
Create a new migration
flask db migrate -m "Description of changes"
Apply migrations
flask db upgrade
Rollback one migration
flask db downgrade
View migration history
flask db history
Current migration status
flask db current
