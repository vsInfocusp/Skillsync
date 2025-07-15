from app.core.database import SessionLocal
from app.services.user_service import UserService


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def user_service() -> UserService:
    return UserService()
