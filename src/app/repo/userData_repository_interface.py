from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from ..entities.user import UserData


class IUserDataRepository (ABC) : 

    @abstractmethod
    def get_all_usersData(self) -> List[UserData] :
        """
        Return all usersData in the database 

        """
        pass 

    
