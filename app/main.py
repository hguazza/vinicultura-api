from fastapi import FastAPI
from app.api.routes import commercialization_router


app = FastAPI()

# Define a simple root endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(commercialization_router)