# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Start the API
uvicorn backend.main:app --reload

# Start the database
docker compose up -d

# Run a migration after model changes
alembic revision --autogenerate -m "describe the change"
alembic upgrade head

# Other alembic commands
alembic downgrade -1      # roll back one migration
alembic current           # show applied revision
```

## Architecture

Spring Boot-style layered architecture. Each domain has four files that follow a strict dependency direction:

```
routers/ → services/ → repositories/ → database.py
```

- **`backend/routers/<domain>_router.py`** — HTTP only. Declares `APIRouter`, injects the service via `Depends`, maps request/response models. No business logic.
- **`backend/services/<domain>_service.py`** — Business logic. Raises `HTTPException` for domain errors (e.g. 404). Injects repository via `Depends`.
- **`backend/repositories/<domain>_repo.py`** — DB access only. Injects `Session` via `Depends(get_session)`. No HTTP concerns.
- **`backend/models/<domain>_models.py`** — SQLModel table definitions. `table=True` classes are the ORM entities.
- **`backend/schemas/<domain>.py`** — Request/response Pydantic schemas kept separate from table models when there is a meaningful difference (e.g. `OrderRead` includes nested `items`).

Routers are registered in `backend/main.py` via `app.include_router(...)`.

## Dependency injection

FastAPI resolves the full chain per request using `Depends(ClassName)` — analogous to Spring's `@Autowired`:

```
Router → Depends(PaymentService)
           PaymentService → Depends(PaymentRepository)
                              PaymentRepository → Depends(get_session)
```

## Key conventions

- Repository file suffix: `_repo.py`, class suffix: `Repository`
- Service file suffix: `_service.py`, class suffix: `Service`
- Router file suffix: `_router.py`, variable name: `router`
- Model schemas follow the `Base / Table / Create / Read / Update` pattern (see `payment_models.py`)
- Custom SQL queries live in the repository layer using `session.exec(text(...))`
- `alembic/env.py` reads `DATABASE_URL` from the environment (via `.env`) and imports `backend.models.*` so autogenerate detects all table changes
- Default DB connection: `postgresql://postgres:postgres@localhost:5432/fastapi_sandbox` (override via `DATABASE_URL` in `.env`)
