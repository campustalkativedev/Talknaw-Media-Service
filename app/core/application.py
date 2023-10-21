from contextlib import asynccontextmanager

import sentry_sdk
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.system.views import router as home_router
from app.core.config import settings

# This Redis instance is tuned for durability.




@asynccontextmanager
async def lifespan(api: FastAPI):
    print("Starting Server and connecting all dependencies")

    if not settings.debug:
        sentry_sdk.init(
            dsn=settings.sentry_logger_url,
            # Set traces_sample_rate to 1.0 to capture 100%
            # of transactions for performance monitoring.
            # We recommend adjusting this value in production,
            traces_sample_rate=1.0,
        )

    yield

    print("Closing all resources and shutting down the application")


def get_app():
    api = FastAPI(
        title="Talknaw Media Routes",
        description=(
            "Some random description about the project"
        ),
        version="0.0.1",
        lifespan=lifespan,
    )

    api.include_router(home_router)

    api.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return api
