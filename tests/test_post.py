import requests
from faker import Faker

BASE_URL = "https://jsonplaceholder.typicode.com"

fake = Faker()

def test_post_success():
    payload = { 
        "userId": fake.random_int(min=1, max=100),
        "title": fake.sentences(nb=5),
        "body": fake.paragraph(nb_sentences=3),
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["userId"] == payload["userId"]
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]

    assert "id" in data                 # Verifica se a chave ID está presente no retorno
    assert isinstance(data["id"], int)  # Valida que é um número
    assert data["id"] > 0               # Valida que o ID gerado é um número positivo