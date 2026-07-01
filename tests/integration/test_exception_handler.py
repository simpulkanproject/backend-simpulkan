from fastapi.testclient import TestClient
from app.main import app
from pytest import fixture
from fastapi import status


class TestExceptionHandler:
    @fixture
    def client(self):
        return TestClient(app)

    def test_unknown_route_returns_404(self, client):
        response = client.get("/hehe")

        body = response.json()

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert body["success"] is False
        assert body["message"] == "Not Found"
        assert body["data"] is None

    def test_method_not_allowed_returns_405(self, client):
        response = client.post("/health")

        body = response.json()

        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert body["success"] is False
        assert body["message"] == "Method Not Allowed"
        assert body["data"] is None
