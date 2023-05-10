from fastapi import FastAPI
from api.v1 import accounts
from core.database import Base
app = FastAPI()


app.include_router(accounts.router, tags=['users'], prefix='/api/accounts')

@app.get("/")
def index():
    return {"message":"Welcome to first api"}


