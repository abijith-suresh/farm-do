from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI(
        title="FARM Todo App",
        version="0.1.0",
        description="A simple Todo backend with FastAPI + MongoDB"
    )
    return app

app = create_app()