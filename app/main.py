from fastapi import FastAPI
# Change the import to include 'app.' at the start
from app.api.endpoints import router as measurement_router

app = FastAPI(title="Body Measurement AI")

# This links your api folder to the main app
app.include_router(measurement_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "API is online. Go to /docs for testing."}