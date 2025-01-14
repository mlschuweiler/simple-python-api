from http import HTTPStatus
import json

class TestExampleListAPI:

    def test_list_all(self, client):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        expected_response = json.loads("""[{"id": 1, "name": "Batman"}, {"id": 2, "name": "Superman"}, {"id": 3, "name": "Spiderman"}]""")

        response = client.get("/examples/", headers=headers)
        actual_response = json.loads(response.data)

        assert response.status_code == HTTPStatus.OK
        assert expected_response == actual_response

    def test_post_example(self, client):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        expected_response = json.loads("""{"id": 4, "name": "Super-test-user"}""")        

        response = client.post("/examples/", data = """{"name":"Super-test-user"}""", headers = headers)
        actual_response = json.loads(response.data)

        assert response.status_code == 201
        assert expected_response == actual_response

class TestExampleAPI:

    def test_list_specific(self, client):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        expected_response = json.loads("""{"id": 3, "name": "Spiderman"}""")        
        response = client.get("/examples/3", headers=headers)
        actual_response = json.loads(response.data)

        assert response.status_code == HTTPStatus.OK
        assert expected_response == actual_response

    def test_patch_example(self, client):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        expected_response = json.loads("""{"id": 3, "name": "Tom Holland"}""")        

        response = client.patch("/examples/3", data = """{"name": "Tom Holland"}""", headers = headers)
        actual_response = json.loads(response.data)

        assert response.status_code == 200
        assert expected_response == actual_response
    

    def test_post_and_delete_example(self, client):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        expected_post_response = json.loads("""{"id": 5, "name": "DELETE_ME_USER"}""")        

        post_response = client.post("/examples/", data = """{"name":"DELETE_ME_USER"}""", headers = headers)
        post_response_json = json.loads(post_response.data)

        assert post_response.status_code == 201
        assert expected_post_response == post_response_json

        delete_response = client.delete("/examples/5")

        assert delete_response.status_code == 204
        assert delete_response.data == b''
