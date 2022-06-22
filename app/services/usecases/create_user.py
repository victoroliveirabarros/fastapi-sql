
from app.domain.usecases import CreateUser as CreateUserContract
from app.domain.usecases import CreateUserParams
from app.services.contracts.user_repository_contract import UserRepositoryContract
from app.services.helpers.http import HttpStatus
from app.services.helpers.http.http import HttpResponse


class CreateUser(CreateUserContract):

    def __init__(
        self,
        user_repository: UserRepositoryContract
    ) -> None:
        self.user_repository = user_repository
    
    # def _create_user(
    #     self,
    #     name: str,
    #     last_name: str,
    #     email: str
    # ):
    #     try:
            
    #     except Exception as e:
    #         print(e)
    #         raise Exception(e)
        
    def execute(self, create_user: CreateUserParams) -> HttpResponse:
        try:
            print(create_user)
            self.user_repository.create_user(
                name=create_user.name,
                last_name=create_user.last_name,
                email=create_user.email
            )

            return HttpStatus.created_201({
                'name': create_user.name,
                'last_name': create_user.last_name,
                'email': create_user.email
            })
        except Exception as e:
            print(e)
            return HttpStatus.bad_request_400(e)
        