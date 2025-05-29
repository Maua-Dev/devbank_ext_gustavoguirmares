from fastapi.exceptions import HTTPException
import pytest

from src.app.main import get_userData



class Test_Main:
#     def test_get_all_UsersData(self) :
#         response = get_all_usersData()
#         expected_response = {
#           'UsersData': [
#         {'name': 'Gustavo', 'agency': '1234', 'account': '12345-6', 'current_balance': 4000.0},
#         {'name': 'Vitor', 'agency': '4321', 'account': '65432-1', 'current_balance': 0.0},
#         {'name': 'Josefina', 'agency': '2134', 'account': '01234-5', 'current_balance': 12000.0}
#     ]
# }
        # assert type(response) == dict
        # assert response == expected_response
        
    def test_get_userData(self):
      response = get_userData()
      expected_response = {
        'UsersData': [
            {'name': 'Gustavo', 'agency': '1234', 'account': '12345-6', 'current_balance': 4000.0}
        ]
    }
      assert type(response) == dict
      assert response == expected_response




