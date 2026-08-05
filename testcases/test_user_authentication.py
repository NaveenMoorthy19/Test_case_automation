```python
import pytest
from requests import post

@pytest.fixture
def auth_headers(requests_session):
    return {
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
    }

@pytest.mark.usefixtures("auth_headers")
def test_user_login_valid_credentials(base_url, requests_session):
    response = requests_session.post(f"{base_url}/login", json={"username": "user@example.com", "password": "securepassword"})
    
    assert response.status_code == 200
    assert 'access_token' in response.json()
    
    # Assuming dashboard endpoint requires access token for authorization
    dashboard_response = requests_session.get(f"{base_url}/dashboard", headers=response.json()['headers'])
    assert dashboard_response.status_code == 200
```

Note: Replace `YOUR_ACCESS_TOKEN` with actual access token and ensure the base URL is correctly set in your environment.