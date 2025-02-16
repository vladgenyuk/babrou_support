from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.db import async_session_maker
from app.logger import logger


class DBSessionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        session = async_session_maker()
        request.state.session = session
        try:
            response = await call_next(request)
            await session.commit()
            return response
        except Exception as e:
            logger.error(f"Rollback session: {str(e)[:450]}")
            await session.rollback()
            raise e
        finally:
            await session.close()
