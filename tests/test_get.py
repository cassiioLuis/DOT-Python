import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)       #Valida que é uma lista (array)

    for item in data:
        assert isinstance(item, dict)   #Valida que cada item da lista é um objeto JSON


def test_get_unic():
    response = requests.get(f"{BASE_URL}/posts/45")

    assert response.status_code == 200
    assert response.json() is not None  #verifica se é um JSON

    data = response.json()
    assert data["id"] == 45
    assert data["title"] == "ut numquam possimus omnis eius suscipit laudantium iure"
    assert data["body"] == "est natus reiciendis nihil possimus aut provident\nex et dolor\nrepellat pariatur est\nnobis rerum repellendus dolorem autem"
    assert data["userId"] == 5


def test_not_found():
    response = requests.get(f"{BASE_URL}/posts/-1")
    assert response.status_code == 404
