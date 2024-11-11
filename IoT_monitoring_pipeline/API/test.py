import requests

BASE_URL = "http://127.0.0.1:8000"

def test_get_all_iot():
    query = """
    query {
        IoTs {
            Adresse
            Speed
            Mileage

            
        }
    }
    """
    response = requests.post(f"{BASE_URL}/graphql", json={"query": query})
    assert response.status_code == 200
    data = response.json()
    assert "errors" not in data
    assert "data" in data
    users = data["data"]
    print(users)
    assert len(users) > 0


test_get_all_iot()

