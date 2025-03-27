import requests
import pytest 

def test_get_method():
    url = "https://reqres.in/api/users/2"
    response = requests.get(url)

    assert response.status_code == 200