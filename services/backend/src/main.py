from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .database.database import engine
from .database.database import Base


Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:8080'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/')
async def home():
    return 'Hello, World!'


@app.get('/seats')
async def awailable_seats():
    return 