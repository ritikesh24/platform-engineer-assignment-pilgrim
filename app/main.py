import logging
import os

import psycopg2
from fastapi import FastAPI
from fastapi.responses import JSONResponse


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)

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
        logger.error(
            "Database health check failed: %s",
            exc
        )

        return JSONResponse(
            status_code=503,
            content={
                "status": "unhealthy",
                "database": "unavailable"
            }
        )