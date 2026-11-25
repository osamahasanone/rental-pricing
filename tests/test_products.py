def test_list_products(client):
    response = client.get("/products")
    assert response.status_code == 200
    assert [p["name"] for p in response.json()] == ["iPhone 15", "MacBook Air", "PlayStation 5"]


def test_get_unknown_product_returns_404(client):
    response = client.get("/products/999")
    assert response.status_code == 404


def test_product_price_one_month(client):
    response = client.get("/products/1/price", params={"months": 1})
    assert response.status_code == 200
    assert response.json()["monthly_price"] == "100.00"


def test_product_price_three_months(client):
    response = client.get("/products/1/price", params={"months": 3})
    assert response.json()["monthly_price"] == "95.00"
