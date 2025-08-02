import requests

API_BASE = "http://localhost:8000/api/products/"  # رابط النظام الأول
API_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU0MTc0NDcyLCJpYXQiOjE3NTQwODgwNzIsImp0aSI6Ijg2NjBhMWE0NzNhMjRmODM5M2VmOWM0ZjViOGY4MDQyIiwidXNlcl9pZCI6MX0._kwRA-qW2NMi8Luwz2PKH2-Kc1e7-K8KHswvpNbUSmY"  # أو خلّيه None لو ما في توثيق

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}" if API_TOKEN else "",
    "Content-Type": "application/json"
}


def get_all_products():
    response = requests.get(API_BASE, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching products: {response.status_code}")
        return []


def get_product(product_id):
    response = requests.get(f"{API_BASE}{product_id}/", headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching product {product_id}")
        return None


def update_product(product_id, data: dict):
    response = requests.put(f"{API_BASE}{product_id}/", json=data, headers=HEADERS)
    return response.status_code, response.json()

def add_product(data):
    """
    data = {
        "name": "New Product",
        "description": "Description here",
        "price": "99.99",
        "stock": 10,
        "categories": [1, 2],  # IDs of categories
        "detail": {
            "manufacturer": "Company X",
            "warranty_period": 12
        }
    }
    """
    headers = {"Content-Type": "application/json"}
    response = requests.post(API_BASE, json=data, headers=HEADERS)

    if response.status_code == 201:  # Created
        return response.json()
    else:
        print(f"Failed to add product: {response.status_code}")
        print(response.text)
        return None
