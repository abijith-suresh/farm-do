from fastapi import FastAPI

from app.api.routes import todo


def create_app() -> FastAPI:
    app = FastAPI(
        title="FARM Todo App",
        version="0.1.0",
        description="A simple Todo backend with FastAPI + MongoDB",
    )
    app.include_router(todo.router)
    return app


app = create_app()
