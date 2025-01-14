from http import HTTPStatus
import json
import pytest

from config import app

class TestHealthCheckController:

    def test_health_check(self, client):
        expected_response = json.loads("""{"status": "ok"}""")
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

        response = client.get("/health/", headers=headers)
        print(response.status_code)
        print(response.headers)
        actual_response = response.get_json()
        assert response.status_code == HTTPStatus.OK
        assert expected_response == actual_response
