from fastapi import FastAPI

from app.core.database import database

def create_app() -> FastAPI:
    app = FastAPI(
        title="FARM Todo App",
        version="0.1.0",
        description="A simple Todo backend with FastAPI + MongoDB"
    )
    return app

app = create_app()

@app.get("/ping-db")
async def ping_db():
    try:
        await database.command("ping")
        return {"message": "Database connection OK!"}
    except Exception as e:
        return {"error": str(e)}