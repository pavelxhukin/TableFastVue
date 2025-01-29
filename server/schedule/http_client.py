import httpx
from fastapi import HTTPException

class HTTPClient:
    def __init__(self, ):
        self.base_url = "http://user_api:8000"
        self.endpoint = "auth"
        self.client = httpx.Client




class RpcClient(HTTPClient):
    def call(self, token: str, ):
        with self.client() as client:
            response = client.post(
                f"{self.base_url}/{self.endpoint}",
                json={"token":token}
            )
        
        # Проверка успешности запроса
        if response.status_code == 200:
            username = response.json().get("username")
            return username  # возвращаем ответ в формате JSON
        else:
            print(response.text)
            raise HTTPException(status_code=401, detail=response.text)