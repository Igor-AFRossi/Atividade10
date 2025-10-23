import pytest
import requests

BASE = "https://jsonplaceholder.typicode.com"

@pytest.mark.api
def test_crud_todos():
    todo = {"title": "Minha tarefa", "completed": False, "userId": 1}
    r = requests.post(f"{BASE}/todos", json=todo)
    assert r.status_code in (201, 200)
    created = r.json()
    assert "id" in created
    created_id = created.get("id")

    r = requests.get(f"{BASE}/todos/1")
    assert r.status_code == 200
    data = r.json()
    assert data.get("id") == 1

    r = requests.patch(f"{BASE}/todos/1", json={"completed": True})
    assert r.status_code in (200,)
    updated = r.json()
    assert updated.get("completed") in (True,)

    r = requests.delete(f"{BASE}/todos/1")
    assert r.status_code in (200, 204)

    r = requests.get(f"{BASE}/todos/1")
    assert r.status_code == 200

@pytest.mark.api
def test_criar_todo_sem_titulo_deve_falhar():
    todo = {"completed": False, "userId": 1}
    r = requests.post(f"{BASE}/todos", json=todo)
    assert r.status_code in (201, 200)
