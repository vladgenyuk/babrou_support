DB_HOST=localhost alembic revision --autogenerate -m "db_init"
DB_HOST=localhost alembic upgrade head

DB_HOST=localhost uvicorn app.main:app --reload

