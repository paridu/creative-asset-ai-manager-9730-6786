from fastapi import FastAPI
from .api import search_router

app = FastAPI(title="OVERLORD AI Agent Backend")

# Include Routers
app.include_router(search_router.router)

@app.get("/health")
def health_check():
    return {"status": "operational", "agent": "ready"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)