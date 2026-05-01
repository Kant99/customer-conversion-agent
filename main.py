from tools.data_tool import fetch_customers

if __name__ == "__main__":
    customers = fetch_customers()
    print(f"Loaded {len(customers)} customers")