from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#import io
import random
#import os
#from fastapi.responses import StreamingResponse

app = FastAPI()

origins = [
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    # "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def sample():
    return {'message': 'Hello World'}

@app.get('/check')
async def check(url : str=None):
    #print(url)
    return {"choice": random.choice([0,1])}
    
