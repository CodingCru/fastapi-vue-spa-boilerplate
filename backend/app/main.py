from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI(
    title="FastAPI Vue SPA Boilerplate",
    description="A minimal FastAPI + Vue 3 SPA boilerplate for rapid application development",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # Vue dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "FastAPI Vue SPA Boilerplate"}

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "fastapi-vue-spa-boilerplate"}

@app.get("/api/health")
async def api_health_check():
    """API health check endpoint."""
    return {"status": "healthy", "api": "v1", "service": "fastapi-vue-spa-boilerplate"}

@app.get("/api/status")
async def get_status():
    """Get service status."""
    return {
        "status": "running",
        "service": "fastapi-vue-spa-boilerplate",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)