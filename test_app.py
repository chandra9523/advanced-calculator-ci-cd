from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# ✅ Basic tests
def test_home():
    assert client.get("/").status_code == 200

def test_add():
    assert client.get("/add/2/3").json() == {"result": 5}

def test_subtract():
    assert client.get("/subtract/5/3").json() == {"result": 2}

def test_multiply():
    assert client.get("/multiply/2/3").json() == {"result": 6}

def test_divide():
    assert client.get("/divide/6/3").json() == {"result": 2.0}

def test_power():
    assert client.get("/power/2/3").json() == {"result": 8}

# ⚠️ Edge cases
def test_divide_by_zero():
    response = client.get("/divide/5/0")
    assert response.status_code == 400

def test_negative_numbers():
    assert client.get("/add/-2/-3").json() == {"result": -5}

def test_float_numbers():
    assert client.get("/add/2.5/3.5").json() == {"result": 6.0}

def test_large_numbers():
    assert client.get("/multiply/100000/100000").json() == {"result": 10000000000}

# ❌ Invalid input
def test_invalid_input():
    response = client.get("/add/a/b")
    assert response.status_code == 422