import os
from dotenv import load_dotenv

import uvicorn
from fastapi import FastAPI, status


from api.routers import route
from api.utils.datadase import engine, Base
from api.models import *

load_dotenv()

Base.metadata.create_all(engine)
app = FastAPI()

app.include_router(route)