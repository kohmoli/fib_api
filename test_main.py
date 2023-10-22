from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_fib():
    response = client.get('/fib?n=1')
    assert response.status_code == 200
    assert 'result' in response.json()
