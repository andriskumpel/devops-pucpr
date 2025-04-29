import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"Hello": "World"}

def test_helloworld_with_q():
    r = client.get("/helloworld", params={"item_id": 1, "q": "abc"})
    assert r.status_code == 200
    assert r.json() == {"item_id": 1, "q": "abc"}

def test_helloworld_without_q():
    r = client.get("/helloworld", params={"item_id": 2})
    assert r.status_code == 200
    assert r.json() == {"item_id": 2, "q": None}

def test_funcaoteste_shape():
    r = client.get("/funcaoteste")
    data = r.json()
    assert r.status_code == 200
    assert data["teste"] is True
    assert 0 <= data["num_aleatorio"] <= 1000

def test_funcaoteste_random():
    n1 = client.get("/funcaoteste").json()["num_aleatorio"]
    n2 = client.get("/funcaoteste").json()["num_aleatorio"]
    # garante que a chamada sempre executa sem erro
    assert isinstance(n1, int) and isinstance(n2, int)
