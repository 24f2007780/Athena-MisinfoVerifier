from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from src.api.misinformation import router as misinformation_router
from src.api.education import router as education_router
from src.api.endpoints import reports as reports_router

app = FastAPI(title="Athena API", version="1.0.0")

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(misinformation_router, prefix="/api/misinformation", tags=["misinformation"])
app.include_router(education_router, prefix="/api/education", tags=["education"])
app.include_router(reports_router.router, prefix="/api/reports", tags=["reports"])

@app.get("/")
async def root():
    return {"message": "Welcome to Athena API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
