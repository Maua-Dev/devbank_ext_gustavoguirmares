from abc import ABC, abstractmethod
from typing import List, Optional
from ..entities.user import UserData

class IUserDataRepository(ABC):

    @abstractmethod
    def get_userData(self) -> List[UserData]:
        """
        Return all users data in the database

        """
        pass

    @abstractmethod
    def get_userData_by_name(self, name: str) -> Optional[UserData]:
        """
        Return a user by name

        """
        pass

    @abstractmethod
    def get_userData_by_agency_and_account(self, agency: str, account: str) -> Optional[UserData]:
        """
        Return a user by agency and account

        """
        pass

    @abstractmethod
    def get_current_balance(self, agency: str, account: str) -> Optional[float]:
        """
        Returns the balance of the account specified by agency and account number

        """
        pass