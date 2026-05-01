import json

def fetch_customers():
    with open("data/customers.json", "r") as f:
        return json.load(f)