# fastapi-forgot-password-example
Forgot password example flow with FastAPI

## Installation
- `python3.11 -m venv python_venv`
- `source python_venv/bin/activate`
- `pip install -r requirements.txt`
- `python3.11 main.py`

## Usage
### Create fist admin manually
`INSERT INTO users (email,password,name,surname,register_date,role) VALUES('admin@example.com', '$2b$12$F1e3WBjqa1EMBwy5//FVPujkqUksC2a.JJEqKGy2bYA.tB/lAkhLW', 'Mockname', 'Mocksurname', '2023-04-19', 'ADMINISTRATOR');`
### Endpoints requests
All endpoints can be used by visiting the swagger documentation at `localhost:9999/v1/documentation`