from fastapi.testclient import TestClient
from app.main import app

client = TestClient

def test_get_comercialization():
    """
    Test the /comercialization/{year} endpoint.
    """
    year = 2023
    response = client.get(f"/comercialization/{year}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    # assert len(data) > 0