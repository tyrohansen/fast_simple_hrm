from fastapi import FastAPI
from api.v1 import accounts

app = FastAPI()


app.include_router(accounts.router, tags=['Notes'], prefix='/api/accounts')

@app.get("/")
def index():
    return {"message":"Welcome to first api"}


