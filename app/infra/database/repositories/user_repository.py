
from app.domain.models import User
from app.services.contracts import UserRepositoryContract


class UserRepository(UserRepositoryContract): 

    def __init__(self, db_instance):
        self._db = db_instance

    def create_user(
        self,
        name: str,
        last_name: str,
        email: str
    ) -> User:
        print(name, last_name, email)
        db_user = User(
            name=name,
            last_name=last_name,
            email=email
        )

        self._db.session.add(db_user)
        self._db.session.commit()
        return db_user
