```python
import pytest
from requests import Session

@pytest.fixture
def base_url():
    return "https://example.com/api"

@pytest.fixture
def auth_headers(base_url):
    session = Session()
    response = session.post(f"{base_url}/login", json={"username": "user123", "password": "pass456"})
    access_token = response.json().get("access_token")
    return {"Authorization": f"Bearer {access_token}"}

def test_user_login(base_url, auth_headers):
    with Session() as session:
        response = session.get(f"{base_url}/dashboard", headers=auth_headers)
        assert response.status_code == 200
```

Note: This script assumes a login endpoint that returns an access token and a dashboard endpoint. The actual implementation details (like API endpoints, authentication logic) should be adjusted according to the application's requirements.