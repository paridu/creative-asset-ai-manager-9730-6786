from fastapi import APIRouter, Depends, HTTPException
from ..agent.interpreter import QueryInterpreter
from ..agent.search_engine import OverlordSearchEngine
import os

router = APIRouter(prefix="/api/v1/search")

# Dependency Injection
def get_search_engine():
    interpreter = QueryInterpreter(api_key=os.getenv("OPENAI_API_KEY"))
    return OverlordSearchEngine(interpreter)

@router.get("/natural-language")
async def search_files(q: str, engine: OverlordSearchEngine = Depends(get_search_engine)):
    """
    Endpoint for the AI Agent search.
    Example: /api/v1/search/natural-language?q=Show me the red logos from May
    """
    try:
        results = await engine.execute_query(q)
        return {
            "status": "success",
            "interpreted_intent": results["plan"],
            "assets": results["results"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))