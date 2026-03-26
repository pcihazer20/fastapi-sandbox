# FastAPI Sandbox

A FastAPI application with SQLModel, PostgreSQL, and Alembic migrations demonstrating full CRUD operations for a `Payment` resource.

## Stack

- **FastAPI** – web framework
- **SQLModel** – ORM (wraps SQLAlchemy + Pydantic)
- **PostgreSQL** – database
- **Alembic** – database migrations
- **psycopg2** – PostgreSQL driver

## Project structure

```
fastapi-sandbox/
├── alembic/                # Alembic migration environment
│   ├── versions/           # Generated migration scripts
│   └── env.py
├── alembic.ini             # Alembic config
├── backend/
│   ├── __init__.py
│   ├── database.py         # Engine, session dependency
│   ├── main.py             # FastAPI app + routes
│   ├── models.py           # SQLModel table & schema models
│   └── enums/
│       └── payment_types.py
├── .env.example
├── pyproject.toml
└── requirements.txt
```

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure the database

Copy `.env.example` to `.env` and update the connection string:

```bash
cp .env.example .env
```

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/fastapi_sandbox
```

### 3. Create the database

```bash
createdb fastapi_sandbox
```

### 4. Run migrations

```bash
# Generate the initial migration (autogenerate from models)
alembic revision --autogenerate -m "create payment table"

# Apply migrations
alembic upgrade head
```

### 5. Start the server

```bash
uvicorn backend.main:app --reload
```

The API will be available at `http://localhost:8000`.
Interactive docs: `http://localhost:8000/docs`

---

## API endpoints

### Payments CRUD

| Method   | Path                    | Description               |
|----------|-------------------------|---------------------------|
| `POST`   | `/payments`             | Create a payment          |
| `GET`    | `/payments`             | List payments             |
| `GET`    | `/payments/{id}`        | Get a single payment      |
| `PATCH`  | `/payments/{id}`        | Partially update a payment|
| `DELETE` | `/payments/{id}`        | Delete a payment          |

### Custom SQL

| Method | Path                      | Description                                      |
|--------|---------------------------|--------------------------------------------------|
| `GET`  | `/payments/stats/by-type` | Total/avg amount grouped by type (raw SQL query) |

---

## Example requests

**Create a payment**
```bash
curl -X POST http://localhost:8000/payments \
  -H "Content-Type: application/json" \
  -d '{"amount": 150.00, "currency": "USD", "type": "ACH", "payer": "Alice", "payee": "Bob"}'
```

**List payments**
```bash
curl http://localhost:8000/payments
```

**Stats by type (custom SQL)**
```bash
curl http://localhost:8000/payments/stats/by-type
```

---

## Alembic cheatsheet

```bash
# Create a new migration (autogenerate detects model changes)
alembic revision --autogenerate -m "description"

# Apply all pending migrations
alembic upgrade head

# Roll back one step
alembic downgrade -1

# Show current revision
alembic current

# Show migration history
alembic history
```
