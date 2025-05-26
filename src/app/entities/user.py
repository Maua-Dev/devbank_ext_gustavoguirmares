from src.app.errors.entity_errors import ParamNotValidated
import re # to usando pq usei no pi e achei legal para busca e verificar str
from typing import Tuple

class UserData : 
    # padrao da doc
    name = str
    agency = str # p o código n apagar os exemplos (0777) e deixar só 777? ou sou burro?
    account = str
    current_balance = float

    def __init__(self,name:str = None, agency:str = None, account:str = None,current_balance:float = None) : 

        validation_name = self.validate_name(name)
        if not validation_name[0] :
            raise ParamNotValidated("Name", validation_name[1])
        self.name = name

        validation_agency = self.validate_agency(agency)
        if not validation_agency[0] :
            raise ParamNotValidated("Agency", validation_agency[1])
        self.agency = agency
    
        validantion_account = self.validate_account(account)
        if not validantion_account[0] :
            raise ParamNotValidated("Account", validantion_account[1])
        self.account = account
    
        validantion_current_balance = self.validate_current_balance(current_balance)
        if not validantion_current_balance[0] :
            raise ParamNotValidated("Current Balance", validantion_current_balance[1])
        self.current_balance = current_balance

    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        if name is None:
            return (False, "Name is required")
        if type(name) != str:
            return (False, "Name must be a string")
        if len(name) < 3:
            return (False, "Name must be at least 3 characters long")
        return (True, "")
    
    @staticmethod
    def validate_agency(agency:str) -> Tuple[bool,str] :
        if agency is None :
            return (False, "Agency is required")
        if type(agency) != str:
            return (False, "Agency must be a string")
        if not re.fullmatch(r'\d{4}', agency):
            return (False, "Agency must be at least 4 digits")
        return (True, "")
        

    @staticmethod
    def validate_account(account:str) -> Tuple[bool, str] :
        if account is None :
            return (False,"Account is required")
        if type(account) != str:
            return (False, "Account must be a string ")
        if not re.fullmatch(r'\d{5}-\d', account) : # com o -, coisa q n usei no de cima, ele obriga a ter uma string apos o - e consecutivamente ja faz o erro de precisar ter 7 caracteres
            return (False, "Account must be in the format ( xxxxx-x )")
        return (True, "")
      
    @staticmethod
    def validate_current_balance(current_balance: float) -> tuple[bool, str]:
        if current_balance is None:
            return (False, "Current balance is required")
        if type(current_balance) != float:
            return (False, "Current balance must be a float")
        if current_balance < 0:
            return (False, "Current balance must be a positive number")
        return (True, "")
        
