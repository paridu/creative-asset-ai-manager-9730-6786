from sqlalchemy import text
from typing import List
from ..database.session import SessionLocal
from .interpreter import QueryInterpreter

class OverlordSearchEngine:
    def __init__(self, interpreter: QueryInterpreter):
        self.interpreter = interpreter

    async def execute_query(self, user_query: str):
        # 1. Interpret Intent
        plan = self.interpreter.parse_request(user_query)
        
        # 2. Build SQL + Vector Query
        # We use pgvector's <=> operator for cosine distance
        sql_query = """
        SELECT id, filename, original_path, 
               (embedding <=> :vector_query) AS distance
        FROM assets
        WHERE 1=1
        """
        
        params = {}
        
        # Add dynamic filters from the Agent
        if plan.filters.file_types:
            sql_query += " AND extension = ANY(:extensions)"
            params["extensions"] = plan.filters.file_types
            
        if plan.filters.date_after:
            sql_query += " AND created_at >= :start_date"
            params["start_date"] = plan.filters.date_after

        # Logic for the embedding: 
        # In a real setup, we'd call the VisionModel to vectorize plan.semantic_query
        # Here we placeholder the vector retrieval
        params["vector_query"] = "[...vectorized_semantic_query...]" 

        sql_query += " ORDER BY distance ASC LIMIT 20"

        # 3. Fetch from DB
        async with SessionLocal() as session:
            results = await session.execute(text(sql_query), params)
            return {
                "plan": plan,
                "results": results.fetchall()
            }