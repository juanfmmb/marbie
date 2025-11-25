from fastapi import FastAPI
from routes.route_devops import router as devops_router
from routes.route_auth import router as auth_router
from exceptions import exceptions_devops_api

app = FastAPI()

exceptions_devops_api(app)

app.include_router(devops_router)
app.include_router(auth_router)