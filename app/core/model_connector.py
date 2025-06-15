# app/core/model_connector.py

import asyncio
from typing import List, Dict

async def query_model(endpoint_url: str, prompts: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Simulates querying an LLM endpoint and returns mocked responses.
    Each prompt is paired with a fake model response.
    """
    # Simulate delay like a real API
    await asyncio.sleep(1)

    results = []
    for item in prompts:
        results.append({
            "prompt": item["prompt"],
            "response": f"This is a simulated response for: {item['group']}",
            "category": item["category"],
            "group": item["group"]
        })
    
    return results
