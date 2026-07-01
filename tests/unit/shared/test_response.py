import json

from fastapi import status
from fastapi.responses import JSONResponse

from app.shared.utils.response import ResponseFactory

from pytest import fixture

class TestResponse:

    @fixture
    def success_response(self):
        return ResponseFactory.success(
            message="API is running",
            data={"status": "ok"}
        )
    
    @fixture
    def created_response(self):
        return ResponseFactory.created(
            message="Resource created",
            data={"id": "123"}
        )

    @fixture
    def bad_request_response(self):
        return ResponseFactory.bad_request("Invalid URL")
    
    @fixture
    def not_found_response(self):
        return ResponseFactory.not_found("News analysis not found")
    
    @fixture
    def internal_server_error_response(self):
        return ResponseFactory.internal_server_error()

        
    def get_response_body(self, response: JSONResponse) -> dict:
        return json.loads(response.body.decode())


    def test_success_response_returns_200(self, success_response):
        body = self.get_response_body(success_response)

        assert success_response.status_code == status.HTTP_200_OK
        assert body["success"] is True
        assert body["message"] == "API is running"
        assert body["data"] == {"status": "ok"}
    
    def test_bad_request_response_returns_400(self, bad_request_response):
        body = self.get_response_body(bad_request_response)

        assert bad_request_response.status_code == status.HTTP_400_BAD_REQUEST
        assert body["success"] is False
        assert body["message"] == "Invalid URL"
        assert body["data"] is None
    
    def test_created_response(self, created_response):
        body = self.get_response_body(created_response)

        assert created_response.status_code == status.HTTP_201_CREATED
        assert body["success"] is True
        assert body["message"] == "Resource created"
        assert body["data"] == {"id": "123"}
    
    def test_not_found_response(self, not_found_response):
        body = self.get_response_body(not_found_response)

        assert not_found_response.status_code == status.HTTP_404_NOT_FOUND
        assert body["success"] is False
        assert body["message"] == "News analysis not found"
        assert body["data"] is None
    
    def test_internal_server_error_response(self, internal_server_error_response):
        body = self.get_response_body(internal_server_error_response)

        assert internal_server_error_response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert body["success"] is False
        assert body["message"] == "Internal server error"
        assert body["data"] is None