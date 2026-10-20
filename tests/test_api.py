from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Knowledge Assistant API is running"}


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ask_endpoint(monkeypatch):
    async def fake_generate_answer(question: str) -> str:
        return f"AI answer to: {question}"


    monkeypatch.setattr(
        "app.services.generate_answer",
        fake_generate_answer,
    )

    response = client.post("/ask", json={"question": "Explain RAG"},)

    assert response.status_code == 200
    assert response.json()["answer"] == "AI answer to: Explain RAG"
    assert response.json()["status"] == "completed"


def test_info_endpoint():
    response = client.get("/info")

    assert response.status_code == 200
    assert response.json() == {"service": "knowledge-assistant"}


def test_ask_endpoint_rejects_short_question():
    response = client.post("/ask", json={"question": "Hi"})

    assert response.status_code == 422
