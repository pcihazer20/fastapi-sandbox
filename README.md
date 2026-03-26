# FastAPI Sandbox

A FastAPI application with SQLModel, PostgreSQL, and Alembic migrations demonstrating full CRUD operations for `Payment` and `Order` resources, following a Spring Boot-style layered architecture.

## Stack

- **FastAPI** – web framework
- **SQLModel** – ORM (wraps SQLAlchemy + Pydantic)
- **PostgreSQL** – database
- **Alembic** – database migrations
- **psycopg2** – PostgreSQL driver
- **Docker Compose** – local database

## Project structure

```
fastapi-sandbox/
├── alembic/                    # Alembic migration environment
│   ├── versions/               # Generated migration scripts
│   └── env.py
├── alembic.ini
├── backend/
│   ├── main.py                 # App entry point, router registration
│   ├── database.py             # Engine, session dependency
│   ├── enums/
│   │   └── payment_types.py
│   ├── models/
│   │   ├── payment_models.py   # Payment table + schemas
│   │   └── order_models.py     # Order / OrderItem tables + schemas
│   ├── schemas/
│   │   └── orders.py           # Order request/response schemas
│   ├── repositories/
│   │   ├── payment_repo.py
│   │   └── order_repo.py
│   ├── services/
│   │   ├── payment_service.py
│   │   └── order_service.py
│   └── routers/
│       ├── payment_router.py
│       └── order_router.py
├── docker-compose.yml
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

```bash
cp .env.example .env
```

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/fastapi_sandbox
```

### 3. Start the database

```bash
docker compose up -d
```

### 4. Run migrations

```bash
alembic revision --autogenerate -m "initial"
alembic upgrade head
```

### 5. Start the server

```bash
fastapi dev backend/main.py
```

The API will be available at `http://localhost:8000`.
Interactive docs: `http://localhost:8000/docs`

---

## API endpoints

### Payments

| Method   | Path                        | Description                              |
|----------|-----------------------------|------------------------------------------|
| `POST`   | `/payments`                 | Create a payment                         |
| `GET`    | `/payments`                 | List payments (`skip`, `limit` params)   |
| `GET`    | `/payments/{id}`            | Get a single payment                     |
| `PATCH`  | `/payments/{id}`            | Partially update a payment               |
| `DELETE` | `/payments/{id}`            | Delete a payment                         |
| `GET`    | `/payments/stats/by-type`   | Totals and averages grouped by type (raw SQL) |

### Orders

| Method | Path          | Description       |
|--------|---------------|-------------------|
| `GET`  | `/orders`     | List orders       |
| `POST` | `/orders`     | Create an order   |

---

## Example requests

**Create a payment**
```bash
curl -X POST http://localhost:8000/payments \
  -H "Content-Type: application/json" \
  -d '{"amount": 150.00, "currency": "USD", "type": "ACH", "payer": "Alice", "payee": "Bob"}'
```

**Payment stats by type (raw SQL)**
```bash
curl http://localhost:8000/payments/stats/by-type
```

**Create an order**
```bash
curl -X POST http://localhost:8000/orders \
  -H "Content-Type: application/json" \
  -d '{"description": "Order #1", "total": 75.00, "items": [{"description": "Item A", "amount": 50.00}, {"description": "Item B", "amount": 25.00}]}'
```

---

## Alembic cheatsheet

```bash
# Generate migration from model changes
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
