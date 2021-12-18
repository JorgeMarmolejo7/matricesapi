from fastapi import FastAPI
from routes.mat import mat


app = FastAPI()

app.include_router(mat)