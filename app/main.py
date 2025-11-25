from fastapi import FastAPI
from routes import router
from exceptions import exceptions_devops_api

app = FastAPI()

exceptions_devops_api(app)

app.include_router(router)