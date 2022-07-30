import requests
import json
from tests.DataDriven import Library
from pytest import mark

@mark.api
def test_add_multiple_students():
    api_url = "https://thetestingworldapi.com/api/studentsDetails"
    f = open(
        "D:/python/Python-Codes-master/PyCodes/AUTOMATION_UDEMY/pytest0.2/tests/DataDriven/TestCases/DataFile.json")
    json_req = json.loads(f.read())

    obj = Library.Common(
        "D:/python/Python-Codes-master/PyCodes/AUTOMATION_UDEMY/pytest0.2/tests/DataDriven/TestData/TestData.xlsx",
        "Sheet1")

    col = obj.fetch_col_count()
    row = obj.fech_row_count()
    key_list = obj.fetch_key_names()

    for i in range(2, row + 1):
        updated_json_req = obj.update_req_with_data(i, json_req
                                                    , key_list)
        response = requests.post(api_url, updated_json_req)

        print(response.status_code)
        # print(response.text)
        assert response.status_code == 201

@mark.api
def test_maths():
    a = 3
    b = 6
    c = a+b
    assert  c == 9
