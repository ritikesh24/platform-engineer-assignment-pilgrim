import os

import psycopg2
from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI(
    title="Platform Engineer Assignment",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "application": "platform-engineer-assignment",
        "status": "running"
    }


@app.get("/health")
def health():
    """
    Application and database health check.

    Returns:
        200 when application and database are healthy.
        503 when database connectivity fails.
    """

    try:
        connection = psycopg2.connect(
            host=os.getenv("DATABASE_HOST"),
            port=os.getenv("DATABASE_PORT", "5432"),
            database=os.getenv("DATABASE_NAME"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            connect_timeout=3
        )

        connection.close()

        return {
            "status": "healthy",
            "database": "connected"
        }

    except Exception as exc:
        return JSONResponse(
            status_code=503,
            content={
                "status": "unhealthy",
                "database": "unavailable"
            }
        )