# PostgreSQL Database Creation with Python

This project demonstrates how to create a Postgres database and tables using Python. The script connects to PostgreSQL using `psycopg2`and creates a new database and tables via script, use `.env` variables for database credentials.

## Tech Stack
- Python 3.21+
- PostgreSQL
- psycopg2
- dotenv

## Install dependencies
```bash
pip install psycopg2-binary python-dotenv
```

## Create `.env` file in the root directory
```ini
DB_USER="your-username"
DB_PASSWORD="your-password"
DB_HOST="your-hostname"
DB_NAME="your-database"
DB_PORT="your-port-number"
```

## Run `create_db_tablea.py`
```bash
python create_db_tables.py
```