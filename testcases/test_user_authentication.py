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
        session.headers.update(auth_headers)
        response = session.get(f"{base_url}/dashboard")
        assert response.status_code == 200
```

Note: The above script assumes a login endpoint at `/login` that returns an access token and a dashboard endpoint at `/dashboard`. Adjust the URLs and authentication logic as per your actual API.