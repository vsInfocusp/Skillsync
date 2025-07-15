from sqlalchemy.orm import Session
from app.core.security import get_password_hash
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate


class UserService:

    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, db: Session, user_in: UserCreate) -> User:
        user_in.password = get_password_hash(user_in.password)
        return self.user_repository.create(db, user_in)

    def get_user_by_email(self, db: Session, email: str) -> User:
        return self.user_repository.get_user_by_email(db, email)

    def update_user(self, db: Session, db_obj: User, user_in: UserUpdate) -> User:
        if user_in.password:
            user_in.password = get_password_hash(user_in.password)
        return self.user_repository.update(db, db_obj, user_in)
