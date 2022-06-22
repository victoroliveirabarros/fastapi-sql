from abc import ABC, abstractmethod

from app.domain.models import User


class UserRepositoryContract(ABC):
    """ User Repository Contract """

    @abstractmethod
    def create_user(
        self,
        name,
        last_name,
        email
    ) -> User:
        raise NotImplementedError()