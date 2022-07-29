from functools import reduce

from pytest import fixture
from pytest import mark
import json
import requests

base_url = "https://reqres.in"


@mark.api
def test_getApi():
    uri = "/api/users/2"
    response = requests.get(base_url + uri)
    resp = json.loads(response.text)
    print(resp)
    assert response.status_code == 200
    assert resp["data"]["id"] == 2
    assert resp["data"]["email"] == "janet.weaver@reqres.in"
    assert resp["data"]["first_name"] == "Janet"
    assert resp["data"]["last_name"] == "Weaver"



# if __name__ == '__main__':
    # test_getApi()

arr = [8,9,5,16,2,4,21,30,11]
evenArr = list(filter(lambda no : (no%2==0), arr))
print(evenArr)
ModArray = list(map(lambda no : no**2,evenArr))
print((ModArray))
sum = reduce(lambda a,b : a+b,ModArray)
print(sum)
