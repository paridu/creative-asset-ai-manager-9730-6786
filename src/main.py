from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.routes import assets

app = FastAPI(
    title="OVERLORD API",
    description="Backend services for Freelance Digital Asset Management",
    version="0.1.0"
)

# Configure CORS for local development (Designer UI)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(assets.router)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "overlord-api"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)