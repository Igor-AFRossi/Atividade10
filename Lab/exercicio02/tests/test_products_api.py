import pytest
import requests

BASE = "https://fakestoreapi.com"

@pytest.mark.api
def test_listar_produtos():
    response = requests.get(f"{BASE}/products")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "title" in data[0]

@pytest.mark.api
def test_buscar_produto_por_id():
    response = requests.get(f"{BASE}/products/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data

@pytest.mark.api
def test_filtrar_por_categoria():
    response = requests.get(f"{BASE}/products/category/electronics")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for item in data:
        assert item.get("category") == "electronics"

@pytest.mark.api
def test_schema_produto_basico():
    response = requests.get(f"{BASE}/products/1")
    assert response.status_code == 200
    data = response.json()
    for key in ["id", "title", "price", "category", "description", "image"]:
        assert key in data

@pytest.mark.api
def test_limite_retornado():
    response = requests.get(f"{BASE}/products?limit=5")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= 5
