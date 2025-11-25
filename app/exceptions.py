from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as ResponseExetion

def exceptions_devops_api (app: FastAPI):
    @app.exception_handler(ResponseExetion)
    async def exceptions_devops_handler(request: Request, exc: ResponseExetion):
        if exc.status_code == 405:
            return JSONResponse(
                status_code=405,
                content={"error":"ERROR"}
            )
        return JSONResponse(
            status_code=exc.status_code,
            content={"error": exc.detail}
        )