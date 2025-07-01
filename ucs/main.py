from fastapi import FastAPI
from ucs.api.create_project.routes import router as project_router

app = FastAPI(title="Backend monolith")

app.include_router(project_router)