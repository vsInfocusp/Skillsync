from app.repositories.base import BaseRepository
from app.models.user import User
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserUpdate


class UserRepository(BaseRepository[User]):

    def __init__(self):
        super().__init__(User)

    def create(self, db: Session, obj_in: UserCreate) -> User:
        obj = User(
            email=obj_in.email,
            username=obj_in.username,
            hashed_password=obj_in.password,
            is_active=True,
            is_superuser=False,
        )
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def update(self, db: Session, db_obj: User, obj_in: UserUpdate) -> User:
        obj_data = obj_in.model_dump(exclude_unset=True)
        if "password" in obj_data:
            obj_data["hashed_password"] = obj_data.pop("password")
        for field, value in obj_data.items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_user_by_email(self, db: Session, email: str) -> User:
        return db.query(self.model).filter(self.model.email == email).first()
