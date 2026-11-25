import pytest


def test_create_order(client):
    response = client.post("/orders", json={"customer_id": 1, "product_id": 1, "months": 3})
    assert response.status_code == 201
    body = response.json()
    assert body["monthly_price"] == "95.00"
    assert body["status"] == "approved"


def test_create_order_unknown_customer_returns_404(client):
    response = client.post("/orders", json={"customer_id": 999, "product_id": 1, "months": 3})
    assert response.status_code == 404


def test_create_order_invalid_months_returns_422(client):
    response = client.post("/orders", json={"customer_id": 1, "product_id": 1, "months": 5})
    assert response.status_code == 422


@pytest.mark.skip(reason="Task 5: retries must not create duplicate orders")
def test_same_idempotency_key_returns_the_same_order(client):
    payload = {"customer_id": 1, "product_id": 1, "months": 3}
    headers = {"Idempotency-Key": "checkout-abc-123"}

    first = client.post("/orders", json=payload, headers=headers)
    second = client.post("/orders", json=payload, headers=headers)

    assert first.status_code == 201
    assert second.status_code in (200, 201)
    assert second.json()["id"] == first.json()["id"]
