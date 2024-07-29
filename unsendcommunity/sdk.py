import requests
import json
from dotenv import load_dotenv
import os
from typing import Optional, Dict, Any

load_dotenv()

class Unsend:
    def __init__(self, key: Optional[str] = None, url: Optional[str] = None):
        self.key = key or os.getenv("UNSEND_API_KEY")
        if not self.key:
            raise ValueError('Missing API key. Pass it to the constructor `Unsend(key="us_123")`')
        
        self.url = (url or os.getenv("UNSEND_BASE_URL", "https://app.unsend.dev")) + "/api/v1"
        self.headers = {
            "Authorization": f"Bearer {self.key}",
            "Content-Type": "application/json"
        }

    def _fetch_request(self, path: str, method: str, body: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        response = requests.request(
            method,
            self.url + path,
            headers=self.headers,
            data=json.dumps(body) if body else None
        )

        default_error = {
            "code": "INTERNAL_SERVER_ERROR",
            "message": response.reason
        }

        if response.status_code >= 400:
            try:
                resp_json = response.json()
                if "error" in resp_json:
                    return {"data": None, "error": resp_json["error"]}
                return {"data": None, "error": resp_json}
            except ValueError:
                return {"data": None, "error": default_error}

        data = response.json()
        return {"data": data, "error": None}

    def post(self, path: str, body: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return self._fetch_request(path, "POST", body)

    def get(self, path: str) -> Dict[str, Any]:
        return self._fetch_request(path, "GET")

    def put(self, path: str, body: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return self._fetch_request(path, "PUT", body)

    def patch(self, path: str, body: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return self._fetch_request(path, "PATCH", body)

    def delete(self, path: str, body: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return self._fetch_request(path, "DELETE", body)

    def send_email(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        return self.post("/emails", payload)
    
    def get_email(self, email_id: str) -> Dict[str, Any]:
        return self.get(f"/emails/{email_id}")
    
    def get_domain(self) -> Dict[str, Any]:
        return self.get("/domains")