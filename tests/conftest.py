from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from app.db import Base, get_session
from app.main import app
from app.seed import seed


@pytest.fixture
def session() -> Iterator[Session]:
    """A fresh in-memory database for every test."""
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)
    TestSession = sessionmaker(bind=engine, expire_on_commit=False)
    with TestSession() as s:
        seed(s)
        yield s
    engine.dispose()


@pytest.fixture
def client(session: Session) -> Iterator[TestClient]:
    app.dependency_overrides[get_session] = lambda: session
    # Not using "with TestClient(app)" on purpose: that would run the
    # startup code against the real database file.
    yield TestClient(app)
    app.dependency_overrides.clear()
