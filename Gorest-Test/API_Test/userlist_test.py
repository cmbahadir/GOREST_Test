import requests
import pytest
import yaml

class TestSet_Users(object):
    """
    Test Set for testing users functionality of https://gorest.co.in
    """
    format = "json"
    test_url = "https://gorest.co.in/public-api/users?"
    
    def __find_string_in_response(self, rawResponse, searchFor):
        """
        Test Helper method to find a specific string in the response body.
        """
        check = True
        if "result" not in rawResponse:
            check = False
        else:
            responseJSON = rawResponse.json()
            length_responseJSON = len(responseJSON["result"])
            for i in range(0,length_responseJSON,1):
                check =  searchFor in responseJSON["result"][i]["first_name"]
                if check == False:
                    return check
        return check

    def setup_method(self):
        settingsFile = open("Test_Settings.yaml", "r")
        setting = yaml.safe_load(settingsFile)
        self.access_token = setting["api_key"]

    #Test-1
    def test_get_users(self):
        """
        First Case : To get users from https::/gorest.co.in/public-api/users
        """
        payload = {"format":format,"access-token":self.access_token}
        response = requests.get(self.test_url, params=payload)
        assert response.status_code == 200

    #Test-2
    @pytest.mark.parametrize("first_name",["John","Ram","Eleanora"])
    def test_get_a_user(self, first_name):
        """
        Second Case : List all users containing "John" , "Ram", "Eleanora"
        """
        payload = {"format":self.format,"access-token":self.access_token,"first_name":first_name}
        response = requests.get(self.test_url, params=payload)
        assert self.__find_string_in_response(response, first_name) == True

    #Test-3
    def test_create_a_user(self):
        """
        Third Case : Create a user by specifying first_name, last_name, email, gender
        """
        payload = {"format":self.format,"access-token":self.access_token,"first_name":"test_user", \
            "last_name":"testuser_lastname","email":"test@test.com","gender":"male"}
        response = requests.post(self.test_url, params=payload)
        responseAfter = requests.get(self.test_url, params={"format":self.format, "access-token":self.access_token,"first_name":"test_user"})
        assert self.__find_string_in_response(responseAfter, "test_user")

    #Test-4
    def test_create_an_existing_user(self):
        """
        Fourth Case : Try to create an existing user - Expected Return Code: 422
        """
        payload = {"format":self.format,"access-token":self.access_token,"first_name":"test_user", \
            "last_name":"testuser_lastname","email":"test_duplicate@test.com","gender":"male"}
        response = requests.post(self.test_url, data=payload)
        responseDuplicate = requests.post(self.test_url, data=payload)
        assert responseDuplicate.status_code == 422
