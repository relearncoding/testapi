from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello World"}

@app.get("/decision")
def read_root():
    return {'1'}

@app.get("/number")
def read_root():
    return {'90'}