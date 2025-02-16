from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from typing import Union, Dict, Any

from pydantic import ValidationError
from app.logger import logger


class ErrorHandlingMiddleware:
    def __init__(self, app: FastAPI) -> None:
        self.app = app

    async def __call__(self, request: Request, call_next) -> Union[JSONResponse, Any]:
        try:
            return await call_next(request)
        except HTTPException as exc:
            logger.error(f"Http error occurred: {exc}")
            return JSONResponse(
                status_code=exc.status_code,
                content={"detail": exc.detail}
            )
        except ValidationError as exc:
            logger.error(f"Validation error occurred: {exc}")
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"detail": exc.errors()}
            )
        except Exception as exc:
            logger.error(f"Unexpected error occurred: {exc}")
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={"detail": "Internal server error occurred. Please try again later."}
            )


def setup_error_middleware(app: FastAPI) -> None:
    app.middleware("http")(ErrorHandlingMiddleware(app))