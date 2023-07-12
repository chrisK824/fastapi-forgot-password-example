import sys

sys.path.append("..")

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from db_models import Base
from database import engine
from routers import users


description = """
An example FastAPI application to demonstrate forgot password flow.
"""


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title='Forgot password example FastAPI app',
    description=description,
    contact={
        "name": "Christos Karvouniaris",
        "email": "christos.karvouniaris247@gmail.com",
        "url": "https://www.linkedin.com/in/chriskarvouniaris/"
    },
    version="1.0.0",
    docs_url="/v1/documentation",
    redoc_url="/v1/redocs",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware, 
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=["*"]
)

app.include_router(users.router)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=9999)
