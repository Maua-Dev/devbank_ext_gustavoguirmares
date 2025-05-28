from typing import List
from ..entities.user import UserData
from ..repo.userData_repository_interface import IUserDataRepository


class UserDataRepositoryMock(IUserDataRepository) : 
    UsersData : List[UserData]

    def __init__(self) :
        self.UsersData = [
        UserData('Gustavo', '1234', '12345-6', 4000.0),
        UserData('Vitor', '4321', '65432-1', 0.0), # sobra nada pro soller 
        UserData('Josefina', '2134', '01234-5', 12000.0)
        ] 
    def get_all_usersData(self) -> List[UserData] :
        return  self.UsersData
    
    

