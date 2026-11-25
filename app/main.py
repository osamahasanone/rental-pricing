from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db import Base, SessionLocal, engine
from app.routes import orders, products
from app.seed import seed


@asynccontextmanager
async def lifespan(app: FastAPI):
    # No migrations in this small repo: tables are created at startup.
    Base.metadata.create_all(engine)
    with SessionLocal() as session:
        seed(session)
    yield


app = FastAPI(title="Rental Pricing", lifespan=lifespan)
app.include_router(products.router)
app.include_router(orders.router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
