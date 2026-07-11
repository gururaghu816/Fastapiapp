import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://postgres:admin123@localhost:5432/student_db"
)

print("DATABASE_URL =", DATABASE_URL)

# Convert PostgreSQL URL to asyncpg URL for SQLAlchemy Async Engine
if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgresql://",
        "postgresql+asyncpg://",
        1
    )

elif DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgres://",
        "postgresql+asyncpg://",
        1
    )


# Supabase PostgreSQL connection
if "supabase.co" in DATABASE_URL:
    # Remove sslmode from URL if present
    DATABASE_URL = DATABASE_URL.split("?")[0]

    engine = create_async_engine(
        DATABASE_URL,
        echo=False,
        connect_args={
            "ssl": "require",
            "prepared_statement_cache_size": 0,
            "statement_cache_size": 0
        }
    )

else:
    # Local PostgreSQL connection
    engine = create_async_engine(
        DATABASE_URL,
        echo=False,
        connect_args={
            "prepared_statement_cache_size": 0,
            "statement_cache_size": 0
        }
    )


# Async database session
SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False
)


# Base class for SQLAlchemy models
Base = declarative_base()


# Dependency for FastAPI routes
async def get_db():
    async with SessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()