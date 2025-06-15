from fastapi import FastAPI
from app.endpoints import audit

app = FastAPI(title="BiasRadar")

app.include_router(audit.router, prefix="/audit")
