from typing import List, Optional
from ..entities.user import UserData
from ..repo.userData_repository_interface import IUserDataRepository


class UserDataRepositoryMock(IUserDataRepository) : 
    UsersData : List[UserData]

    def __init__(self) :
        self.UsersData = [
        UserData('Gustavo', '1234', '12345-6', 4000.0),
        # UserData('Vitor', '4321', '65432-1', 0.0), # sobra nada pro soller 
        # UserData('Josefina', '2134', '01234-5', 12000.0)
        ] 
    def get_usersData(self):
        return self.UsersData
    
    def get_userData(self):
        return self.UsersData

    
    def get_userData_by_name(self, name: str) -> Optional[UserData]:
        for user in self.UsersData:
            if user.name == name:
                return user
        return None

    # def get_userData_by_agency_and_account(self, agency: str, account: str) -> Optional[UserData]:
    #     for user in self.UsersData:
    #         if user.agency == agency and user.account == account: #mudei para and pq lembrei q n é uma agencia para cada usuáriokkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk
    #             return user
    #     return None 

    # def get_current_balance(self, agency: str, account: str) -> Optional[float]:
    #     for user in self.UsersData:
    #         if user.agency == agency or user.account == account:
    #             return user.current_balance
    #     return None