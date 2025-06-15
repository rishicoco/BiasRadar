from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from app.core.prompt_gen import generate_prompts
from app.core.model_connector import query_model

router = APIRouter()

class AuditRequest(BaseModel):
    model_name: str
    endpoint_url: str
    categories: List[str]

@router.post("/")
async def run_audit(payload: AuditRequest):
    # 1. Generate prompts based on categories
    prompts = generate_prompts(payload.categories)

    # 2. Send prompts to simulated model connector
    results = await query_model(payload.endpoint_url, prompts)

    # 3. Return the responses to the user
    return {
        "model": payload.model_name,
        "tested_categories": payload.categories,
        "results": results
    }
