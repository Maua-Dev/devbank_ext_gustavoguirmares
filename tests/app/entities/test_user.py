import pytest
from src.app.errors.entity_errors import ParamNotValidated
from src.app.entities.user import UserData

class Test_user :
    def test_user(self) :
        User = UserData("gustavo", "1234", "12345-6", 4000.0)
        assert User.name == "gustavo"
        assert User.agency == "1234"
        assert User.account == "12345-6"
        assert User.current_balance == 4000.0

    def test_name_is_none(self):
        with pytest.raises(ParamNotValidated):
            UserData("1234", "12345-6", 4000.0)

    def test_name_has_the_minimum_character(self):
        with pytest.raises(ParamNotValidated):
            UserData("g", "1234", "12345-6", 4000.0)

    def test_name_is_str(self) :
        with pytest.raises(ParamNotValidated) :
             UserData(1, "1234", "12345-6", 4000.0)


    def test_agency_is_none(self):
        with pytest.raises(ParamNotValidated):
            UserData("gustavo", "12345-6", 4000.0)

    
    def test_agency_is_str(self) :
        with pytest.raises(ParamNotValidated) :
             UserData("gustavo", 2, "12345-6", 4000.0)

    def test_agency_has_the_minimum_character(self):
        with pytest.raises(ParamNotValidated) :
            UserData("gustavo", "123", "12345-6", 4000.0)

    def test_account_is_none(self) :
        with pytest.raises(ParamNotValidated):
            UserData("gustavo", "123", 4000.0)

    def test_account_is_str(self) :
        with pytest.raises(ParamNotValidated):
            UserData("gustavo", "123", 1 , 4000.0)

    def test_account_has_the_minimum_character(self) :
        with pytest.raises(ParamNotValidated):
            UserData("gustavo", "123", "1234-5" , 4000.0)

    def test_current_balance_is_none(self) :
        with pytest.raises(ParamNotValidated) :
             UserData("gustavo", "123", "12345-6"  )

    def test_current_balance_is_not_float(self) :
        with pytest.raises(ParamNotValidated) :
             UserData("gustavo", "123", "12345-6", 4000 )

    def test_current_balance_is_positive(self) :
        with pytest.raises(ParamNotValidated) :
             UserData("gustavo", "123", "12345-6", -4000.0 )

    def test_to_dict(self) :
        name = "gustavo"
        agency = "1234"
        account = "12345-6"
        current_balance = 4000.0

        userData = UserData(name,agency,account,current_balance )

        UserData_dict = userData.to_dict()

        expected_userData_dict = {
            "name" : name,
            "agency": agency,
            "account" : account, 
            "current_balance" : current_balance
        }

        assert UserData_dict == expected_userData_dict