from fastapi import FastAPI
from app.api.v1 import health as health_v1
from app.api.v2 import health as health_v2

app = FastAPI(title="Skillsync API", version="1.0.0", description="skillsync API")

app.include_router(health_v1.router, prefix="/api/v1")
app.include_router(health_v2.router, prefix="/api/v2")


@app.get("/")
async def root():
    return {"message": "Welcome to Skillsync API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
