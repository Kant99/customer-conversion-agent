def recommend_product(customer, products):
    """
    Select the best matching product for a customer based on eligibility.
    Returns structured output with reasoning.
    """

    for product in products:
        reasons = []

        # Check eligibility conditions
        if customer["income"] >= product["min_income"]:
            reasons.append("Income meets requirement")

        if customer["credit_score"] >= product["min_credit_score"]:
            reasons.append("Credit score meets requirement")

        # If both conditions satisfied → recommend product
        if len(reasons) == 2:
            return {
                "product": product["name"],
                "reason": ", ".join(reasons)
            }

    # If no product matched
    return {
        "product": None,
        "reason": "Customer does not meet eligibility criteria"
    }


def generate_recommendations(evaluated_customers, products):
    """
    Generate recommendations for filtered customers.
    Skips low-probability customers.
    """

    results = []

    for entry in evaluated_customers:
        customer = entry["customer"]
        score = entry["score"]
        category = entry["category"]

        # Skip low likelihood customers
        if category == "Low":
            continue

        recommendation = recommend_product(customer, products)

        results.append({
            "customer": customer,
            "score": score,
            "category": category,
            "reasons": entry["reasons"],  # from scoring_tool
            "recommendation": recommendation
        })

    return results