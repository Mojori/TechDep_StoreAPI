from models.models import User
from sqlalchemy import update


class UserRepository:
    def __init__(self, db):
        self.db = db

    def create_user(self, user_name: str) -> User | bool:
        db_user = self.db.query(User).filter(User.name == user_name).first()

        if not db_user:
            db_user = User(name=user_name)
            self.db.add(db_user)
            self.db.commit()
            self.db.refresh(db_user)
            return db_user

        else:
            return False

    def get_all_users(self) -> list[User] | bool:
        db_users = self.db.query(User).all()

        if db_users:
            return db_users

        else:
            return False

    def get_user_by_id(self, user_id: int) -> User | bool:
        db_user = self.db.query(User).filter(User.id == user_id).first()

        if db_user:
            return db_user
        else:
            return False

    def update_user_by_id(self, user_id: int, user_new_name: str) -> User | bool:
        db_user = self.db.query(User).filter(User.id == user_id).first()

        if db_user:
            stmt = (
                update(User).
                where(User.id == user_id).
                values(name=user_new_name)
            )
            self.db.execute(stmt)
            self.db.commit()
            self.db.refresh(db_user)

            return db_user

        else:
            return False

    def delete_user_by_id(self, user_id: int) -> bool:
        db_user = self.db.query(User).filter(User.id == user_id).first()

        if db_user:
            self.db.delete(db_user)
            self.db.commit()
            return True

        else:
            return False
