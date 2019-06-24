import requests
import pytest

#pytest API testing for gorest.co.in 
#Tests are written to practice autom
#ated API testing using pytest and r
#equests library of python.

class TestSet_Users(object):
    access_token = "6qcp1ZWsMWR89ws7VRqkKlf84RZScW6qtPQr"
    format = "json"
    test_url = "https://gorest.co.in/public-api/users?"

    def __find_string_in_response(self, rawResponse, searchFor):
        check = True
        responseJSON = rawResponse.json()
        length_responseJSON = len(responseJSON["result"])
        for i in range(0,length_responseJSON,1):
            check =  searchFor in responseJSON["result"][i]["first_name"]
            if check == False:
                return check
        return check

    def test_get_users(self):
        payload = {"format":format,"access-token":self.access_token}
        response = requests.get(self.test_url, params=payload)
        assert response.status_code == 200

    @pytest.mark.parametrize("first_name",["John","Ram","Eleanora"])
    def test_get_a_user(self, first_name):
        payload = {"format":self.format,"access-token":self.access_token,"first_name":first_name}
        response = requests.get(self.test_url, params=payload)
        assert self.__find_string_in_response(response, first_name) == True

    def test_create_a_user(self):
        payload = {"format":self.format,"access-token":self.access_token,"first_name":"test_user", \
            "last_name":"testuser_lastname","email":"test@test.com","gender":"male"}
        response = requests.post(self.test_url, params=payload)
        responseAfter = requests.get(self.test_url, params={"format":self.format, "access-token":self.access_token,"first_name":"test_user"})
        assert self.__find_string_in_response(responseAfter, "test_user")

    def test_create_an_existing_user(self):
        payload = {"format":self.format,"access-token":self.access_token,"first_name":"test_user", \
            "last_name":"testuser_lastname","email":"test_duplicate@test.com","gender":"male"}
        response = requests.post(self.test_url, data=payload)
        responseDuplicate = requests.post(self.test_url, data=payload)
        assert responseDuplicate.status_code == 422

# if __name__ == "__main__":
#     test = TestSet_Users()
#     test.test_get_a_user()
#     pass
